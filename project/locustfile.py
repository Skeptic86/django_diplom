from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_posts(self):
        self.client.get("/posts/")

    @task
    def create_post(self):
        self.client.get("/posts/create")
