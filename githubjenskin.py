stage('Build') {
    steps {
        sh 'mvn clean package'
    }
}
