# list-custom-resource-defination
we can use the client module to interact with the kubernetes resources. 

But In Python, we instantiate ApiextensionsV1Api class from client module:

`client_api = client.ApiextensionsV1Api()`         

Here I've created the client with it's respective class ApiextensionsV1Api
and storing in a var named as client_api. so furture we can use it.

`KubeConfig:` to pass the on local cluster e.g minikube we use bellowcommand: 

`config. load_kube_config()`

#### Authenticating to the Kubernetes API server

But what if you want to list all the custom resource defination of a GKE or any other  Cluster, you must need to authenticate the configuration

`configuration.api_key = {"authorization": "Bearer" + bearer_token}` 

I've used Bearer Token which enable requests to authenticate using an access key.

#### get the list of the custom resource defination:

call the function get_crd(cluster_details)

And run following command:

`python3 crd.py`
