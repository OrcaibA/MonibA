#!/bin/bash

echo "Creating project structure..."

PROJECT="MonibA"


mkdir -p config
mkdir -p controllers
mkdir -p routes
mkdir -p services
mkdir -p middlewares
mkdir -p utils
mkdir -p uploads
mkdir -p auth
mkdir -p logs


touch app.js
touch server.js
touch .env
touch config/env.js
touch config/whatsapp.js
touch controllers/controller.js
touch routes/routes.js
touch services/service.js
touch middlewares/error.js
touch middlewares/validation.js
touch utils/logger.js
touch utils/response.js

echo "Project structure created successfully!"
