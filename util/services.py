from xml.dom import ValidationErr
from menu.models import Menu
import openpyxl
from datetime import timedelta

def get_excel_sheet(excel_file):
    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb["주간메뉴표"]
    wb.active
    return worksheet

def make_menu(
    worksheet, place, day, date,
    content_start, content_end,
    time, type=""):
    calorie = worksheet[day][content_end].value
    calorie = parse_calorie(calorie)
    contents = ""
    for cell in worksheet[day][content_start:content_end]:
        if cell.value is not None and cell.value != "★":
            contents += str(cell.value) + "\n"
    contents = contents.rstrip('\n')
    try:
        menus = Menu.objects.create(
        place=place,
        date=date,
        content=contents,
        calorie=calorie,
        time=time,
        type=type
        )
    except:
        raise ValidationErr("Upload failed")
    return menus

def make_7dates(day):
    dates = [day]
    for i in range(1, 7):
        dates.append(day + timedelta(days=i))
    return dates

def parse_calorie(calorie):
    if calorie is None:
        return None
    if isinstance(calorie, int):
        return calorie
    if calorie.find(",") != -1:
        calorie = calorie.replace(",", "")
    if calorie.find("Kcal") != -1:
        calorie = calorie.split("Kcal")[0]
    print("calorie", calorie)
    return int(calorie)
    