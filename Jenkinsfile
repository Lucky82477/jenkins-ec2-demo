pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Lucky82477/jenkins-ec2-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-ec2-demo:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f jenkins-demo || true
                docker run -d -p 5000:5000 --name jenkins-demo jenkins-ec2-demo:latest
                '''
            }
        }
    }
}
