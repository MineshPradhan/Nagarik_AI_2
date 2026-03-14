FROM node:20 as frontend-build

WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend .
RUN npm run build


FROM python:3.11

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend .

COPY --from=frontend-build /frontend/dist ./static

RUN pip install uvicorn fastapi

EXPOSE 10000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","10000"]