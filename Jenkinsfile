pipeline {
    agent any

    environment {
        IMAGE_NAME = "weather-app"
        DOCKER_REG = "docker.io"            // for docker hub use docker.io/yourusername
        DOCKER_IMAGE = "${DOCKER_REG}/${DOCKER_USERNAME}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
    }

    parameters {
        booleanParam(name: 'PUSH_TO_DOCKER_HUB', defaultValue: false, description: 'Push built image to Docker Hub')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<yourusername>/weather-app.git'
            }
        }

        stage('Unit Tests / Lint (optional)') {
            steps {
                // Example: for python you might run unit tests
                sh '''
                   if [ -f requirements.txt ]; then
                       echo "No tests configured. You can add pytest or linters here."
                   fi
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build image tagged with build number
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Push to Docker Hub (optional)') {
            when { expression { params.PUSH_TO_DOCKER_HUB } }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKER_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }

        stage('Deploy (Run container)') {
            steps {
                script {
                    // Stop & remove existing container if present, then run new
                    sh '''
                    if docker ps -q --filter "name=weather-app-container" | grep -q .; then
                      echo "Restarting existing container..."
                      docker rm -f weather-app-container
                    fi
                    docker run -d --name weather-app-container -p 5000:5000 ${IMAGE_NAME}:${BUILD_NUMBER}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Build: ${env.BUILD_NUMBER}"
        }
        success {
            echo "Build succeeded"
        }
        failure {
            echo "Build failed"
        }
    }
}
