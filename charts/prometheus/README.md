# Deploy Prometheus
helm upgrade prometheus --install --namespace monitoring stable/prometheus -f values.yaml

# Get service endpoint IP address
servic_ip_addr=`minikube service prometheus -n monitoring --url | egrep -o "([0-9]{1,3}\.){3}[0-9]{1,3}"`


# Add nginx-ingress host for prometheus service in '/etc/hosts' file
echo "$service_ip_addr prometheus.demoproject.info" | sudo tee -a /etc/hosts

# Access prometheus service
http://prometheus.demoproject.info/
