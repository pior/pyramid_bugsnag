from typing import Any, Callable, Dict  # noqa
import logging

import bugsnag
import pyramid.registry
import pyramid.response  # noqa
import pyramid.request  # noqa

log = logging.getLogger('pyramid_bugsnag')


def get_route_name(request):  # type: (pyramid.request.Request) -> str
    """Get a route name from URL Dispatch or Traversal."""
    if request.matched_route:
        return str(request.matched_route.name)

    return 'no-matched-route'


def extract_context(request):  # type: (pyramid.request.Request) -> str
    parts = [request.method, get_route_name(request)]
    return ' '.join(parts)


def extract_user(request):  # type: (pyramid.request.Request) -> Dict[str, str]
    user_id = (
        request.unauthenticated_userid
        or request.remote_user
        or request.remote_addr
    )
    return {'id': user_id}


def extract_metadata(request):  # type: (pyramid.request.Request) -> Dict[str, Any]
    return {
        'request': {
            'method': request.method,
            'path': request.path,
            'query_string': request.query_string,
            'GET': dict(request.GET),
            'POST': dict(request.POST),
            'url': request.url,
            'user_agent': request.user_agent,
        }
    }


EXCEPTION_REASON = {
    "type": "unhandledExceptionMiddleware",
    "attributes": {
        "framework": "Pyramid"
    }
}


def handle_error(request, exception):  # type: (pyramid.request.Request, Exception) -> None
    try:
        bugsnag.notify(
            exception,
            context=extract_context(request),
            user=extract_user(request),
            metadata=extract_metadata(request),
            severity_reason=EXCEPTION_REASON,
        )
    except Exception:
        log.exception("Error in Bugsnag tween")


_HandlerType = Callable[[pyramid.request.Request], pyramid.response.Response]


def tween_factory(handler, registry):  # type: (_HandlerType, pyramid.registry.Registry) -> _HandlerType
    def tween(request):  # type: (pyramid.request.Request) -> pyramid.response.Response
        try:
            response = handler(request)
        except Exception as exc:
            handle_error(request, exc)
            raise

        if request.exception is not None:
            handle_error(request, request.exception)

        return response

    return tween
