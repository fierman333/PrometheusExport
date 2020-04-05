# Set git short tag version for deploy.
```
appVersion=`git rev-parse --short HEAD`
```

# Deploy 'prometheus-export' service
```
helm upgrade prometheus-export --install --namespace default --set-string image.tag=${appVersion} .
```
