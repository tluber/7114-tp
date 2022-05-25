import numpy as np


class Bank:
    def __init__(self, id, dem, x, y):
        self.id = id
        self.dem = dem
        self.coord = (x, y)

    def get_id(self):
        return self.id

    def get_demand(self):
        return self.dem

    def get_coord(self):
        return self.coord


class Truck:
    def __init__(self, capacity):
        self.load = 0
        self.position = (0, 0)
        self.banks = []
        self.capacity = capacity
        self.distance_traveled = 0

    def set_load(self, amount):
        self.load += amount

    def get_load(self):
        return self.load

    def get_capacity(self):
        return self.capacity

    def get_position(self):
        return self.position

    def set_position(self, coord):
        self.position = coord

    def visit_bank(self, bank):
        self.banks.append(bank)

    def get_visited_banks(self):
        return self.banks

    def add_distance(self, distance):
        self.distance_traveled += distance

    def get_distance_traveled(self):
        return self.distance_traveled


filename = 'problema_dos.txt'


def get_banks():
    with open(filename) as f:
        lines = f.readlines()

        m_banks = []

        dem_start_index = lines.index("DEMANDAS\n") + 1
        dem_end_index = lines.index("FIN DEMANDAS\n")
        dem = lines[dem_start_index:dem_end_index]

        coord_start_index = lines.index("NODE_COORD_SECTION\n") + 1
        coord_end_index = lines.index("EOF")
        coords = lines[coord_start_index:coord_end_index]

        for i in range(get_dimension()):
            d = int(dem[i].split(" ")[1])
            x = float(coords[i].split(" ")[1])
            y = float(coords[i].split(" ")[2])
            m_banks.append(Bank(i + 1, d, x, y))

    return m_banks


def get_distance(coord1, coord2):
    a = np.array(coord1)
    b = np.array(coord2)
    return np.linalg.norm(a - b)


def get_capacity():
    with open(filename) as f:
        lines = f.readlines()
        capacity = [s for s in lines if "CAPACIDAD" in s].pop().split(": ")

    return int(capacity[1])


def get_dimension():
    with open(filename) as f:
        lines = f.readlines()
        dimen = [s for s in lines if "DIMENSION" in s].pop().split(": ")

    return int(dimen[1])


def get_min_dist_banks(m_truck, m_banks):
    def take_second(elem):
        return elem[1]

    dist = []
    for bank in m_banks:
        d = get_distance(m_truck.get_position(), bank.get_coord())
        dist.append((bank.get_id(), d))

    dist.sort(key=take_second)

    return dist


def is_available_for_pick_up(m_truck, m_results, m_bank):
    if m_bank in m_results:
        return False

    balance = m_truck.get_load() + m_bank.get_demand()
    if 0 <= balance <= m_truck.get_capacity():
        return True
    else:
        return False


banks = get_banks()
dimension = get_dimension()
max_capacity = get_capacity()

truck = Truck(max_capacity)

results = []

while len(results) < dimension:
    min_len_banks = get_min_dist_banks(truck, banks)
    for min_len_bank in min_len_banks:
        bank = list(filter(lambda b: b.get_id() == min_len_bank[0], banks))[0]
        if is_available_for_pick_up(truck, results, bank):
            truck.add_distance(min_len_bank[1])
            truck.set_load(bank.get_demand())
            truck.set_position(bank.get_coord())
            results.append(bank)
            break

f = open("results.txt", "w+")
for res in results:
    f.write("%d " % (res.get_id()))
print("TOTAL DISTANCE:", truck.get_distance_traveled())
