#!/bin/bash

echo "Creating project structure..."

PROJECT="MonibA"


mkdir -p app/core
mkdir -p app/api
mkdir -p app/services
mkdir -p app/utils
mkdir -p app/models

touch app/core/config.py
touch app/core/logger.py

touch app/api/routes.py
touch app/services/google_sheet.py
touch app/services/monitor.py
touch app/services/whatsapp.py
touch app/services/formatter.py
touch app/services/state

touch requirements.txt
touch Dockerfile
touch .env
touch .gitignore
touch README.md
touch main.py

mkdir -p storage
touch storage/state.json
mkdir -p sessions/chrome

touch app/services/image_builder.py
echo "Project structure created successfully!"
