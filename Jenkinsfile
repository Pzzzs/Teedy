// pipeline {
//     agent any

//     stages {
        
//         stage('Build') {
//             steps {
//                 // 使用 Maven 编译项目
//                 sh 'mvn -B -DskipTests clean package -U'
//             }
//         }

//         stage('Test') {
//             steps {
//                 // 运行测试并生成 Surefire 报告
//                 sh 'mvn test'
//             }
//             post {
//                 always {
//                     // 收集 Surefire 报告
//                     junit '**/target/surefire-reports/*.xml'
//                 }
//             }
//         }

//         stage('Generate JavaDoc') {
//             steps {
//                 // 生成 JavaDoc
//                 sh 'mvn clean -DskipTests install'
//                 sh 'mvn javadoc:jar -U'
//             }
//             post {
//                 always {
//                     // 归档生成的 JavaDoc
//                     archiveArtifacts artifacts: '**/target/site/**', fingerprint: true
//                     archiveArtifacts artifacts: '**/target/**/*.jar', fingerprint: true
//                     archiveArtifacts artifacts: '**/target/**/*.war', fingerprint: true

//                 }
//             }
//         }
//     }
// }

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
<<<<<<< HEAD
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
=======
            steps {
                // 使用 Maven 编译项目
                sh 'mvn -B -DskipTests clean package -U'
            }
        }
        stage('Building image') {
            steps {
                // 生成 JavaDoc
                sh 'mvn clean -DskipTests install'
                sh 'docker build -t teedy2024_lab12 .'
            }
        }

        stage('Upload image') {
            steps {
                // 生成 JavaDoc
                sh 'docker tag teedy2024_lab12 pzzzs/teedy_lab12_1:v1.0'
                sh 'docker push pzzzs/teedy_lab12_1:v1.0'
            }
        }

        stage('Run containers') {
            steps {
                // 生成 JavaDoc
                sh 'docker run -d -p 8084:8080 --name teedy_lab12_1_01 teedy2024_lab12'
                sh 'docker run -d -p 8083:8080 --name teedy_lab12_1_02 teedy2024_lab12'
                sh 'docker run -d -p 8082:8080 --name teedy_lab12_1_03 teedy2024_lab12'
>>>>>>> 7a5a3dded0a8bec1f9ec88915928bdc0938cba85
            }
        }
         
    }
}
