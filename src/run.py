import broker
from net import Network
from logic import Logic

import daemon
import lockfile
import os


with daemon.DaemonContext(
        working_directory=os.path.dirname(os.path.realpath(__file__)),
        pidfile=lockfile.FileLock("/tmp/min.pid")
    ):
    net = Network('/tmp/min.so')
    logic = Logic()

    broker.register(net)
    broker.register(logic)

    net.run()



