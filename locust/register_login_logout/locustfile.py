from locust import task, run_single_user
from locust import FastHttpUser


class register_login_logout(FastHttpUser):
    host = "http://localhost:3000"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "localhost:3000",
                "If-None-Match": 'W/"68515f217ae916c023bcdef985e632ec"',
                "Referer": "http://localhost:3000/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/html, application/xhtml+xml",
                "x-sec-purpose": "prefetch",
                "x-turbo-request-id": "bc644dad-301d-4c94-b209-51e7336c3c12",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={"Referer": "http://localhost:3000/login"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "157",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "localhost:3000",
                "Origin": "http://localhost:3000",
                "Referer": "http://localhost:3000/login",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "uq5tMLsSGz2mk618jPikeKxRueDJLZWhfZzH_WPWTRyVbLC6ExCSlEVARA4C-faRzHIt8kFEJvDZyfAc_IXYlQ",
                "x-turbo-request-id": "ce9a4934-d7d4-4ebe-bb7d-667b28ccb0a0",
            },
            data="authenticity_token=nwsW0ORtb-1UVD9lTky9jSHmEeAMaqrq7faGnpa59Rc-T09k_Ytdyh6t0DJpCSp6AefIGyCj4z3WSxEMr_0GMg&username=cataquack&password=cataquack&commit=Log+In",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "localhost:3000",
                "If-None-Match": 'W/"f1436071f56abaa9883dbb01a4f8d6d3"',
                "Referer": "http://localhost:3000/login",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "uq5tMLsSGz2mk618jPikeKxRueDJLZWhfZzH_WPWTRyVbLC6ExCSlEVARA4C-faRzHIt8kFEJvDZyfAc_IXYlQ",
                "x-turbo-request-id": "ce9a4934-d7d4-4ebe-bb7d-667b28ccb0a0",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={"Referer": "http://localhost:3000/"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/logout",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "120",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "localhost:3000",
                "Origin": "http://localhost:3000",
                "Referer": "http://localhost:3000/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "z62f_r3oTU_Epmfmq4GIBJMSY-XAsnCWRgjMf55m5TDgb0J0FerE5id1jpQlgNrt8zH390jbw8fiXfueATVwuQ",
                "x-turbo-request-id": "62a2d1be-bdd4-4557-9074-1718402b9510",
            },
            data="_method=delete&authenticity_token=6EV0tRY-60d1qxAsZb-8Zf3vmqn-24rtZa2R3vYrWNXhx4oyuIxa6jJ1KSIH94hq3Gt63ZUdmOTq5XtOFXcahA",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "localhost:3000",
                "Referer": "http://localhost:3000/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "z62f_r3oTU_Epmfmq4GIBJMSY-XAsnCWRgjMf55m5TDgb0J0FerE5id1jpQlgNrt8zH390jbw8fiXfueATVwuQ",
                "x-turbo-request-id": "62a2d1be-bdd4-4557-9074-1718402b9510",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={"Referer": "http://localhost:3000/login"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "157",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Host": "localhost:3000",
                "Origin": "http://localhost:3000",
                "Referer": "http://localhost:3000/login",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "CQZqW3JK8bac0mJkwtQp8LQDi5etKqVDpIOAE3AlSQkmxLfR2kh4H38BixZM1XsZ1CAfhSVDFhIA1rfy73bcgA",
                "x-turbo-request-id": "b05d05be-7445-497c-9b31-d17c30813510",
            },
            data="authenticity_token=8dnalQ9yMDD0vsz1vhJNlVIYlPQ4-vi05BU7zfV3WlVQnYMhFpQCF75HI6KZV9pichlNDxQzsWPfqKxfzDOpcA&username=cataquack&password=cataquack&commit=Log+In",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Host": "localhost:3000",
                "If-None-Match": 'W/"32cbdc316f87be97ced79f46d1460bdb"',
                "Referer": "http://localhost:3000/login",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "accept": "text/vnd.turbo-stream.html, text/html, application/xhtml+xml",
                "x-csrf-token": "CQZqW3JK8bac0mJkwtQp8LQDi5etKqVDpIOAE3AlSQkmxLfR2kh4H38BixZM1XsZ1CAfhSVDFhIA1rfy73bcgA",
                "x-turbo-request-id": "b05d05be-7445-497c-9b31-d17c30813510",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={"Referer": "http://localhost:3000/"},
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(register_login_logout)
