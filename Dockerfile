# 1. Start with a base OS that has Python installed
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies first (for caching speed)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install -r requirements.txt

# 5. Copy the rest of our app code 
COPY . .

# 6. Expose the port so we can access it
EXPOSE 5000

# 7. The command to run when the container starts
CMD ["python", "app.py"]