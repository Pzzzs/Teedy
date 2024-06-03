pipeline {
    agent any

    stages {

        stage('init') {
            echo 'Build'
        }

            dir('FrontEnd') {
                steps {
                    // 全局安装 Vue CLI
                    sh 'npm install -g @vue/cli'
                }
            }
        }
        stage('Install Vue CLI') {
            dir('FrontEnd') {
                steps {
                    // 全局安装 Vue CLI
                    sh 'npm install -g @vue/cli'
                }
            }
        }

        stage('Install Dependencies') {
            dir('FrontEnd') {
                steps {
                    // 使用npm安装项目依赖
                    sh 'npm install'
                }
            }
        }

        stage('Build') {
            dir('FrontEnd') {
                steps {
                    // 运行构建命令
                    sh 'npm run build'
                }
            }
        }

        stage('Archive Artifacts') {
            dir('FrontEnd') {
                steps {
                    // 存档构建产物以供后续步骤使用
                    archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
                }
            }
        }
         
    }
}
