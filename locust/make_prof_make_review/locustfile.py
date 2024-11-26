from locust import task, run_single_user
from locust import FastHttpUser


class make_prof_make_review(FastHttpUser):
    host = "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "a99313d2-9bbd-4c54-825e-598a1054c28c",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "157",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "q7EQo6sHGAqUHDCE-QzGlXn23ZwC4xSwWiZ70W4jfEbexzEpdFEmIImubvAxjJl58el1sjRwSVJLoN2DyMA8ZA",
                "x-turbo-request-id": "8abd98a0-6e4b-4090-9a0d-4667ce023374",
            },
            data="authenticity_token=ihQe3Q_toeWmpoQT9o_t4EeWVe41yIPdavjfuw_Aq65GCfOyiIcwk5MJIvKiwvY14dM6Ackcl3nk2SQnoL9pfQ&username=cataquack&password=cataquack&commit=Log+In",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/students/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "edbe3953-008a-4365-8e01-6d95bb2961e8",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/students/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"925866a9b28801aa7efc7d42d134f331"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/students/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "75bac68d-8ad2-46dc-99e9-2a87a23b078c",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/students",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "185",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/students/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "WYXZsJhT5F0KLN16JX8xY9aGHWBw5q4N07TYHpnqBLks8_g6RwXadxeegw7t_26PXpm1TkZ18-_CMn5MPwlEmw",
                "x-turbo-request-id": "eda55cc2-ceb5-4ae1-b51c-517253b86412",
            },
            data="authenticity_token=zPNMjnM3l9IJDxWBLiQMNlXhlKR4F63bi-xTy95SfrWQe9-CtCkel--IcrD8MIlviJmbAGti7mCataNEcYcLwQ&student%5Busername%5D=cataquack&student%5Bpassword%5D=cataquack&commit=Register",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"3a12e101ffdf678d5905481f588b0c29"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/students/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "WYXZsJhT5F0KLN16JX8xY9aGHWBw5q4N07TYHpnqBLks8_g6RwXadxeegw7t_26PXpm1TkZ18-_CMn5MPwlEmw",
                "x-turbo-request-id": "eda55cc2-ceb5-4ae1-b51c-517253b86412",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/students/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"c66e69314cbd5a64005f35bc9d1b4a2c"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "6a197848-e16a-48a6-9935-3011a4161052",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "bc1adb59-3001-4e89-b909-8d8a0c146b9d",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "157",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "9Gfn7wfezbZR3JkwzUoo5Q5-DdAv3NlfueL15TEUuhaBEcZl2IjznExux0QFyncJhmGl_hlPhL2oZFO3l_f6NA",
                "x-turbo-request-id": "29168adb-1731-47c1-b6ac-203c25407314",
            },
            data="authenticity_token=EfNzhTLtJ1qlGM6kmnVd6SX-MQn6-W58TnsGNwZKIbHd7p7qtYe2LJC3aEXOOEY8g7te5gYtetjAWv2rqTXjYg&username=cataquack&password=cataquack&commit=Log+In",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"a032e826a47689e818a5e018a7ec79a3"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "9Gfn7wfezbZR3JkwzUoo5Q5-DdAv3NlfueL15TEUuhaBEcZl2IjznExux0QFyncJhmGl_hlPhL2oZFO3l_f6NA",
                "x-turbo-request-id": "29168adb-1731-47c1-b6ac-203c25407314",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/logout",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "120",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "RyKUh8-C4XzSKIk4jjCEDQgnED0K8VziDmb1ZlbkBvgyVLUNENTfVs-a10xGsNvhgDi4EzxiAQAf4FM08AdG2g",
                "x-turbo-request-id": "c1037d8e-aa56-471a-a1b0-1940919d939e",
            },
            data="_method=delete&authenticity_token=coQToj38YtY9FGIIkswduJ2HNPJ-D5XS2-bTEXRDH4aqIVSEB6rUipNYr4fav21HzsBMIK-BMMdDDs5HlVvXhw",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "RyKUh8-C4XzSKIk4jjCEDQgnED0K8VziDmb1ZlbkBvgyVLUNENTfVs-a10xGsNvhgDi4EzxiAQAf4FM08AdG2g",
                "x-turbo-request-id": "c1037d8e-aa56-471a-a1b0-1940919d939e",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"09a8c70ed94872a4c904b25135586d74"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "98bb9ae4-ad84-403b-b907-3ae63a9ca650",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "2b5c1117-39ce-475d-9e9a-dd314d7625d7",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "222",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "Ll0xxMQErpG2d2mKgAJwvrcLHZtSE7IbTrvgtPavJtxbKxBOG1KQu6vFN_5Igi9SPxS1tWSA7_lfPUbmUExm_g",
                "x-turbo-request-id": "61d10c38-ecdb-41b1-a66b-d288730950a0",
            },
            data="authenticity_token=4hSNv7IcAUG-grETNgiTvqGQjsbdwFS4ayD_AuFGWvp6bdi4ljgKLbZ5a1ED0DpDbrC5Gm5mZURh_Wa5MEq5Jg&professor%5Bname%5D=Vinayak+Gajjewar%2C+Ph.D.&professor%5Bdepartment%5D=Culinary+Scientology&commit=Create+Professor",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "Ll0xxMQErpG2d2mKgAJwvrcLHZtSE7IbTrvgtPavJtxbKxBOG1KQu6vFN_5Igi9SPxS1tWSA7_lfPUbmUExm_g",
                "x-turbo-request-id": "61d10c38-ecdb-41b1-a66b-d288730950a0",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"a18ceaf56e3a2f57d1e938849efee19e"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "c22a19ce-8873-4674-9975-e333a2bd1153",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "76c4c2d9-d53d-4884-bbb4-07bbaec9e746",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1/reviews/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "830abadd-0760-4d3b-bbdd-6a380c6231e8",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"d4d6e228c5c0ab6e6ef8816480c0c644"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "830abadd-0760-4d3b-bbdd-6a380c6231e8",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"3ae06b7f69f244411541bcf5123ccac6"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "989e5210-9a2e-4c38-8b65-8cbcb55e53cc",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"daf16510478a21a67f013a7237a8fd01"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "b2d566a1-cc5e-487e-ae9d-03757e769406",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1/reviews/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "d9e43b59-2148-4a88-8932-ccc4a072b2ba",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"fbce06299926072e80cb514dd7370bd2"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "d9e43b59-2148-4a88-8932-ccc4a072b2ba",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"3250fcd10afd7b2410c48b84dac03219"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "1d10e19e-599b-4e66-8d13-d63775c1325c",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1/reviews/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "990311e3-d976-4b48-9e00-2ec059449044",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"d5cc259769a9ad134cb1b1844e33ce6b"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "990311e3-d976-4b48-9e00-2ec059449044",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "157",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "01MBnFfZud-f6XmFSq_zgasTJWCtvn-AQGW_W1eUKMamJSAWiI-H9YJbJ_GCL6xtIwyNTpstImJR4xkJ8Xdo5A",
                "x-turbo-request-id": "a6010d98-0a93-44ea-b3a1-4a0dc71c4a22",
            },
            data="authenticity_token=qaNRxRLlYBG0WaZJ39XoCamTCIcZk7BKj8MjjHALlfVlvryqlY_xZ4H2AKiLmPPcD9ZnaOVHpO4B4tgQ33RXJg&username=cataquack&password=cataquack&commit=Log+In",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"c106084bcfaec71a26a08cd122ffd8d8"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "01MBnFfZud-f6XmFSq_zgasTJWCtvn-AQGW_W1eUKMamJSAWiI-H9YJbJ_GCL6xtIwyNTpstImJR4xkJ8Xdo5A",
                "x-turbo-request-id": "a6010d98-0a93-44ea-b3a1-4a0dc71c4a22",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"fbd5a80c54322d614895e4f6bf25afbd"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "89e73e19-8c4b-4508-9688-6cadbd0778a2",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"9e4ad4c551b8b4608aeae5e1685db542"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "8e63a7d1-d8e1-48b3-b45b-2de712a2a731",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1/reviews/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "97486994-c927-4964-839a-02240ae50e8e",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/courses/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "2c0ae7e3-0a35-470d-b244-e0d380b2e9d7",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/courses",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "213",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "Q3_r8u-Ocsijqk5ab60kDiuPgGrRRN8Y0zxNDNsqU9Q2Ccp4MNhM4r4YEC6nLXvio5AoROfXgvrCuutefckT9g",
                "x-turbo-request-id": "2595e253-b601-4c23-b433-4c084032d6b1",
            },
            data="authenticity_token=p9Bjr9aJQEHgqIE7A2V_biAHVQ3416hYZ_IGm0nzGDghAdWVOmU2nM_aNHFhqqRJA7DLrOvbV1Bim2nZTW0nag&course%5Bname%5D=Fishing+101&course%5Bcode%5D=fish101&course%5Bdescription%5D=Fishing.&commit=Create+Course",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/courses",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "Q3_r8u-Ocsijqk5ab60kDiuPgGrRRN8Y0zxNDNsqU9Q2Ccp4MNhM4r4YEC6nLXvio5AoROfXgvrCuutefckT9g",
                "x-turbo-request-id": "2595e253-b601-4c23-b433-4c084032d6b1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/courses/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"b2906cad7e77a008b5089563f4dd76bd"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "4d972065-7ad0-4932-857a-6649b9b5a049",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"27cac2734fda7015e46d56e6cb0de631"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "16b527d8-2323-4520-9a00-6da4e0283e2c",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"d69a18416de7109a73212d6ba86eb6fa"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "4c703b15-2aed-4a2d-82d3-2e40eb7e405a",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"b9f949a8f905f386eac3b7b0879330cd"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "11c80ac4-346e-47cc-a49b-08a71bec1ee2",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1/reviews/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"f5c27d6e26c1d417c6f57f4334e8fc00"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "653069a0-d167-44bc-bba5-b0e920883773",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/courses/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"e3f095d8220ae575d6dd055ad9f0e64c"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "0471194d-5090-4b93-830e-b7938717a80e",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/courses/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"5433a40233d67bc7da94a0679878423f"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "e489cc38-9e37-401d-9471-754268bc13ae",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/professors/1/reviews",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "225",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "TxecMmeVFY42litJorg5puV4lvrxl9zoj2B0hPyI8fU6Yb24uMMrpCskdT1qOGZKbWc-1McEgQqe5tLWWmux1w",
                "x-turbo-request-id": "88ec22cd-5a95-46e6-9e52-c866adba87bc",
            },
            data="authenticity_token=I484Mb-JoN6htxJI4pkN8PbQfiLqTZ9lf5Y965Rt0gcLFsfhJX7GVa-lXSmuWRs9Lbv_Hqi35I1HfZwsdGIzww&review%5Bcontent%5D=He+dresses+weird+and+talks+funny.&review%5Brating%5D=5&review%5Bcourse_id%5D=1&commit=Submit+Review",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"5b163b12e1f2e9f62f3589ae5a34cefb"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "TxecMmeVFY42litJorg5puV4lvrxl9zoj2B0hPyI8fU6Yb24uMMrpCskdT1qOGZKbWc-1McEgQqe5tLWWmux1w",
                "x-turbo-request-id": "88ec22cd-5a95-46e6-9e52-c866adba87bc",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"3062eee724082d994fceb0b17e2e42f7"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "c0e6556c-dd81-4ebc-83b4-a1ecba8192d1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/logout",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "120",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "Y7PazNxg7LJIjdbmi39apMGohVb4ysriYzM129Ra2d4WxftGAzbSmFU_iJJD_wVISbcteM5ZlwBytZOJcrmZ_A",
                "x-turbo-request-id": "598ebd0a-d347-43b5-9c51-949d08dab468",
            },
            data="_method=delete&authenticity_token=Y1hCA-A4ZG7M5uabua5osq2r0mR-HnwWMRIqMk1ow1-7_QUl2m7SMmKqKxTx3RhN_uyqtq-Q2QOp-jdkrHALXg",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "Y7PazNxg7LJIjdbmi39apMGohVb4ysriYzM129Ra2d4WxftGAzbSmFU_iJJD_wVISbcteM5ZlwBytZOJcrmZ_A",
                "x-turbo-request-id": "598ebd0a-d347-43b5-9c51-949d08dab468",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login"
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(make_prof_make_review)
