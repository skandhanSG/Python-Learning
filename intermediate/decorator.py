import time

def process(func):

    def timer():
        print("starting  now ............................................")
        start = time.time()

        func()

        print("ending now.....................................")

        end = time.time()

        print(f"the execuation timing is : {end - start}")

    return(timer)


@process
def test():
    print("this is under test")

test()   
