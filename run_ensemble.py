from models import Ensemble
import numpy as np

ens = Ensemble.Ensemble()

ens.evaluate()

print("acc:",ens.get_acc(),"err:",ens.get_acc_error())
