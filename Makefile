# pyenv, virtualenvs 설치 후 진행
# python 버전은 3.9.2 사용
###############################################################################################
# pyenv install 3.9.2
# pyenv virtualenv 3.9.2 unist-meal-backend
# pyenv local unist-meal-backend
###############################################################################################

# 초기 설정
init:
	pip install -r requirements.txt

# 서버 구동
run-server:
	python manage.py migrate
	python manage.py runserver

# requirements.txt 저장
save-requirements:
	pip freeze > requirements.txt

# heroku 서버 배포
deploy:
	git push heroku main
	heroku run python manage.py migrate
	heroku run python manage.py collectstatic --noinput
	heroku restart

# migrate 실행
migrate:
	python manage.py makemigrations
	python manage.py migrate

# test 실행
test:
	python manage.py test