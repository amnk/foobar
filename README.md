This repository contains an example app, that shows
big power of containers and all current ecosystem of Kubernetes.

It contains:

* application itself:
  * [flask](http://flask.pocoo.org/) app with a simple `/hello` endpoint;
  * [uwsgi](https://github.com/unbit/uwsgi) uwsgi to serve Python app;
* [Helm](https://github.com/kubernetes/helm) chart;
* [Jenkinsfile](https://jenkins.io/doc/book/pipeline/jenkinsfile/) for integration
  with Jenkins;
* `foobar.groovy` which defines sample job in [JobDSL](https://github.com/jenkinsci/job-dsl-plugin);

This Helm Chart implies two flows:

* usual one, when you deploy app to remote k8s cluster and follow all usual
  guidlines;

* local development one. After doing certain steps:

  `minikube mount foobar/:/src`
  `helm install --name hello --set development=true ./helm-chart/`

  app will be deployed with `foobar/` mounted inside container, so all changed
  done to Python code will cause hot reload.

In all cases, after deployment one can get name of the pod using

`kubectl get pods`

and then do port-forward:

`kubectl port-forward $POD_NAME 8080:8080`

Afterwards `curl localhost:8080/hello` should display some awesome hello :)

# Prometheus monitoring
Prometheus chart is not included in this repo, but app has all needed annotations. Just run
`helm install stable/prometheus`, let pods start and configure port forwarding:

* `export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")`
* `kubectl --namespace default port-forward $POD_NAME 9090`

Now, by navigating to [Prometheus Targets](http://localhost:9090/targets) you should be able to see
[kubernetes pods](http://localhost:9090/targets#job-kubernetes-pods) scraped, and `hello` app there. If you go back to
*Graph* section, and put `requests_for_host` into *Expression* - you should be able to see the graph from `hello` app.
