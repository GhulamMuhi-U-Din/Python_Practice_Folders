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