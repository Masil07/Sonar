pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    echo 'Checked out code from the repository.'
                    echo "Current build result after checkout: ${currentBuild.result}"
                }
            }
        }
        stage('Build') {
            steps {
                // Set the PATH and install dependencies using pip
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                '''
                script {
                    echo 'Build stage completed.'
                    echo "Current build result after build: ${currentBuild.result}"
                }
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
                script {
                    echo 'SonarQube analysis stage completed.'
                    echo "Current build result after SonarQube analysis: ${currentBuild.result}"
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo "Waiting for SonarQube quality gate to complete..."
                    }
                    def qualityGateResult = waitForQualityGate()
                    if (qualityGateResult.status == 'FAILED') {
                        currentBuild.result = 'FAILURE'
                        echo 'Quality gate failed. Pipeline will stop here.'
                        error('Quality gate failed.')
                    } else {
                        echo 'Quality gate passed.'
                    }
                }
                script {
                    echo 'Quality gate check completed.'
                    echo "Current build result after quality gate: ${currentBuild.result}"
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
            script {
                echo "Final build result: ${currentBuild.result}"
            }
        }
        failure {
            echo 'Pipeline failed'
            script {
                echo "Final build result: ${currentBuild.result}"
            }
        }
        always {
            echo 'This runs regardless of the result.'
            script {
                echo "Pipeline result at the end: ${currentBuild.result}"
            }
        }
    }
}
