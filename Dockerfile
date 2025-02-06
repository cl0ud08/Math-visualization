# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Fix PATH issue to find streamlit
ENV PATH="/root/.local/bin:${PATH}"

# Run the Streamlit app
CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
