pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/weather-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-app .'
            }
        }
        stage('Test Application') {
            steps {
                sh 'echo "Running tests..."'
                sh 'python -m py_compile app.py'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name weather-container weather-app || docker restart weather-container'
            }
        }
    }
}
