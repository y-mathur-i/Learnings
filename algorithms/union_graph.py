"""Module for disjoint union set greaph
"""


class DSU:
    """DSU graph
    """
    def __init__(self) -> None:
        self.par = list(range(1001))
        self.rank = [0]*1001

    def findPar(self, x: int) -> int:
        """Method to get the parent
        """
        if self.par[x] != x:
            return self.findPar(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        """Method to union/add the nodes into same grp
        """
        xp, yp = self.findPar(x),self.findPar(y)
        if xp==yp:
            return False
        elif self.rank[xp] < self.rank[yp]:
            self.par[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.par[yp] = xp
        else:
            self.par[yp] = xp
            self.rank[xp] += 1
        return True
