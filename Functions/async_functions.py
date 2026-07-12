# =====================================
# SINGLE TASK
#======================================

# Import asyncio module
import asyncio

# Create an async function
async def hello():

    # Print before waiting
    print("Start")

    # Wait asynchronously for 2 seconds
    await asyncio.sleep(2)

    # Print after waiting
    print("End")


# Start and run the async program
asyncio.run(hello())

# =====================================
# MULTIPLE TASKS
#======================================

import asyncio

async def task1():

    print("Task 1 Started")

    await asyncio.sleep(3)

    print("Task 1 Completed")

async def task2():

    print("Task 2 Started")

    await asyncio.sleep(1)

    print("Task 2 Completed")

async def main():

    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())