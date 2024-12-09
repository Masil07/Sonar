pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Set the PATH and install dependencies using pip
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
            }
        }
        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=github_trial1 \
                              -Dsonar.projectName=Trial1 \
                              -Dsonar.sources=. \
                              -Dsonar.host.url=http://localhost:9000 \
                              -Dsonar.token=%SONAR_TOKEN%
                '''
            }
        }
        stage('Quality Gate') {
            steps {
                script {
                    sleep 30
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Pipeline aborted due to quality gate failure: ${qg.status}"
                    }
                }catch (Exception e) {
                echo "An error occurred while waiting for the quality gate: ${e.getMessage()}"
                throw e
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
