# assignment-backend
### TODO application setup:
1. Pull repository.
2. Create virtual env for new application, for example with virtualenvwrapper:
```
mkvirtualenv todoapp
```
3. Install requirements from requirements.txt file:
```
pip install -r requirements.txt 
```
4. Apply migrations:
```
python manage.py migrate
```
5. Install redis server to make celery works:

Ubuntu:
```
sudo apt install redis-server
```
Fedora:
```
sudo dnf install redis
```
Mac OS X:
```
brew install redis
```
6. After it run redis server with command:
```
redis-server
```
7. In new terminal tab run django server:
```
python manage.py runserver
```
8. In another terminal tab run celery worker:
```
celery -A todoapp worker -l info
```

# Additional information.

### Run tests.

Go to the project folder and simply just run:

```
pytest
```

### API Points.

To get list of all boards and add new board:

http://127.0.0.1:8000/api/v1/board/list/

To get detail board view, update board or delete board:

http://127.0.0.1:8000/api/v1/board/detail/1/

To get list of all tasks and add new tasks:

http://127.0.0.1:8000/api/v1/tasks/list/

Yo can specify result with url parameters.
To get list of tasks which related to specific board:

http://127.0.0.1:8000/api/v1/tasks/list/?board_name=Test

To get list of tasks which are done:

http://127.0.0.1:8000/api/v1/tasks/list/?is_done=true

To get list of tasks which are done and related to specific board:

http://127.0.0.1:8000/api/v1/tasks/list/?is_done=true&board_name=Test

To get detail task view, update task or delete task:

http://127.0.0.1:8000/api/v1/tasks/detail/1/

To get list of all reminders and create new reminder:

http://127.0.0.1:8000/api/v1/reminder/list/

To get detail reminder, remove or change it:

http://127.0.0.1:8000/api/v1/reminder/detail/1/

### Notes.

After creating notification - celery task will be triggered. For example if you set to remind you in 1 minute you will see afeter 1 minute log from console email backend in opened celery worker tab. Example:
```
[2017-09-21 08:33:52,227: WARNING/ForkPoolWorker-7] Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Test subject
From: hello@test.com
To: test@test.com
Date: Thu, 21 Sep 2017 08:33:51 -0000
Message-ID: <20170921083351.14532.81422@admins-macbook-pro.local>
[2017-09-21 08:33:52,228: WARNING/ForkPoolWorker-7]
```

Good luck :) !
