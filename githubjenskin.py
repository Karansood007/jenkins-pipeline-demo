pipeline {
    agent any
    
    environment {
        GIT_REPO = 'https://github.com/Karansood007/jenkins-pipeline-demo.git'
        EMAIL_RECIPIENT = 'karansood107@gmail.com'
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the code...'
                bat 'mvn clean package' // Replace with the actual build command for Windows
            }
        }
        
        stage('Unit and Integration Tests') {
            steps {
                echo 'Running Unit and Integration Tests...'
                bat 'mvn test' // Replace with actual test command for Windows
            }
        }
        
        stage('Code Analysis') {
            steps {
                echo 'Running Code Analysis...'
                bat 'sonar-scanner' // Replace with actual SonarQube command for Windows
            }
        }
        
        stage('Security Scan') {
            steps {
                echo 'Performing Security Scan...'
                bat 'dependency-check --project myapp --scan C:\\path\\to\\your\\code' // Replace with actual security scan command for Windows
            }
        }
        
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to Staging...'
                bat 'aws deploy ...' // Replace with actual deployment command for Windows
            }
        }
        
        stage('Integration Tests on Staging') {
            steps {
                echo 'Running Integration Tests on Staging...'
                bat 'run integration tests' // Replace with actual integration test command for Windows
            }
        }
        
        stage('Deploy to Production') {
            steps {
                echo 'Deploying to Production...'
                bat 'aws deploy ...' // Replace with actual production deployment command for Windows
            }
        }
    }
    
    post {
        success {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Build Success - ${env.JOB_NAME}",
                 body: "The build for ${GIT_REPO} succeeded. Check Jenkins for details."
        }
        failure {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Build Failed - ${env.JOB_NAME}",
                 body: "The build for ${GIT_REPO} failed. Check Jenkins for details."
        }
    }
}
