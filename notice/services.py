from notice.models import Notice


def fetch_notices():
    conditions = {}
    notices = Notice.objects.filter(**conditions).all()
    return notices

def get_notice(notice_id):
    return Notice.objects.get(id=notice_id)
    