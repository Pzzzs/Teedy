pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'mvn -B clean package'
      }
    }
    stage('Test') {
      steps {
        sh 'mvn test'
      }
      post {
        always {
          // Generate Surefire report and archive as artifact
          step([$class: 'JUnitResultArchiver', testResults: 'target/surefire-reports/**/*.xml'])
        }
      }
    }
    stage('pmd') {
      steps {
        sh 'mvn pmd:pmd'
      }
      post {
        always {
          // Archive PMD reports as artifact
          archiveArtifacts artifacts: 'target/site/pmd/index.html', fingerprint: true
          archiveArtifacts artifacts: 'target/site/pmd/cpd.html', fingerprint: true
        }
      }
    }
  }
  post {
    always {
      // Archive other artifacts
      archiveArtifacts artifacts: '**/target/**/*.jar', fingerprint: true
      archiveArtifacts artifacts: '**/target/**/*.war', fingerprint: true
      // Generate Javadoc and archive as artifact
      sh 'mvn javadoc:jar'
      archiveArtifacts artifacts: 'target/site/apidocs/**/*.jar', fingerprint: true
    }
  }
}
