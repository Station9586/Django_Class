class Mydb3Router: 
    def db_for_read(model, **hints):
        if model._meta.app_label == 'DB':
            return 'mydb3'
        return None

    def db_for_write(model, **hints):
        if model._meta.app_label == 'DB':
            return 'mydb3'
        return None

    def allow_relation(obj1, obj2, **hints):
        if obj1._meta.app_label == 'DB' and obj2._meta.app_label == 'DB':
            return True
        return None

    def allow_migrate(db, app_label, model_name=None, **hints):
        if app_label == 'DB':
            return db == 'mydb3'
        elif db == 'mydb3':
            return False
        return None