Step 1: Install docker if not already installed
Step 2: docker-compose build
Step 3: docker-compose up -d

Setup the database: docker-compose run srm sh /app/setup.sh
Seed the databse with default values: docker-compose run srm sh /app/seed.sh
