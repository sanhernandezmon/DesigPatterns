# Target Interface
class Target:
    def request(self):
        raise NotImplementedError

# Adaptee (The class with an incompatible interface)
class ToAdapt:
    def specific_request(self):
        print("ToAdapt's specific request")

# Adapter (Adapter class that wraps the Adaptee)
class Adapter(Target):
    def __init__(self, toAdapt):
        self.toAdapt = toAdapt

    def request(self):
        print("Adapter's request")
        self.toAdapt.specific_request()

# Creating an instance of toAdapt
toAdapt = ToAdapt()

# Creating an Adapter instance and passing the ToAdapt to it
adapter = Adapter(toAdapt)

# Using the Adapter in client code
adapter.request()
