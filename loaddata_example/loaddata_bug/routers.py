class AppRouter:
    app_router_map = {
        'app_two': 'db_two',
    }

    def _get_route(self, app):
        return self.app_router_map.get(app, None)

    def db_for_read(self, model, **hints):
        return self._get_route(model._meta.app_label)

    def db_for_write(self, model, **hints):
        return self._get_route(model._meta.app_label)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        result = None
        if db != 'default':
            result = False
        if self._get_route(app_label):
            # only allow migrations for that database
            result = db == self._get_route(app_label)
        return result
