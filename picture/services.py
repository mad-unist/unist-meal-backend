from picture.models import Picture


def fetch_pictures():
    conditions = {}
    pictures = Picture.objects.filter(**conditions).all()
    return pictures
