import sys
from os import path

from pandas import read_csv


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)


class OpenData:
    def __init__(self):
        self.threadDataFile = resource_path('thread.csv')
        self.threadDataFileShaft = resource_path('threadShaft.csv')
        self.threadDataFileHole = resource_path('threadHole.csv')

        self.df_thread = read_csv(self.threadDataFile, header=0)
        self.df_thread_shaft = read_csv(self.threadDataFileShaft, header=0)
        self.df_thread_hole = read_csv(self.threadDataFileHole, header=0)

    def getDiameter(self):
        return [str(int(x)) if x - int(x) == 0 else str(x) for x in self.df_thread['dD']]

    def getStep(self, dD):
        return str.split(
            self.df_thread['P'].to_numpy()[self.df_thread['dD'].to_numpy() == float(dD)].item(), '/')

    def getThreadData(self, dD, P):
        threadData = []
        threadData.append(str(dD))
        threadData.append(str(P))

        threadParam_shaft = self.df_thread_shaft.loc[self.df_thread_shaft['P'] == float(P)].to_numpy()
        threadParam_hole = self.df_thread_hole.loc[self.df_thread_hole['P'] == float(P)].to_numpy()

        if len(threadParam_shaft) != 0 and len(threadParam_hole) != 0:
            threadData.append(str(round((float(dD) - 1.0825 * float(P)), 3)))
            threadData.append(str(round((float(dD) - 0.6495 * float(P)), 3)))

            threadData.append(str(round(float(threadParam_shaft[0][7]), 3)))

            for i in range(1, len(threadParam_shaft[0])-2):
                threadData.append([str(x) for x in threadParam_shaft[0]][i])

            threadData.append(str(round(float(dD) - float(threadParam_shaft[0][6]), 3)))

            for i in range(1, len(threadParam_hole[0])-2):
                threadData.append([str(x) for x in threadParam_hole[0]][i])

            threadData.append(str(round(float(dD) + float(threadParam_hole[0][6]), 3)))

        else:
            for i in range(15):
                threadData.append(str(0))

        return threadData

    def getClosest(self, dD):
        closest = []
        row = self.df_thread['row'].to_numpy()[self.df_thread['dD'].to_numpy() == float(dD)].item()

        df1 = self.df_thread.drop(self.df_thread[self.df_thread['row'] != 1].index)
        df2 = self.df_thread.drop(self.df_thread[self.df_thread['row'] != 2].index)

        closest.append(str(row))
        closest.append(str(dD))

        if row == 1:
            return closest
        else:
            if row == 2:
                res = df1.iloc[(df1['dD'] - float(dD)).abs().argsort()[:2]]
                diam = [str(int(x)) if x - int(x) == 0 else str(x) for x in res['dD']]
                closest.append(diam[0])
                closest.append(diam[1])
                return closest
            else:
                res1 = df1.iloc[(df1['dD'] - float(dD)).abs().argsort()[:2]]
                res2 = df2.iloc[(df2['dD'] - float(dD)).abs().argsort()[:2]]
                diam1 = [str(int(x)) if x - int(x) == 0 else str(x) for x in res1['dD']]
                diam2 = [str(int(x)) if x - int(x) == 0 else str(x) for x in res2['dD']]
                for i in range(2):
                    closest.append(diam1[i])
                for i in range(2):
                    closest.append(diam2[i])
                return closest
