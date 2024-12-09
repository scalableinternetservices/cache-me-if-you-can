from locust import task, run_single_user
from locust import FastHttpUser


class make_multiple_reviews(FastHttpUser):
    host = "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/search?query=vinayak&commit=Search",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-turbo-request-id": "0002220d-22a1-4dee-b3a9-ba0643dec820",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/search?query=vinayak&commit=Search"
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/search?query=Vinayak&commit=Search",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/search?query=vinayak&commit=Search",
                "accept": "text/html, application/xhtml+xml",
                "x-turbo-request-id": "a704d55d-40e6-4b64-b9c2-4c7b66157617",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/search?query=Vinayak&commit=Search"
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
                "If-None-Match": 'W/"4013c75988e4a87ab506d67292f440d7"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/search?query=Vinayak&commit=Search",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "38edeaa3-54b9-47bb-b4d1-63136a28cc62",
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
                "x-turbo-request-id": "0e4aea27-a715-43e2-80c5-5d02c26a21b2",
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
                "If-None-Match": 'W/"2ec301dbe2dcc45c6d7ecd8843bbce93"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "0e4aea27-a715-43e2-80c5-5d02c26a21b2",
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
            "/students/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"8f3324f1b6b293b4e612252e1f3da95b"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "b6a006a6-e92e-42ea-9e84-213b6773abe0",
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
                "x-csrf-token": "x7mdiY6XQ5LSFARYtriLpPRbpZgrYJqJ_c03Y_y4nZSyz7wDUcF9uM-mWix-ONRIfEQNth3zx2vsS5ExWlvdtg",
                "x-turbo-request-id": "cd2c52ed-6ac0-4125-8463-1b3a9d666c64",
            },
            data="authenticity_token=WuzGca4XoQor8DVEXG7oWuQYVSZEupWCvIyLB52CxIYGZFV9aQkoT813UnWOem0DOWBaglfP1jmt1XuIMlex8g&student%5Busername%5D=cataquack&student%5Bpassword%5D=cataquack&commit=Register",
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
                "If-None-Match": 'W/"e4bf60f7f3ff2b2de2901f83a183e957"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/students/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "21da2307-8a80-4dca-aa0b-264b2e54b24c",
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
                "x-csrf-token": "qA4brU6vq15StLsJWWpqqO9dsK7fnr8PCxaEPXBhemvdeDonkfmVdE8G5X2R6jVEZ0IYgOkN4u0akCJv1oI6SQ",
                "x-turbo-request-id": "2e7aaa84-10bc-4d51-aab4-93205de09300",
            },
            data="authenticity_token=iM7_aLwyn84fdPa6hs2iH9E_r5qCUdxQZZb_VB-PpKBE0xIHO1gOuCrbUFvSgLnKd3rAdX6FyPTrtwTIsPBmcw&username=cataquack&password=cataquack&commit=Log+In",
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
                "If-None-Match": 'W/"9e4f8b92091beae264a5e4c7317d2e88"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/login",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "qA4brU6vq15StLsJWWpqqO9dsK7fnr8PCxaEPXBhemvdeDonkfmVdE8G5X2R6jVEZ0IYgOkN4u0akCJv1oI6SQ",
                "x-turbo-request-id": "2e7aaa84-10bc-4d51-aab4-93205de09300",
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
            "/courses",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"c8c00a40ca2bdc681b95755016f4b467"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "dcea3089-5b6a-45da-ba09-b824c5b5eb30",
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
                "If-None-Match": 'W/"bc5dcebcd60f9dd04251a8b365bd233e"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "0d3696e1-ea31-4a50-8411-d460cc883a8d",
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
                "If-None-Match": 'W/"2f7fb11d1802373f8ef516dafec41e94"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "a4427bd8-de62-4b88-8294-a16a958d368d",
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
                "If-None-Match": 'W/"3b007f504f8868841b7254fba7338279"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "48dc1978-6d35-40ee-a117-e83090160369",
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
                "x-turbo-request-id": "24a7ba72-8265-461d-aa87-17e4e8159725",
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
                "If-None-Match": 'W/"11c64dacbc525c027e0ea8a4a95be6e5"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "4cd168d1-4484-433b-9637-12ce5bdd4028",
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
                "Content-Length": "245",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "PZ8vxzxAlZkW1wX23lVooAeeG6mRlhvYBO1Cq2bgk6RI6Q5N4xarswtlW4IW1TdMj4Gzh6cFRjoVa-T5wAPThg",
                "x-turbo-request-id": "9c35974d-7dae-4cdc-8cb6-ae1b8e491209",
            },
            data="authenticity_token=PJtIByg-suc_bdq8YfFjNIAZSHlx_K1ckRR0vBwnYKO6Sv49xNLEOhAfb_YDPrgTo67W2GLwUlSUfRv-GLlf8Q&course%5Bname%5D=How+to+walk+on+your+hands&course%5Bcode%5D=blah101&course%5Bdescription%5D=How+to+walk+on+your+hands.&commit=Create+Course",
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
                "x-csrf-token": "PZ8vxzxAlZkW1wX23lVooAeeG6mRlhvYBO1Cq2bgk6RI6Q5N4xarswtlW4IW1TdMj4Gzh6cFRjoVa-T5wAPThg",
                "x-turbo-request-id": "9c35974d-7dae-4cdc-8cb6-ae1b8e491209",
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
                "If-None-Match": 'W/"e401cb5c8a48445b9f461a18ea447d9a"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "3775c22e-a609-4525-84bb-765231993b6b",
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
                "If-None-Match": 'W/"a55209c70bfe7d3f5ae7bff15fcc9b3f"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/courses",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "5e6e2779-d1d8-4184-a219-e48bd85dd3d5",
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
                "If-None-Match": 'W/"625667d436f5593abc07e606c1ecd25a"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "96e59c9d-0d8a-49e5-a015-4e530b76c184",
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
                "If-None-Match": 'W/"f92ed9c46ea02aeb50d6baf235e7dbd4"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "ea4ea29b-2d12-4664-b3ae-4cd54891d7e4",
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
                "If-None-Match": 'W/"9d522672939693e6e5005bcdb47f1a0b"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "c83c069b-9893-4a7a-881e-7561ed395eb4",
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
                "Content-Length": "206",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "ibmnl7pm0fWPti7ABM9Av8OuER9ITM832MbZUjxJi3T8z4YdZTDv35IEcLTMTx9TS7G5MX7fktXJQH8AmqrLVg",
                "x-turbo-request-id": "1d18647a-2daa-4457-8945-a924452a5ead",
            },
            data="authenticity_token=YB-t0w4W-uN2kQZPCQpnJPT_0exLZ2BQuO7j3b5a5SZIhlIDlOGcaHiDSS5FynHpL5RQ0AmdG7iABUIaXlUE4g&review%5Bcontent%5D=He%27s+great.&review%5Brating%5D=5&review%5Bcourse_id%5D=76&commit=Submit+Review",
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
                "If-None-Match": 'W/"a3a27691c7005aa652a0f377cefc8412"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "ibmnl7pm0fWPti7ABM9Av8OuER9ITM832MbZUjxJi3T8z4YdZTDv35IEcLTMTx9TS7G5MX7fktXJQH8AmqrLVg",
                "x-turbo-request-id": "1d18647a-2daa-4457-8945-a924452a5ead",
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
                "If-None-Match": 'W/"3af8fff4a79551cf86ac416a09bbc915"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "2d094941-45b2-4bae-aab0-14a02e243d9a",
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
                "If-None-Match": 'W/"97bcb110d9fd9585f7478c86f6d6e8cc"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "204a056c-2a7a-4d07-95e0-a2e0c5de2763",
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
                "If-None-Match": 'W/"39d0211a6456999d6a9471e4c285f7c6"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "90a1c885-3ae3-4c67-90eb-17cae4aed1c1",
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
                "Content-Length": "208",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "egJas7WExfq3BJ6akwKHy6L_vJjTYSzpybcFZNNw_6IPdHs5atL70Kq2wO5bgtgnKuAUtuXycQvYMaM2dZO_gA",
                "x-turbo-request-id": "63b8b3ea-1e6c-4a66-8475-ae431393cc31",
            },
            data="authenticity_token=Ng59adsYjrPdgpwHEE-tl_fLVbgObIjq-7U31-Nw3Qsel4K5Qe_oONOQ02Zcj7taLKDUhEyW8wLDXpYQA388zw&review%5Bcontent%5D=He%27s+so+cool.&review%5Brating%5D=4&review%5Bcourse_id%5D=76&commit=Submit+Review",
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
                "If-None-Match": 'W/"737b46db17a89ea37bb24d2099a8dd71"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "egJas7WExfq3BJ6akwKHy6L_vJjTYSzpybcFZNNw_6IPdHs5atL70Kq2wO5bgtgnKuAUtuXycQvYMaM2dZO_gA",
                "x-turbo-request-id": "63b8b3ea-1e6c-4a66-8475-ae431393cc31",
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
                "If-None-Match": 'W/"954e89f4df35bbc14235e9a396e9e596"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "049e550b-9dd0-4920-9054-d21784b60004",
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
                "If-None-Match": 'W/"4dd6d597c2cfb2090c5a5285dd849d7c"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "cb4c42c9-079e-4ca2-8b14-73b3a4d67dba",
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
                "Content-Length": "204",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "gI6B6NwipNIpqPPRjp7muNEh2O2FVKAmaTbEP55saE31-KBiA3Sa-DQaraVGHrlUWT5ww7PH_cR4sGJtOI8obw",
                "x-turbo-request-id": "7e93e943-a30b-4dee-9bcb-9d9ccc0199a6",
            },
            data="authenticity_token=1Hq1TpW0hm4y8WOlMGxElL9_BANHbVBqSNIle2_9nc7840qeD0Pg5TzjLMR8rFJZZBSFPwWXK4JwOYS8j_J8Cg&review%5Bcontent%5D=He%27s+meh.&review%5Brating%5D=3&review%5Bcourse_id%5D=76&commit=Submit+Review",
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
                "If-None-Match": 'W/"250df3306e841a939612706d9bee9db6"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "gI6B6NwipNIpqPPRjp7muNEh2O2FVKAmaTbEP55saE31-KBiA3Sa-DQaraVGHrlUWT5ww7PH_cR4sGJtOI8obw",
                "x-turbo-request-id": "7e93e943-a30b-4dee-9bcb-9d9ccc0199a6",
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
                "If-None-Match": 'W/"b1b7db6e71ae1cb339e0ce54e87a0068"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "7292d45e-ab38-4e2d-87a2-3e48558b709a",
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
                "If-None-Match": 'W/"bd8430cfd7f8e64fa3baa75b99427bea"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "a6cbb3a7-dd36-46cc-a77b-586403193aa3",
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
                "If-None-Match": 'W/"33e0f19394d950b2e2eb08b46af19e8a"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "4a00008e-6078-4d15-8129-779cd81db619",
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
                "If-None-Match": 'W/"72c16b1852264f0a6f74a9f0704cd4f9"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "87a5c808-c962-4a43-9829-b7e715107645",
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
                "Content-Length": "197",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "jWasOSj-53a0F2A0dMmHQL_cEIcO6AMSSfIaQhQo0pL4EI2z96jZXKmlPkC8SdisN8O4qTh7XvBYdLwQssuSsA",
                "x-turbo-request-id": "9e512be1-a51d-48b4-a593-d6c30d83e36a",
            },
            data="authenticity_token=4sZ4_frhw8xnA0-UgenmDFfphl4rp9n_c8j6IjLnf_PKX4ctYBalR2kRAPXNKfDBjIIHYmldohdLI1vl0uieNw&review%5Bcontent%5D=Bad.&review%5Brating%5D=2&review%5Bcourse_id%5D=76&commit=Submit+Review",
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
                "If-None-Match": 'W/"240db2ad5f216cc4c5e0487690bf75d6"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "jWasOSj-53a0F2A0dMmHQL_cEIcO6AMSSfIaQhQo0pL4EI2z96jZXKmlPkC8SdisN8O4qTh7XvBYdLwQssuSsA",
                "x-turbo-request-id": "9e512be1-a51d-48b4-a593-d6c30d83e36a",
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
                "If-None-Match": 'W/"70f6ff59ac06b5130d81833151b3c632"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "98955821-340b-49e5-a788-4b1b68728a81",
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
                "If-None-Match": 'W/"8426b97831411b2ae8479ac0765637aa"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "84a4ec41-ea7d-4113-a892-22301ac80054",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/professors/1/reviews/72",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "14b6b559-c0ae-44d8-8e59-7465ab4251be",
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
                "If-None-Match": 'W/"2c4e8384b622f4bd26a1f29eaf57c842"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "99cd07b3-96bb-44c1-97ba-b60e89cb8342",
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
            "POST",
            "/professors/1/reviews",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "202",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "J4jFOtFSKLAzHji9yH_Yr509MFrjVPW0aRYAdfZUKlhS_uSwDgQWmi6sZskA_4dDFSKYdNXHqFZ4kKYnULdqeg",
                "x-turbo-request-id": "c1eae104-bd71-447c-b2b7-d40b6a8482dc",
            },
            data="authenticity_token=h9WwejfkETM3VtDgXFnqVQKfX5dZsFq4obOWJSxpf7OvTE-qrRN3uDlEn4EQmfyY2fTeqxtKIVCZWDfizGaedw&review%5Bcontent%5D=%3E%3A%28&review%5Brating%5D=1&review%5Bcourse_id%5D=76&commit=Submit+Review",
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
                "If-None-Match": 'W/"f40277903a6cf0d8bd5dba112b49f661"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1/reviews/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "J4jFOtFSKLAzHji9yH_Yr509MFrjVPW0aRYAdfZUKlhS_uSwDgQWmi6sZskA_4dDFSKYdNXHqFZ4kKYnULdqeg",
                "x-turbo-request-id": "c1eae104-bd71-447c-b2b7-d40b6a8482dc",
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
            "/professors/1/reviews/1",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "b49134e8-41ac-4db7-b72a-40bae1ad1aca",
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
                "If-None-Match": 'W/"e06e37bfefb92e19149e27cc4bf13f4c"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "00e4b55e-4687-4ccd-bb9c-cd430d5c4c85",
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
                "If-None-Match": 'W/"c39a93b26e3ac53390ecffb2edd9dcaf"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/1",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "465956a9-42a7-43bc-97ee-1d57e7076dd3",
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
                "x-csrf-token": "5fgITdN_mBqwguvCFVR0z56B2xOaWQiwdDg-Wf2sT1yQjinHDCmmMK0wtbbd1CsjFp5zPazKVVJlvpgLW08Pfg",
                "x-turbo-request-id": "527eb381-1471-4d46-9842-c8a1ce56da85",
            },
            data="_method=delete&authenticity_token=Re3fGzlGRqqIB14XpqBkEmDlwS7R6xiQhpUMfv6g6pCdSJg9AxDw9iZLk5ju0xTtM6K5_ABlvYUefREoH7gikQ",
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
                "x-csrf-token": "5fgITdN_mBqwguvCFVR0z56B2xOaWQiwdDg-Wf2sT1yQjinHDCmmMK0wtbbd1CsjFp5zPazKVVJlvpgLW08Pfg",
                "x-turbo-request-id": "527eb381-1471-4d46-9842-c8a1ce56da85",
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
    run_single_user(make_multiple_reviews)
