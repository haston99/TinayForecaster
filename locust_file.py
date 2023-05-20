from locust import HttpUser,task,between 

class AppUser(HttpUser):
    wait_time = between(2,5)

    #Endpoint
    #The @task decorator is essential in informing locust on which route/endpoint to perform load testing on.
    # In our case we will use the main route ‘/’(which is the app Homepage).

    @task
    
    #def home_page(self):
    #    self.client.get("/")
    def test_forecaster(self):
        self.client.get("/pages/TF_Data-Forecaster")
        self.client.post()