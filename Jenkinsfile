pipeline {
    agent any

    environment {
        NODE_ENV = 'production'
    }

    stages {
        
        // stage('Install Dependencies') {
        //     steps {
        //         dir('FrontEnd') {

        //             // 全局安装 Vue CLI
        //             sh 'npm install -g @vue/cli'

        //             // 使用 npm 安装项目依赖
        //             sh 'npm install'

        //         }
        //     }
        // }

        // stage('Build') {
        //     steps {
        //         dir('FrontEnd') {

        //             // 运行构建命令
        //             sh 'npm run build'
        //         }
        //     }
        // }

        // stage('Archive Artifacts') {
        //     steps {
        //         dir('FrontEnd') {
        //             // 存档构建产物以供后续步骤使用
        //             archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
        //         }
        //     }
        // }

        stage('Archive Artifacts') {
            steps {
                dir('BackEnd') {
                    // 存档构建产物以供后续步骤使用
                    sh 'pip install --no-cache-dir -r requirements.txt'
                }
            }
        }

        
    }

    
}
