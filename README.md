# 실행 방법

```shell
# be-django 폴더 안에서 다음의 명령을 수행
pip install -r requirements.txt
git submodule init
git submodule update --remote
python iotProject/manage.py makemigrations
python iotProject/manage.py migrate
python iotProject/manage.py runserver
```
