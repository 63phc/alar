Запустить:

```
# pg в докере, если есть локальный пг то надо поменять креды в .env
cp .env.example .env 
docker-compose up
python -m venv Venv
source Venv/bin/activate
export FLASK_APP=run.py
flask db upgrade
flask run
```

1) первая часть http://127.0.0.1:5000/  креды test@test.test;test1234
2) вторая http://127.0.0.1:5000/data

```
В коде присетсвуют комментарии и есть блоки с русскими комментами там я выскаваю почему так сделано (пометил их как FIXME: чтобы легче найти)
Основанная причина почему не сделал как хотел, не охото было тратить больше чем 1 день на тестовое,
 в общей сложности ушло у меня примерно 6 часов (что очень много для тестового)