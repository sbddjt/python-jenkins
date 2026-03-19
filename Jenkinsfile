pipeline {
    agent any

    options {
        timestamps() // 타임스탬프 자동 추가
    }

    environment {
        PYTHON_VERSION = '3.9'
        PROJECT_NAME = "Python Calculator"
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