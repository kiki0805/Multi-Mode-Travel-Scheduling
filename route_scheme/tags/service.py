from tags.models import Tag
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer

class TagService(object):
    @classmethod
    def get_related_tags(cls, user):
        print user.profile.tags.all()
        # user = UserProfileSerializer(data=)
        # user.save()
