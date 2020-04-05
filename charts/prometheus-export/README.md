# Deploy 'prometheus-export' service
helm upgrade prometheus-export --install --namespace default --set-string image.tag=latest .
