# Prometheus-ORKUZ-2022L

helm upgrade -i prom ./kube-prometheus-stack -f ./values/prometheus-values.yml -n prom --create-namespace

helm upgrade -i spark ./spark-operator -f ./values/spark-values.yml -n spark --create-namespace

kubectl apply -f ./pi.yml
