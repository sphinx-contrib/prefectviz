from prefect import task, Flow


@task
def hello_world():
    print("Hi!")


with Flow(name="Random") as flow:
    hello_world()
