from locust import task, run_single_user, between, FastHttpUser


class MultipleFlowUser(FastHttpUser):
    wait_time = between(0.5, 10)
    host = "http://vinayakgajjewar.eba-bmmpctqy.us-west-2.elasticbeanstalk.com"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    @task
    def make_multiple_profs(self):
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

    @task
    def make_multiple_reviews(self):
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

    @task
    def make_prof_make_review(self):
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
    run_single_user(MultipleFlowUser)
