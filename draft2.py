import pandas as pd
import numpy as np

class moviedata():
    
    def __init__(self) -> None:
        self.credits=pd.read_csv("archive\credits.csv")
        self.credits.merge(pd.read_csv("archive\credits-2.csv"))


dfcs=moviedata()
print(dfcs.credits)