"""
General: General utilities for django.

"""

###############################################################################
## Imports
###############################################################################
from django.conf import settings
from django.contrib.auth.models import Group, SiteProfileNotAvailable
from django.core.cache import cache
from django.db.models import get_model
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.shortcuts import _get_queryset


###############################################################################
## Utils
###############################################################################
def get_or_none(klass, *args, **kwargs):
    """
    Uses get() to return an object or None if the object does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), a MultipleObjectsReturned will be raised if more
    than one object is found.

    From django-annoying: https://bitbucket.org/offline/django-annoying
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None


def get_profile_model():
    """
    Return the model class for the currently-active user profile
    model, as defined by the ``AUTH_PROFILE_MODULE`` setting.

    :return: The model that is used as profile.
    """
    if (not hasattr(settings, 'AUTH_PROFILE_MODULE')) or \
           (not settings.AUTH_PROFILE_MODULE):
        raise SiteProfileNotAvailable

    profile_mod = get_model(*settings.AUTH_PROFILE_MODULE.split('.'))
    if profile_mod is None:
        raise SiteProfileNotAvailable
    return profile_mod


def get_group(name):
    """
    Return group with given name, if it exists. Check cache first.
    """
    group = cache.get('djutils.general.group_%s' % name)
    if not group:
        group = Group.objects.get(name=name)
        cache.set('djutils.general.group_%s' % name, group, 365 * 24 * 60 * 60)
    return group


@receiver(post_delete, sender=Group,
    dispatch_uid='djutils.general.group_post_delete')
@receiver(post_save, sender=Group,
    dispatch_uid='djutils.general.group_post_save')
def group_post_save_delete(sender, instance, created, **kwargs):
    cache.delete('djutils.general.group_%s' % instance.name)
