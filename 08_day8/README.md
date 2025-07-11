#### create docker image from the dockerfile 
docker build -t image_name .

#### to run the docker container 
docker run -it --name your_container -p 5000:5000 image_name 

#### now add your image name in the deployment.yaml

#### apply deployment and service.yaml 
kubectl apply -f deployment.yaml 
kubectl apply -f service.yaml

##### 
When you deploy a FastApi application on your local Minikube Kubernetes cluster and expose it using a Kubernetes Service (typically of type NodePort or LoadBalancer), you can access it easily using the minikube service command. This command acts as a helper tool that simplifies the process of accessing your service from the host machine, especially on Windows or macOS where the Kubernetes cluster runs inside a virtual machine or Docker container. Internally, minikube service locates the specified


#### 
kubectl get po -A