from diagrams import Cluster, Diagram
from diagrams.onprem.database import Postgresql
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Nginx
from diagrams.onprem.network import Gunicorn
from diagrams.onprem.dns import Coredns
from diagrams.gcp.network import DNS

with Diagram("site", show=False):
    dns = DNS("Cloudflare DNS")
    with Cluster("GCP Instances"):
        db = Postgresql("PostgreSQL")
        cache = Redis("Redis Cache")
        with Cluster("Discourse"):
            nginx = Nginx("Webserver")
            gunicorn = Gunicorn("Discourse")
    
    dns >> nginx
    nginx >> gunicorn
    gunicorn >> cache
    gunicorn >> db