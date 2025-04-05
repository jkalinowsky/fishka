pipeline {
    agent any
    
    tools {
        nodejs 'node16'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test Backend') {
            steps {
                dir('backend') {
                    script {
                        docker.image('python:3.9').inside {
                            sh 'pip install -r requirements.txt'
                            sh 'pytest'
                        }
                    }
                }
            }
        }
        
        stage('Test Frontend') {
            steps {
                dir('frontend/angular-app') {
                    script {
                        docker.image('node:16').inside {
                            sh 'npm install'
                            sh 'npm test'
                        }
                    }
                }
            }
        }
        
        stage('Build and Deploy') {
            steps {
                script {
                    sh 'docker-compose up -d --build'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
