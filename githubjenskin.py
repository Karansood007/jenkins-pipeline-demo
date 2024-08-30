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
                sh 'mvn clean package' // Replace with the actual build command
            }
        }
        
        stage('Unit and Integration Tests') {
            steps {
                echo 'Running Unit and Integration Tests...'
                sh 'mvn test' // Replace with actual test command
            }
        }
        
        stage('Code Analysis') {
            steps {
                echo 'Running Code Analysis...'
                sh 'sonar-scanner' // Replace with actual SonarQube command
            }
        }
        
        stage('Security Scan') {
            steps {
                echo 'Performing Security Scan...'
                sh 'dependency-check --project myapp --scan /path/to/your/code' // Replace with actual security scan command
            }
        }
        
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to Staging...'
                sh 'aws deploy ...' // Replace with actual deployment command
            }
        }
        
        stage('Integration Tests on Staging') {
            steps {
                echo 'Running Integration Tests on Staging...'
                sh 'run integration tests' // Replace with actual integration test command
            }
        }
        
        stage('Deploy to Production') {
            steps {
                echo 'Deploying to Production...'
                sh 'aws deploy ...' // Replace with actual production deployment command
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
