# Set git short tag version for deploy.
appVersion="ae72090"

# Deploy 'prometheus-export' service
helm upgrade prometheus-export --install --namespace default --set-string image.tag=${appVersion} .
