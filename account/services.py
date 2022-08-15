from account.models import User


def fetch_users():
    conditions = {}
    users = User.objects.filter(**conditions).all()
    return users

def create_user(kakao_id, email):
    return User.objects.create(
            kakao_id=kakao_id,
            email=email
        )