from django.contrib.auth.models import User
from account.models import Student


class StudentIDModelBackend(object):


    def authenticate(self, student_id=None, password=None):
        if isinstance(student_id, int):

            try:
                user = Student.objects.get(student_id=student_id).user
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None
        else:
            try:
                user = User.objects.get(username=student_id)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None