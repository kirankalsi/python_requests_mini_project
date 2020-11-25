pipeline{
        agent any
        stages{
            stage('Build Images'){
                steps{
                    sh "docker build -t python_requests_mini_project/service1 ."
                    sh "docker build -t python_requests_mini_project/service2 ."
                }
            }
            stage('Deploy'){
                steps{
                    sh "docker stack deploy --compose-file docker-compose.yaml my-stack"
                }
            }
        }
}