from diagrams import Cluster, Diagram
from diagrams.onprem.database import Postgresql
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Nginx
from diagrams.onprem.network import Gunicorn

with Diagram("site", show=False):
    with Cluster("GCP Instances"):
        db = Postgresql("PostgreSQL")
        cache = Redis("Redis Cache")
        with Cluster("Discourse"):
            nginx = Nginx("Webserver")
            gunicorn = Gunicorn("Discourse")
        
    nginx >> gunicorn
    gunicorn >> cache
    gunicorn >> db