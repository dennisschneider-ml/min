import broker
from net import Network
from logic import Logic

net = Network('/tmp/min.so')
logic = Logic()

broker.register(net)
broker.register(logic)

net.run()



