cd backend
redis-server --daemonize yes
python3 app.py &
celery -A app.celery beat --max-interval 1 -l info &
celery -A app.celery worker -l info &
cd ..
cd frontend
npm run serve