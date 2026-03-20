pipeline {
    agent any

    options {
        timestamps() // 타임스탬프 자동 추가
    }

    environment {
        PYTHON_VERSION = '3.9'
        PROJECT_NAME = "Python Calculator"
        DOCKER_IMAGE = 'sbddjt/python-calculator'
        DOCKER_CREDENTIALS = credentials('dockerhub-token')
    }
    
    stages {
        stage('GitHub Clone') {
            steps {
                echo "========================================="
                echo "Project: ${PROJECT_NAME}"
                echo "Python Version: ${PYTHON_VERSION}"
                echo "Build Number: ${BUILD_NUMBER}"
                echo "========================================="

                git branch: 'main', 
                    url: 'https://github.com/sbddjt/python-jenkins.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                    echo "▶ 가상환경 세팅"
                    python3 -m venv venv
                    . venv/bin/activate
                    
                    echo "▶ 의존성 패키지 설치"
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    echo "▶ 단위 테스트 실행 🧪"
                    . venv/bin/activate
                    pytest tests/ -v --tb=short
                '''
            }
        }
        
        stage('Code Quality Check') {
            steps {
                sh '''
                    echo "▶ 코드 품질 검사"
                    . venv/bin/activate
                    # pylint나 flake8 등 추가 가능
                    echo "✅ Code quality check passed"
                '''
            }
        }

        stage('Docker Image Build') {
            steps {
                sh '''
                    echo "▶ Docker 이미지 빌드 🐳"
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                    docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                    echo "✅ Docker 이미지 빌드 완료"
                '''
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                    echo "▶ Docker Hub 로그인"
                    echo ${DOCKERHUB_CREDENTIALS} | docker login -u sbddjt --password-stdin
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                    echo "▶ Docker Hub에 이미지 Push 🚀"
                    docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    docker push ${DOCKER_IMAGE}:latest
                    echo "✅ Docker Hub Push 완료"
                '''
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(credentials: ['deploy-server-ssh']) {
                    sh '''
                        echo "▶ 원격 서버에 배포 🚀"
                
                        # 배포 스크립트를 서버에 복사
                        scp -o StrictHostKeyChecking=no -P 2222 \
                            deploy.sh seongyun@192.168.56.1:/tmp/
                
                        # 서버에서 배포 스크립트 실행
                        ssh -o StrictHostKeyChecking=no -p 2222 \
                            seongyun@192.168.56.1 \
                            "bash /tmp/deploy.sh ${BUILD_NUMBER}"
                
                        echo "✅ 배포 완료!"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo '========================================='
            echo '파이프라인 실행 완료'
            echo '========================================='
        }
        success {
            echo '✅ 모든 테스트 통과! 배포 준비 완료'
        }
        failure {
            echo '❌ 빌드 또는 테스트 실패'
        }
    }
}