#!groovy

node('node') {

    currentBuild.result = "SUCCESS"

    try {

        stage('Checkout'){
            checkout scm
        }

        stage('Test'){
            sh 'pip install -r foobar/test-requirements.txt'
            sh 'cd foobar && python hello_tests.py'
        }

        stage('Build and tag'){
            echo 'docker build -t production:latest .'
        }

    }
    catch (err) {
        currentBuild.result = "FAILURE"
            mail body: "project build error is here: ${env.BUILD_URL}" ,
            from: 'jenkins@example.com',
            replyTo: 'noreply@example.com',
            subject: 'project build failed',
            to: 'devs@example.com'
        throw err
    }
}
