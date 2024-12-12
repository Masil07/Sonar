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

        stage('Verify Coverage Run Command Execution') {
            steps {
                // Check if coverage run command works and show if there are errors
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Running coverage run command to check execution..."
                coverage run --source=. test_unit.py
                if %ERRORLEVEL% neq 0 (
                    echo "Error: Coverage run command failed!"
                    exit /b %ERRORLEVEL%
                ) else (
                    echo "Coverage run command executed successfully"
                )
                '''
            }
        }

        stage('Ensure Correct Working Directory') {
            steps {
                // Print current working directory to ensure correct context for coverage
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Current working directory: %cd%"
                '''
            }
        }

        stage('Run Unit Tests and Generate Coverage') {
            steps {
                // Run the unit tests from test_unit.py and generate a coverage report
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Running tests with coverage..."
                coverage run --source=. test_unit.py
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
