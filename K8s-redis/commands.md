kubectl create ns cache
kubectl apply -f .\redis-conf.yaml
kubectl apply -f redis-pod.yaml
kubectl get all -n cache
kubectl get cm -n cache
kubectl exec --stdin --tty shell-demo -- /bin/bash
kubectl exec --stdin --tty shell-demo -- /bin/sh
kubectl exec -i -t redis-cache -- nslookup kubernetes.default

kubectl exec -i -t redis-cache -- nslookup redis-cache.cache