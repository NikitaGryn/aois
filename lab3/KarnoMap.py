from variable import *


class KarnoMap:
    def __init__(self, table, variables):
        self.variables = variables

        if len(variables) > 4:
            return

        if len(variables) <= 1:
            return

        if len(variables) == 4:
            self.xSize = 4
            self.ySize = 4
            self.var_size = 4
        elif len(variables) == 3:
            self.xSize = 2
            self.ySize = 4
            self.var_size = 3
        elif len(variables) == 2:
            self.xSize = 2
            self.ySize = 2
            self.var_size = 2

        self.included_table = [[False] * self.ySize for i in range(self.xSize)]
        self.table_vars = [[1] * self.ySize for i in range(self.xSize)]
        self.table = [[False] * self.ySize for i in range(self.xSize)]

        self.setup_tables(table)

    def setup_tables(self, table):
        for row in table:
            x, y = 0, 0
            if self.var_size == 4:
                x_str = str(int(row[0])) + str(int(row[1]))
                y_str = str(int(row[2])) + str(int(row[3]))
                x, y = self.to_coord(x_str), self.to_coord(y_str)

            if self.var_size == 3:
                x_str = str(int(row[0]))
                y_str = str(int(row[1])) + str(int(row[2]))
                x, y = self.to_coord(x_str), self.to_coord(y_str)

            if self.var_size == 2:
                x_str = str(int(row[0]))
                y_str = str(int(row[1]))
                x, y = self.to_coord(x_str), self.to_coord(y_str)

            self.table[x][y] = row[-1]
            variables = [
                Variable(row[ind], var) for ind, var in enumerate(self.variables)
            ]
            self.table_vars[x][y] = variables

    def print_table(self):
        for x in range(len(self.table)):
            for y in range(len(self.table[x])):
                print(f"{self.table[x][y]:<3}", end="")
            print()

    def get_SKNF(self):
        areas_list = self.get_areas(False)

        result_form = []
        for area_type in areas_list:
            for area in area_type:
                form = []
                for i, var in enumerate(area[0]):
                    if all(var == area[j][i] for j in range(len(area))):
                        to_add = var.copy()

                        to_add.positive = not to_add.positive
                        form.append(to_add)

                if form != []:
                    result_form.append(form)

        return full_form_to_str(result_form, "&")

    def get_SDNF(self):
        areas_list = self.get_areas(True)

        result_form = []
        for area_type in areas_list:
            for area in area_type:
                form = []
                for i, var in enumerate(area[0]):
                    if all(var == area[j][i] for j in range(len(area))):
                        to_add = var.copy()

                        form.append(to_add)

                if form != []:
                    result_form.append(form)

        return full_form_to_str(result_form, "|")

    def is_fit(self, area_size):
        return area_size[0] <= self.xSize and area_size[1] <= self.ySize

    def get_areas(self, find_cond):
        areas_list = []
        for area_size in area_sizes:
            if not self.is_fit(area_size):
                continue

            areas = self.find_area(area_size, find_cond)
            if areas != []:
                areas_list.append(areas)
        return areas_list

    def find_area(self, area_size, find_cond):
        area_list = []
        for x in range(len(self.table)):
            for y in range(len(self.table[0])):
                if self.detect_area(x, y, area_size, find_cond):
                    # print(f"found: {x}, {y}")
                    # print(f"Size: {area_size[0]}, {area_size[1]}")
                    area_list.append(self.obtain_area(x, y, area_size))

        return area_list

    def obtain_area(self, x, y, area_size):
        area = []
        for i in range(x, x + area_size[0]):
            for j in range(y, y + area_size[1]):
                self.mark_include(i, j)
                area.append(self.get_vars(i, j))

        # print(area)
        return area

    def mark_include(self, x, y):
        self.included_table[x % self.xSize][y % self.ySize] = True

    def get_vars(self, x, y):
        return self.table_vars[x % self.xSize][y % self.ySize]

    def detect_area(self, x, y, area_size, find_cond):
        at_least_one = False
        for i in range(x, x + area_size[0]):
            for j in range(y, y + area_size[1]):
                if self.is_true(i, j) != find_cond:
                    return False

                if not self.is_included(i, j):
                    at_least_one = True

        return at_least_one

    def is_true(self, x, y):
        return self.table[x % self.xSize][y % self.ySize]

    def is_included(self, x, y):
        return self.included_table[x % self.xSize][y % self.ySize]

    def to_coord(self, table_part: str):
        if table_part == "10":
            return 3
        if table_part == "11":
            return 2

        return int(table_part, 2)
