#!/usr/bin/env python3

import random
from datetime import datetime, timedelta

outfile = "/var/log/weblogs/access.log"

ips = ["8.8.8.8","1.1.1.1","13.107.42.14","45.33.32.156",
       "172.217.169.14","151.101.1.69","104.18.32.47"]

pages = ["/","/products","/login","/cart","/checkout","/purchase","/support"]
methods = ["GET","POST"]
statuses = [200,200,200,200,200,301,302,400,401,403,404,500,503]

agents = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/137.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) Firefox/138.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)",
"Mozilla/5.0 (Linux; Android 14)"
]

refs = ["https://google.com","https://bing.com",
        "https://shop.com","https://shop.com/cart","-"]

start = datetime.now() - timedelta(days=7)

with open(outfile,"w") as f:
    for i in range(10000):
        timestamp = start + timedelta(seconds=i*20)
        ip = random.choice(ips)
        page = random.choice(pages)
        method = random.choice(methods)
        status = random.choice(statuses)
        size = random.randint(100,12000)
        ref = random.choice(refs)
        agent = random.choice(agents)

        log_entry = (
            f'{ip} - - '
            f'[{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")}] '
            f'"{method} {page} HTTP/1.1" '
            f'{status} {size} '
            f'"{ref}" '
            f'"{agent}"\n'
        )
        f.write(log_entry)

print("Generated 10,000 web log events successfully!")
