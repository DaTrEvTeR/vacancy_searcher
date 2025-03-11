import aiohttp


class CustomSession:
    def __init__(self, *args, **kwargs):
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "accept": "application/json,*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "ru,uk;q=0.9,en;q=0.8",
        }
        self.args = args
        self.kwargs = kwargs
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers, *self.args, **self.kwargs)
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
