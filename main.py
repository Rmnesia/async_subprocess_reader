import sys
import asyncio
from io import BytesIO, TextIOWrapper

async def run():
    await asyncio.sleep(1)
    # Sim async stdout
    print("ajsdkhakhdka")
    await asyncio.sleep(1)
    print("abc")
    print("dasjkhdahshdkakhsfk")
    await asyncio.sleep(1)
    print("dasdasd")
    await asyncio.sleep(10)
    print("daaaaaaaa")
    await asyncio.sleep(5)
    print("hello")
    await asyncio.sleep(1)
    print("Async operation completed")

async def loop_and_capture_output():
    while True:
        # setup the environment
        old_stdout = sys.stdout
        sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
        # wait for a short period of time
        await asyncio.sleep(1)
        # get output
        sys.stdout.seek(0)  # jump to the start
        out = sys.stdout.read()  # read output

        # restore stdout
        sys.stdout.close()
        sys.stdout = old_stdout

        if out:
            # do stuff with the output
            print(out.upper())

async def main():
    # start the loop_and_capture_output task
    loop_task = asyncio.create_task(loop_and_capture_output())

    # wait for the run() function to complete
    await run()

    # cancel the loop_and_capture_output task
    loop_task.cancel()

    # wait for the loop_and_capture_output task to be cancelled
    try:
        await loop_task
    except asyncio.CancelledError:
        pass

# run the main function
asyncio.run(main())
