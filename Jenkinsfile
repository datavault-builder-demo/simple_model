pipeline {
  agent any
  environment {
    DOCKER_PROJECT = 'datavaultbuilder'
  }
  options {
    disableConcurrentBuilds()
    timestamps()
  }
  stages {
    stage('Deploy to integrated Test') { // for display purposes
      steps {
        dir('cicdscripts') {
         echo "Branch: ${env.BRANCH_NAME}"
         sh "echo Hallo Bash"
         sh "pwd"
         sh "python3 deploy2dev.py -b ${env.BRANCH_NAME}"
        }
     
      }
    }
  }
}
