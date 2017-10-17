import bugsnag
import pyramid
from pyramid.settings import asbool


BOOLEAN_SETTINGS = {
    'asynchronous',
    'auto_notify',
    'send_code',
}


def make_settings(settings):
    bugsnag_settings = {}
    for key, value in settings.items():
        if key.startswith('bugsnag.'):
            setting_key = key[len('bugsnag.'):]
            if setting_key in BOOLEAN_SETTINGS:
                value = asbool(value)
            bugsnag_settings[setting_key] = value
    return bugsnag_settings


def includeme(config):
    settings = make_settings(config.registry.settings)
    bugsnag.configure(**settings)

    config.add_tween('pyramid_bugsnag.tween.tween_factory', over=[
        pyramid.tweens.EXCVIEW,
        # if pyramid_tm is in the pipeline we want to track errors caused
        # by commit/abort so we try to place ourselves over it
        'pyramid_tm.tm_tween_factory',
    ])
