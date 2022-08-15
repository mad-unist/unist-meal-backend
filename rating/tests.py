from datetime import datetime, timedelta
from django.urls import reverse
from rest_framework.test import APITestCase as TestCase

from menu.models import Menu
from rating.models import Rating
from account.models import User

# Create your tests here.
class RatingTest(TestCase):
    def setUp(self):
        self.users = User.objects.bulk_create([
            User(id=1, email="user1@gmail.com"),
            User(id=2, email="user2@gmail.com"),
            User(id=3, email="user3@gmail.com"),
        ])
        
    def test_get_list_ok(self):
        # given
        menu = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        Rating.objects.bulk_create([
            Rating(user_id=self.users[0].id, menu_id=menu.id, rating=5),
            Rating(user_id=self.users[1].id, menu_id=menu.id, rating=5),
            Rating(user_id=self.users[2].id, menu_id=menu.id, rating=5),
        ])
        
        # when
        url = reverse("rating:v1_rating_list")
        response = self.client.get(url)
        
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 3)
        
    def test_post_ok(self):
        # given
        menu = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        
        # when
        url = reverse("rating:v1_rating_list")
        response = self.client.post(url, {"user_id": self.users[0].id, "menu_id": menu.id, "rating": 5})
        
        # then
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.filter(id=response.json()["data"]["id"]).exists(), True)
        
    def test_update_rating_when_existing_rating(self):
        # given
        menu = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        rating = Rating.objects.create(user_id=self.users[0].id, menu_id=menu.id, rating=5)
        
        # when
        url = reverse("rating:v1_rating_list")
        response = self.client.post(url, {"user_id": self.users[0].id, "menu_id": menu.id, "rating": 3})
        
        # then
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.get(id=rating.id).rating, 3.0)
        
    def test_cannot_create_rating_for_not_today_menu(self):
        # given
        menu = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today()+timedelta(days=1))
        
        # when
        url = reverse("rating:v1_rating_list")
        response = self.client.post(url, {"user_id": self.users[0].id, "menu_id": menu.id, "rating": 3})
        
        # then
        self.assertEqual(response.status_code, 400)
        
    def test_cannot_create_rating_for_same_time_menu(self):
        # given
        menu1 = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        menu2 = Menu.objects.create(place="학생식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        Rating.objects.create(user_id=self.users[0].id, menu_id=menu1.id, rating=5)
        
        # when
        url = reverse("rating:v1_rating_list")
        response = self.client.post(url, {"user_id": self.users[0].id, "menu_id": menu2.id, "rating": 3})
        
        # then
        self.assertEqual(response.status_code, 400)
        
    def test_delete_ok(self):
        # given
        menu = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        rating = Rating.objects.create(user_id=self.users[0].id, menu_id=menu.id, rating=5)
        
        # when
        url = reverse("rating:v1_rating_list")
        response = self.client.delete(url, {"user_id": self.users[0].id, "menu_id": menu.id})
        
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Rating.objects.filter(id=rating.id).exists(), False)
        
    def test_get_rating_list_by_user_ok(self):
        # given
        menu1 = Menu.objects.create(place="기숙사식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        menu2 = Menu.objects.create(place="학생식당", type="한식", time="점심", content="메뉴1", calorie=100, date=datetime.today())
        Rating.objects.bulk_create([
            Rating(user_id=self.users[0].id, menu_id=menu1.id, rating=5),
            Rating(user_id=self.users[1].id, menu_id=menu1.id, rating=5),
            Rating(user_id=self.users[1].id, menu_id=menu2.id, rating=5),
        ])
        
        # when
        url = reverse("rating:v1_rating_list_by_user", kwargs={"user_id": self.users[1].id})
        response = self.client.get(url)
        
        # then
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 2)