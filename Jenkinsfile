pipeline {
    agent any
    
    stages {
        stage('GitHub Clone') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/sbddjt/python-jenkins.git'
            }
        }
        
        stage('Setup & Test') {
            steps {
                sh '''
                    echo "========================================="
                    echo "🐍 Python Pipeline CI Started"
                    echo "Build Number: ${BUILD_NUMBER}"
                    echo "========================================="
                    
                    # 가상환경 생성 및 활성화
                    echo ""
                    echo "▶ 가상환경 세팅"
                    python3 -m venv venv
                    . venv/bin/activate
                    
                    # 패키지 설치
                    echo ""
                    echo "▶ 의존성 패키지 설치"
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    # 테스트 실행
                    echo ""
                    echo "▶ 단위 테스트 실행 🧪"
                    pytest tests/ -v --tb=short
                    
                    # 결과 판별
                    if [ $? -eq 0 ]; then
                        echo ""
                        echo "✅ All tests passed!"
                    else
                        echo ""
                        echo "❌ Tests failed!"
                        exit 1
                    fi
                '''
            }
        }
    }
    
    post {
        always {
            echo '파이프라인 실행 완료'
        }
        success {
            echo '✅ 테스트 성공! 배포 준비 완료'
        }
        failure {
            echo '❌ 빌드 또는 테스트 실패'
        }
    }
}