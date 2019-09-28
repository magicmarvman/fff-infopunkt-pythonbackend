from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class StrikeModel(Model):
    """
    A DynamoDB Strike
    """
    class Meta:
        table_name = "FFF-Strikes"
    strikeId = NumberAttribute(hash_key=True)
    datetime = NumberAttribute(range_key=True)
    title = UnicodeAttribute()
    latitude = NumberAttribute()
    longitude = NumberAttribute()
    url = UnicodeAttribute()
    description = UnicodeAttribute()