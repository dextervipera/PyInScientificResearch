# asycnio
import asyncio
from time import sleep

async def routine(times: int):
    if times < 0:
        print("Finished")
    else:
        sleep(1)
        print(times)

def main():
    print("Main test")
    asyncio.run(routine(6))
    
    
if __name__ =="__main__":
    main()