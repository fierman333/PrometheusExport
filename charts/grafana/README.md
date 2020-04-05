# Deploy Grafana
```
helm upgrade grafana --install --namespace monitoring stable/grafana -f values.yaml
```

# Access grafana service for minikube
## Get service endpoint IP address
```
servic_ip_addr=`minikube service grafana -n monitoring --url | egrep -o "([0-9]{1,3}\.){3}[0-9]{1,3}"`
```

## Add nginx-ingress host for grafana service in '/etc/hosts' file
```
echo "$service_ip_addr grafana.demoproject.info" | sudo tee -a /etc/hosts
```

## Access grafana service
```
http://grafana.demoproject.info/
```
