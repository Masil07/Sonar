pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Install dependencies and run tests using the full path to pip
                bat 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token')
            }
            steps {
                bat '''
                sonar-scanner -Dsonar.projectKey=github_trial1 \
                              -Dsonar.projectName=Trial1 \
                              -Dsonar.sources=. \
                              -Dsonar.host.url=http://localhost:9000 \
                              -Dsonar.login=%SONAR_TOKEN%
                '''
            }
        }
        stage('Quality Gate') {
            steps {
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Pipeline aborted due to quality gate failure: ${qg.status}"
                    }
                }
            }
        }
    }
}