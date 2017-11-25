from tags.models import Tag
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer

class TagService(object):
    @classmethod
    def get_related_tags(cls, user):
        users = UserProfileSerializer(UserProfile.objects.all(), many=True).data
        user = UserProfileSerializer(user.profile).data
        print users, user
        # user = UserProfileSerializer(data=)
        # user.save()
