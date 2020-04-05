# Add 'kir4h' helm repository
helm repo add kir4h https://kir4h.github.io/charts/

# Deploy registry-creds with AWS ECR support
helm upgrade --install registry-creds -f values.yaml kir4h/registry-creds
