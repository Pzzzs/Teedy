pipeline {
    agent any

    environment {
        NODE_ENV = 'production'
    }

    stages {
        

        stage('Navigate to Frontend Directory') {
            steps {
                dir('FrontEnd') {
                    // 全局安装 Vue CLI
                    sh 'npm install -g @vue/cli'

                    // 使用 npm 安装项目依赖
                    sh 'npm install'

                    // 运行构建命令
                    sh 'npm run build'
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                dir('FrontEnd') {
                    // 存档构建产物以供后续步骤使用
                    archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
                }
            }
        }

        
    }

    post {
        always {
            // 清理工作区
            cleanWs()
        }
        success {
            // 构建成功后执行的操作
            echo 'Build succeeded!'
        }
        failure {
            // 构建失败后执行的操作
            echo 'Build failed!'
        }
    }
}
