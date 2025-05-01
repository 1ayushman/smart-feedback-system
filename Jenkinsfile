pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/YOUR_USERNAME/smart-feedback-system.git'
            }
        }
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'docker build -t smart-feedback .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 smart-feedback'
            }
        }
    }
}
