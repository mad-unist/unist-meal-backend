from menu.models import Menu


def fetch_menus():
    conditions = {}
    menus = Menu.objects.filter(**conditions).all()
    return menus
