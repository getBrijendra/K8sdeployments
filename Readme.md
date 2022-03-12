docker build -t demoapp-flask .
kubectl apply -f .\deployment.yaml
kubectl get all -n cache