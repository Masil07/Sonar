pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pull code from your GitHub repository
                git branch: 'main', url: 'https://github.com/Masil07/Sonar.git'
            }
        }
        stage('Build') {
            steps {
                // Use Maven to build your project
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') { 
                    // Run SonarQube analysis
                    sh 'mvn sonar:sonar'
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
