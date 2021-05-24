from django.db import models
import random, string, datetime
# Create your models here.


class UUID(models.Model):

    date = models.DateTimeField(auto_now=True)
    uuid = models.CharField(max_length=32)

    @staticmethod
    def generate_random_code():

        source = string.ascii_letters + string.digits
        rand_str = ''.join((random.choice(source) for i in range(35)))

        return {
            "rand_value":rand_str
         }

    @staticmethod
    def create_new_uuid():

        uuid = UUID.generate_random_code().get("rand_value")

        new_uuid = UUID(uuid = uuid)
        new_uuid.save()

        return {
            "status": True,
            "uuid": new_uuid
        }
   
    @staticmethod
    def get_all():

        uuids = {str(uuid.date).split("+")[0]: uuid.uuid for uuid in UUID.objects.all().order_by("-date")}
        print(uuids)

        return {
            "status": True,
            "uuids": uuids
        }