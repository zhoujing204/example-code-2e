import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD_LEN = 4  # <1>

async def probe(domain: str) -> tuple[str, bool]:  # <2>
    loop = asyncio.get_running_loop()  # <3>
    try:
        await loop.getaddrinfo(domain, None)  # <4>
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main() -> None:  # <5>
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() for name in names)  # <7>
    async with asyncio.TaskGroup() as tg:
        for domain in domains:
            tg.create_task(probe(domain))
        async for task in tg:
            domain, found = task.result
            mark = '+' if found else '-'
            print(f'{mark} {domain}')
            

if __name__ == '__main__':
    asyncio.run(main())  # <11>