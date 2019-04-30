from models import Ensemble

ens = Ensemble.Ensemble(small=True)

ens.evaluate()

print("acc:",ens.get_acc(),"err:",ens.get_acc_error())