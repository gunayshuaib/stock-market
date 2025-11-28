# Stock Market Dashboard

A Python Flask web app showing the last 1 month of stock prices for:

* S&P 500 (^GSPC)
* NASDAQ (^IXIC)
* Top 7 IT companies: Apple, Microsoft, Google, Amazon, Meta, Nvidia, Tesla

Features:

* Interactive charts using Chart.js
* Docker and Docker Compose support
* Kubernetes manifests & Helm chart

---

## Requirements

```
Python 3.11+
Flask
yfinance
Docker (optional)
Kubernetes cluster (optional)
```

---

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open your browser at **[http://localhost:5000](http://localhost:5000)**

---

## Docker

### Build image

```bash
docker build -t stock-dashboard:latest .
```

### Run container

```bash
docker run -p 5000:5000 stock-dashboard:latest
```

### Docker Compose

```bash
docker-compose up --build
```

---

## Kubernetes Deployment

### 1. Apply manifests

Edit `k8s/deployment.yaml` to set correct image, then:

```bash
kubectl apply -f k8s/
```

### 2. Port-forward (if needed)

```bash
kubectl port-forward deployment/stock-dashboard 5000:5000
```

### 3. Image Pull Secrets

If using a private registry:

```yaml
spec:
  containers:
    - name: stock-dashboard
      image: ghcr.io/username/stock-dashboard:latest
  imagePullSecrets:
    - name: ghcr-secret
```

---

## Helm Deployment

```bash
helm upgrade --install stock-dashboard charts/stock-dashboard \
  --set image.repository=ghcr.io/username/stock-dashboard \
  --set image.tag=latest
```

---

## Cleanup

```bash
helm uninstall stock-dashboard
kubectl delete -f k8s/
```

---

## Notes

* Replace `ghcr.io/username/stock-dashboard` with your actual Docker Hub or GHCR path.
* Minikube users: `minikube service stock-dashboard --url` to get service URL.
