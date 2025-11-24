FROM python:3.11-slim

WORKDIR /app

# Cài gunicorn trước
RUN pip install --no-cache-dir gunicorn

# Copy và cài requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code
COPY . .

# Tạo thư mục
RUN mkdir -p instance uploads static/uploads

EXPOSE 5000

# Chạy gunicorn trên port 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "--timeout", "120", "run:app"]