from kubernetes import client, utils 

import kubernetes.client
from kubernetes.client import ApiClient

from kubernetes.client.rest import ApiException
from kubernetes import client, config

def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = kubernetes.client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
            api_instance1 = kubernetes.client.ApiextensionsV1Api(api_client)
        return api_instance1

    except ApiException as e:
        print("Error getting kubernetes client:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))
        return None

def __format_data_for_cluster(client_output):
        temp_dict={}
        temp_list=[]
        
        json_data=ApiClient().sanitize_for_serialization(client_output)
        if len(json_data["items"]) != 0:
            for ls in json_data["items"]:
                temp_dict={
                    "name": ls["metadata"]["name"],  
                    "labels":ls["metadata"]["labels"]
                }
                temp_list.append(temp_dict)
        return temp_list

def get_crd(cluster_details):
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
        )
     
        crd =client_api.list_custom_resource_definition()
        data=__format_data_for_cluster(crd)
        print("get the list of custom resource defination: {}".format(data))
      
 
if __name__ == '__main__':
    cluster_details={
        "bearer_token":"GKE-Bearer-Token",
        "api_server_endpoint":"Ip-k8s-control-plane"
    }
    get_crd(cluster_details)