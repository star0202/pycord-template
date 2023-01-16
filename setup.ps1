Copy-Item .env.example .env
New-Item database.db
python -m venv venv
./venv/Scripts/pip install -r requirements.txt
./venv/Scripts/activate