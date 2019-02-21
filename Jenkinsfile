@Library('jenkins-shared-library')_

node {
    try {
        stage('Clone repository') {
            checkout scm
        }

        stage('Install dependencies') {
            sshagent([env.SSH_KEY_ID]) {
                sh "pip3 install -r requirements.txt --process-dependency-links"
            }
        }

        stage('Test library') {
            sh "python3 unit.py"
        }
    } catch (e) {
        currentBuild.result = "FAILED"
        throw e
    } finally {
        slackNotifier(currentBuild.result)
    }
}
