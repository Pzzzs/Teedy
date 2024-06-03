pipeline {
    agent any

    environment {
        NODE_ENV = 'production'
    }

    stages {
        
        stage('FrontEnd Dependencies') {
            steps {
                dir('FrontEnd') {
                    sh 'npm install -g @vue/cli'
                    

                }
            }
        }

        stage('Build FrontEnd') {
            steps {
                dir('FrontEnd') {

                    sh 'npm install'
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                dir('FrontEnd') {

                    sh 'npm install'
                }
            }
        }

        stage('BackEnd Dependencies') {
            steps {
                dir('BackEnd') {

                    sh 'pip install --no-cache-dir -r requirements.txt'
                }
            }
        }

        stage('Build Docker') {
            steps {
                dir('FrontEnd') {

                    sh 'npm install'
                }
            }
        } 
    }
}

