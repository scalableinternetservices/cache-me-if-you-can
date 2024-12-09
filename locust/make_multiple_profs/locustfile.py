from locust import task, run_single_user
from locust import FastHttpUser


class make_multiple_profs(FastHttpUser):
    host = "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/professors/new",
            headers={
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "If-None-Match": 'W/"ec6fcebb10123af7788b4f288a893e34"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "26265856-731b-4075-9356-ab90982c38aa",
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
                "Content-Length": "215",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "bmBOTm9V8K2-nYy59pIuILZD07Ig7DGrlraRnTar9GcbFm_EsAPOh6Mv0s0-EnHMPlx7nBZ_bEmHMDfPkEi0RQ",
                "x-turbo-request-id": "e6527286-04d9-4a99-9c30-6e4bb26dce76",
            },
            data="authenticity_token=PoGVLGbp3MLmsPK1GX1feiACoNzCjTBEyWcIzIGetpKm-MArQs3Xru5LKPcspfaH7yKXAHErAbjDupF3UJJVTg&professor%5Bname%5D=Miles+Morales%2C+Ph.D.&professor%5Bdepartment%5D=Computer+Science&commit=Create+Professor",
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
                "x-csrf-token": "bmBOTm9V8K2-nYy59pIuILZD07Ig7DGrlraRnTar9GcbFm_EsAPOh6Mv0s0-EnHMPlx7nBZ_bEmHMDfPkEi0RQ",
                "x-turbo-request-id": "e6527286-04d9-4a99-9c30-6e4bb26dce76",
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
                "If-None-Match": 'W/"b267bdfa6ae55f4a4e21701f00ffec1a"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "01ee8255-c76b-4225-9a2c-b0271ad54a90",
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
                "Content-Length": "211",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "S3YFBWf_SEBJXYzFJGSARhoe6z_S2qGJnzjRGOyuKR0-ACSPuKl2alTv0rHs5N-qkgFDEeRJ_GuOvndKSk1pPw",
                "x-turbo-request-id": "9720435a-8847-4d7a-ba7b-d3ee46ad9e2b",
            },
            data="authenticity_token=qCE5t_mBw3N5K2gscqsEKw42jxLPPXs5AfqdeGK8qH8wWGyw3aXIH3HQsm5Hc63WwRa4znybSsULJwTDs7BLow&professor%5Bname%5D=Guy+Fieri%2C+Ph.D.&professor%5Bdepartment%5D=Computer+Science&commit=Create+Professor",
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
                "x-csrf-token": "S3YFBWf_SEBJXYzFJGSARhoe6z_S2qGJnzjRGOyuKR0-ACSPuKl2alTv0rHs5N-qkgFDEeRJ_GuOvndKSk1pPw",
                "x-turbo-request-id": "9720435a-8847-4d7a-ba7b-d3ee46ad9e2b",
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
                "If-None-Match": 'W/"b0424e6deb7ddb93e4e262b2aabd41d7"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "4c40838c-c612-43e1-8907-e2d81d204480",
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
                "If-None-Match": 'W/"353d1e6ed516b49762d9e224aa639594"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "369ea5ac-1a39-4ab8-9550-22c6ad00c90c",
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
                "Content-Length": "211",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "teEhK7cLVihuQVU2jMYn1tTwOo5pGd6dzZ5ss1fbxRjAlwChaF1oAnPzC0JERng6XO-SoF-Kg3_cGMrh8TiFOg",
                "x-turbo-request-id": "1911ba22-1930-4d7d-ab97-2770d1e3258e",
            },
            data="authenticity_token=xM_yZQ7YSRE2Jo0AsSd1bj1vXf-blocezUi8X6-snqBctqdiKvxCfT7dV0KE_9yT8k9qIygwtuLHlSXkfqB9fA&professor%5Bname%5D=Joe+Biden%2C+Ph.D.&professor%5Bdepartment%5D=Computer+Science&commit=Create+Professor",
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
                "x-csrf-token": "teEhK7cLVihuQVU2jMYn1tTwOo5pGd6dzZ5ss1fbxRjAlwChaF1oAnPzC0JERng6XO-SoF-Kg3_cGMrh8TiFOg",
                "x-turbo-request-id": "1911ba22-1930-4d7d-ab97-2770d1e3258e",
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
                "If-None-Match": 'W/"e93f540149d3cdeba09e3e3682bcdacc"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "b462c016-ea89-427c-a7d2-29960285180d",
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
                "If-None-Match": 'W/"5dc7052067fba72af7a21898f9b3fdf3"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "33810702-2b88-44e1-83cd-6645653a4466",
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
                "Content-Length": "214",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "_rIEGUguBAB78OagUHJtHDqg0d-vI9C-CUQIlIvSqOSLxCWTl3g6KmZCuNSY8jLwsr958ZmwjVwYwq7GLTHoxg",
                "x-turbo-request-id": "58a41133-307a-460d-a434-b21225ca8c6d",
            },
            data="authenticity_token=9dA-Z5ae3OdlemqWBm9GqxlOGHb5f50kk967axlUbaVtqWtgsrrXi22BsNQzt-9W1m4vqkrZrNiZAyLQyFiOeQ&professor%5Bname%5D=Jason+Bourne%2C+Ph.D.&professor%5Bdepartment%5D=Computer+Science&commit=Create+Professor",
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
                "x-csrf-token": "_rIEGUguBAB78OagUHJtHDqg0d-vI9C-CUQIlIvSqOSLxCWTl3g6KmZCuNSY8jLwsr958ZmwjVwYwq7GLTHoxg",
                "x-turbo-request-id": "58a41133-307a-460d-a434-b21225ca8c6d",
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
                "If-None-Match": 'W/"d82f5c40ed7032016853c9b6f234b3c0"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "947620d9-9e41-4186-906c-3dd04cc854aa",
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
                "Content-Length": "212",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "oyapguhUNj7HGNwc451V2P5C18efUao3017n3ANs69bWUIgINwIIFNqqgmgrHQo0dl1_6anC99XC2EGOpY-r9A",
                "x-turbo-request-id": "5c74804a-76e3-4642-850d-34121910bb45",
            },
            data="authenticity_token=Mk-B1JorUWfyffnkiZsz7h3HcIiyV9Yoo9Sn07x4eJKqNtTTvg9aC_qGI6a8Q5oT0udHVAHx59SpCT5obXSbTg&professor%5Bname%5D=Hulk+Hogan%2C+Ph.D.&professor%5Bdepartment%5D=Computer+Science&commit=Create+Professor",
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
                "x-csrf-token": "oyapguhUNj7HGNwc451V2P5C18efUao3017n3ANs69bWUIgINwIIFNqqgmgrHQo0dl1_6anC99XC2EGOpY-r9A",
                "x-turbo-request-id": "5c74804a-76e3-4642-850d-34121910bb45",
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
                "If-None-Match": 'W/"3b49cc3dd4227d5fe754857bdd404759"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "4033164c-6822-422a-8087-72d5d83e2ec9",
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
                "Content-Length": "215",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Origin": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com",
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors/new",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "9oasbYGXbwfOF7uICjCp4AkPbQOz03dpie6zNzBAbsOD8I3nXsFRLdOl5fzCsPYMgRDFLYVAKouYaBVllqMu4Q",
                "x-turbo-request-id": "bd463130-9093-4a60-8eb1-d8438074d985",
            },
            data="authenticity_token=7jda0epIjldOlG56CiC0J3kPIGtca4reaDcO6RxSiPp2Tg_WzmyFO0ZvtDg_-B3ati8Xt-_NuyJi6pdSzV5rJg&professor%5Bname%5D=David+Tennant%2C+Ph.D.&professor%5Bdepartment%5D=Computer+Science&commit=Create+Professor",
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
                "x-csrf-token": "9oasbYGXbwfOF7uICjCp4AkPbQOz03dpie6zNzBAbsOD8I3nXsFRLdOl5fzCsPYMgRDFLYVAKouYaBVllqMu4Q",
                "x-turbo-request-id": "bd463130-9093-4a60-8eb1-d8438074d985",
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
                "If-None-Match": 'W/"b11db1a57f9f7f0dde59424a4f848b6a"',
                "Referer": "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com/professors",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "d165ce04-85ad-475a-9ad8-15378e9b226b",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(make_multiple_profs)
