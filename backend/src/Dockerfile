# 1. Use a lightweight Python image
FROM python:3.12

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the project files into the container
COPY . /app

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the application port (if your app runs on a specific port)
EXPOSE 8000

# 6. Command to run the application
CMD ["python", "run.py"]
