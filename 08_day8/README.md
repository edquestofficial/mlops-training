#### create docker image from the dockerfile 
docker build -t image_name .

#### to run the docker container 
docker run -it --name your_container -p 5000:5000 image_name 

#### Step-by-Step Installation of minikube on windows

#### 1. Install Chocolatey (if not already installed)
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

#### Close and reopen PowerShell after installation.
#### 2. Install kubectl and Minikube

choco install kubernetes-cli -y
choco install minikube -y

#### Verify installation:

kubectl version --client
minikube version

#### 3. Start Minikube with Docker driver 
#### Make sure Docker Desktop is running, then:

minikube start --driver=docker

#### Wait for Minikube to pull images and start.

#### Verify Installation

minikube status
kubectl get nodes

#### apply deployment and service.yaml 
kubectl apply -f deployment.yaml 
kubectl apply -f service.yaml

#### Start a minikube tunnel to acces your api

minikube service ice-cream-service

##### Reason to start minikube tunnel
When you deploy a FastApi application on your local Minikube Kubernetes cluster and expose it using a Kubernetes Service (typically of type NodePort or LoadBalancer), you can access it easily using the minikube service command. This command acts as a helper tool that simplifies the process of accessing your service from the host machine, especially on Windows or macOS where the Kubernetes cluster runs inside a virtual machine or Docker container. Internally, minikube service locates the specified

#### Step-by-Step Installation of minikube on MACOS

####  Homebrew installation via Terminal if not installed:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#### 1. Install kubectl and minikube via Homebrew
brew install kubectl
brew install minikube

#### 2. Start Minikube with Docker as driver

minikube start --driver=docker

#### This will Create a Kubernetes cluster, Use Docker to host the cluster nodes

#### Verify Installation

minikube status
kubectl get nodes

#### curl command used localhost IP and random port:
curl -X POST http://12.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"temps\": [47, 20, 7]}"


#### 
kubectl get po -A