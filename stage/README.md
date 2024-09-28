# Momentum Deployment and Pipeline for Staging:

## Overview

This project includes various Kubernetes microservices, along with their deployment configurations, service definitions, and Jenkins pipelines for automation. The following services are represented:

- knowledge-graph
- momentum-core
- momentum-server
- momentum as micro-services:
   - celery
   - mom-api
   - conversation-api (mom-api)

- neo4j-helm
- PgBouncer
- Ingress Controller

## Getting Started

### Prerequisites

To run this project, you need:
- A Kubernetes cluster (e.g., Minikube, GKE, EKS, AKS).
- Kubectl installed and configured to communicate with your cluster.
- Jenkins configured for CI/CD with the necessary plugins for Kubernetes.

### Deploying Services

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Deploy each service by applying the relevant Kubernetes YAML files, such as: :
   ```bash
   kubectl apply -f app/knowledge-graph/knowledge-graph.yaml
   kubectl apply -f app/momentum-core/momentum-core-deployment.yaml

3. Start Jenkins and which is already configure the Jenkins pipeline which access on .
- `knowledge-graph_GKE_deployment_pipeline  < app/knowledge-graph/Jenkinsfile >`
- `momentum-core_GKE_deployment_pipeline  < app/momentum-core/Jenkinsfile >`
- `Neo4j_GKE_deployment_pipeline < Neo4j/Jenkinsfile >`
- `Pgbouncer_GKE_deployment_pipeline < aPgbouncer/Jenkinsfile >`
- `Deployment_HPA_pipeline < ./HPAJenkinsfile >`
- `Deployment_rollback_pipeline <./JenkinsfileRollBack>`

