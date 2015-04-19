from django.db import models

# Create your models here.

class Maze(models.Model):
    name = models.CharField(max_length=128, unique=True)
    width = models.IntegerField()
    height = models.IntegerField()
    cells = models.TextField()
    __grid = None

    def getOrCreateGrid(self):
        if self.rows*self.cols > len(self.cells):
            self.cells = []
            return self.cells
        if(self.__grid):
            return self.__grid

        cells = [str(x) for x in self.cells if x == "1" or x == "0"]
        grid = []
        index = 0
        for i in xrange(self.rows):
            row = []
            for j in xrange(self.cols):
                row += cells[index]
                index += 1
            grid += [row]
        self.__grid = grid
        return grid

    def __unicode__(self):
        return self.name