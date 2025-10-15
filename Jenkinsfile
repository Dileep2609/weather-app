pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Dileep2609/weather-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''
                if docker ps -q --filter "name=weather-app-container" | grep -q .; then
                    docker rm -f weather-app-container
                fi
                docker run -d -p 5000:5000 --name weather-app-container weather-app
                '''
            }
        }
    }
}

