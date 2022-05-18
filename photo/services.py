from photo.models import Photo


def fetch_photos():
    conditions = {}
    photos = Photo.objects.filter(**conditions).all()
    return photos
