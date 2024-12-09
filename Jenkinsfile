pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Masil07/Sonar.git'
            }
        }
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat '''
                    sonar-scanner -Dsonar.projectKey=github_trial1
                                  -Dsonar.projectName=Trial1
                                  -Dsonar.sources=.
                                  -Dsonar.host.url=http://localhost:9000
                                  -Dsonar.token=your-sonar-token
                    '''
                }
            }
        }
        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
    }
}
