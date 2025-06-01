### 5. README.md
```
# Flask Microservice

## Setup
1. Build image: `docker build -t project3-app .`
2. Run container:
   ```bash
   docker run -e DB_HOST=<host> \
              -e DB_NAME=<db> \
              -e DB_USER=<user> \
              -e DB_PASS=<pass> \
              -p 3000:3000 \
              project3-app
   ```
3. Test endpoints:
   - `GET http://localhost:3000/health`
   - `GET http://localhost:3000/items`
   - `POST http://localhost:3000/items` with JSON `{ "name": "example" }`


Kick of a new test to see CICD working 