from django.db.backends.base.features import BaseDatabaseFeatures

class DatabaseFeatures(BaseDatabaseFeatures):
   supports_transactions=False
