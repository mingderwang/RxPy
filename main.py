from rx import of

source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
print(type(source))
print(dir(source))
print(source)
print('----------')
source.subscribe(lambda value: print("Received {0}".format(value)))