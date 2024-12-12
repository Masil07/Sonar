pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                // Pull the source code from the repository
                checkout scm
            }
        }
        stage('Verify Coverage Installation') {
            steps {
                // Verify that coverage is installed locally
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip show coverage
                '''
            }
        }
        stage('Run Unit Tests and Generate Coverage') {
            steps {
                // Run the unit tests from test_unit.py and generate a coverage report
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                coverage run --source=. test_unit.py
                coverage xml -o coverage.xml
                '''
            }
        }
        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token') // Accessing the SonarQube token stored in Jenkins credentials
            }
            steps {
                // Perform SonarQube analysis
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=github_trial1 ^
                              -Dsonar.projectName=Trial1 ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.token=%SONAR_TOKEN%
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
