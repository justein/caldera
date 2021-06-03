from aiohttp import web


def make_app(services):
    from .responses import json_request_validation_middleware
    from .security import authentication_required_middleware_factory

    app = web.Application(
        middlewares=[
            authentication_required_middleware_factory(services['auth_svc']),
            json_request_validation_middleware
        ]
    )

    from .handlers.health_api import HealthApi
    HealthApi(services).add_routes(app)

    from .handlers.config_api import ConfigApi
    ConfigApi(services).add_routes(app)

    from .handlers.planner_api import PlannerApi
    PlannerApi(services).add_routes(app)

    from .handlers.plugins_api import PluginApi
    PluginApi(services).add_routes(app)

    return app
