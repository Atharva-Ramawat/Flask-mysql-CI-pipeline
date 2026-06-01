FROM python:3.9-slim

WORKDIR /app

# Create a non-privileged user
RUN addgroup --system appuser && adduser --system --ingroup appuser appuser

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and set ownership
COPY . .
RUN chown -R appuser:appuser /app

# Switch to the non-privileged user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
