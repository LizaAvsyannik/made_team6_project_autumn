from locust import HttpUser, task, between


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_get_author_info(self):
        author_id = "53f42f36dabfaedce54dcd0c"
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json"}
        self.client.get(f"/author/{author_id}", headers=headers)

    @task(2)
    def test_get_article_info(self):
        article_id = "53e99784b7602d9701f3f68f"
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json"}
        self.client.get(f"/article/{article_id}", headers=headers)
