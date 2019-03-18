@Library('jenkins-shared-library')_

node {
    try {
        stage('Clone repository') {
            checkout scm
        }

        stage('Install dependencies') {
            sshagent([env.SSH_KEY_ID]) {
                sh "poetry install"
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
