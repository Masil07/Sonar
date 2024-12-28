pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python312\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                if exist requirements.txt (
                    echo "Installing dependencies from requirements.txt..."
                    pip install -r requirements.txt
                ) else (
                    echo "No requirements.txt found. Skipping dependency installation."
                )
                '''
            }
        }

        stage('Run Unit Tests and Generate Coverage') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                coverage run --source=. -m unittest discover
                coverage xml -o coverage.xml
                if exist coverage.xml (
                    echo "Coverage report generated successfully."
                ) else (
                    echo "Error: Coverage report not found!"
                    exit /b 1
                )
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token')
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=github_trial1 ^
                              -Dsonar.projectName=Trial1 ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.cpd.exclusions=**/test/** ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.login=%SONAR_TOKEN%
                '''
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
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
