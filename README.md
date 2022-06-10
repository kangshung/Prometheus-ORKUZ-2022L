# Prometheus jako narzędzie monitorowania systemów rozproszonych

## ORKUZ 2022L

---

### Damian Fiłonowicz

### Igor Pieniek

### Aleksandra Straus

---

Prerequisites:

- az cli - uwierzytelnione na swoją chmurę
- dockerd - do zbudowania obrazu
- kubectl cli / https://k8slens.dev/ - do komunikacji z klastrem
- helm cli - do odpalenia chartów

Komendy na odpalanie:

Klaster AKS

```
cd .\terraform\
terraform init
terraform apply
cd ..
```

Prometheus + Kube Metrics + Grafana

```
helm upgrade -i prom ./kube-prometheus-stack -f ./values/prometheus-values.yml -n prom --create-namespace
```

Spark-on-k8s-operator

```
helm upgrade -i spark ./spark-operator -f ./values/spark-values.yml -n spark --create-namespace
```

Sparkowa aplikacja strumieniowa

```
kubectl apply -f .\streaming\streaming-demo-application.yaml
```

ServiceMonitor aplikacji sparkowej

```
kubectl apply -f .\streaming\streaming-servicemonitor.yml   
```

Foldery:

- kube-prometheus-stack - Helm chart
- spark-operator - Helm chart
- streaming - wszystko związane z aplikacją Sparkową
- terraform - wszystko związane z infrastrukturą
- values - konfiguracja Helm chartów
