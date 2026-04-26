# Vehicle type = 2 moto
# type = 4 carro

class ParkingLot:
    def __init__(self, helper, parking) -> None:
        self.parking = parking
        self.is_available = {}
        self.free_spots_per_floor = []
        self.memory = {}

        for i, floor in enumerate(self.parking):
            self.free_spots_per_floor.append({
                2: 0,
                4: 0
            })
            for j, row in enumerate(floor):
                for k, column in enumerate(row):
                    if parking[i][j][k] == 2:
                        self.free_spots_per_floor[i][2] += 1
                        self.is_available[(i, j, k)] = True
                    elif parking[i][j][k] == 4:
                        self.free_spots_per_floor[i][4] += 1
                        self.is_available[(i, j, k)] = True
                    else:
                        self.is_available[(i, j, k)] = False


        return

    def park(self, vehicleType, vehicleNumber, ticketId, parkingStrategy):
        '''
        This function assigns an empty parking spot to vehicle and maps vehicleNumber and ticketId to the assigned spotId

        - parkingStrategy has two values, 0 and 1
        parkingStrategy = 0
        - Get the parking spot at lowest index i.e. lowest floor, row and column

        parkingStrategy = 1 :
        - Get the floor with maximum number of free spots for the given vehicle type.
        '''
        spotId = 0 # floor+"-"+row+"-"+column
        floor_idx, row_idx, col_idx = self._get_next_available_parking_spot(parkingStrategy, vehicleType)
        if floor_idx == -1:
            return "No available spots"

        # update values
        self._update_values(floor_idx, row_idx, col_idx, vehicleType, remove=False)

        spotId = str(floor_idx)+'-'+str(row_idx)+'-'+str(col_idx)
        self.memory[vehicleNumber] = spotId
        self.memory[ticketId] = spotId
        return spotId

    def _get_next_available_parking_spot(self, parkingStrategy, vehicleType):

        if parkingStrategy == 0:
            for i, floor in enumerate(self.parking):
                for j, row in enumerate(floor):
                    for k, column in enumerate(row):
                        if self.is_available[(i, j , k)] and self.parking[i][j][k] == vehicleType:
                            return i, j, k
        else:
            # Parking Strategy == 1:
            max_free_spots = 0
            max_free_spots_floor_idx = 0
            for i, floor in enumerate(self.free_spots_per_floor):
                if floor[vehicleType] > max_free_spots:
                    max_free_spots = floor[vehicleType]
                    max_free_spots_floor_idx = i

            i = max_free_spots_floor_idx
            for j, row in enumerate(self.parking[max_free_spots_floor_idx]):
                for k, column in enumerate(row):
                    if self.is_available[(i, j , k)] and self.parking[i][j][k] == vehicleType:
                            return i, j, k

        return -1, -1, -1

    def _update_values(self, floor_idx, row_idx, col_idx, vehicleType, remove=False):
        if remove:
            self.is_available[(floor_idx, row_idx, col_idx)] = True
            self.free_spots_per_floor[floor_idx][vehicleType] += 1
        else:
            # park a new car
            self.is_available[(floor_idx, row_idx, col_idx)] = False
            self.free_spots_per_floor[floor_idx][vehicleType] -= 1



    def removeVehicle(self, spotId):
        '''
        - Unparks or removes vehicle from parking spot.
        - returns true if vehicle is removed
        - returns false if vehicle not found or any other error
        '''
        # parse spotId
        spotId = spotId.split('-')
        spotId_idx = []
        for id in spotId:
            spotId_idx.append(int(id))

        floor, row, col = spotId_idx[0], spotId_idx[1], spotId_idx[2]
        if self.is_available[(floor, row, col)]:
            return False

        self._update_values(floor, row, col, self.parking[floor][row][col], remove=True)
        return True

    def searchVehicle(self, query):
        '''
        - searches the latest parking details of a vehicle parked in previous park() method calls.
        - returns spotId e.g. 2-0-15 or empty string ""
        - Query will be either vehicleNumber or ticketId.
        '''
        if query in self.memory:
            return self.memory[query]
        else:
            return ''

    def getFreeSpotsCount(self, floor, vehicleType):
        '''
        - At any point of time get the number of free spots of vehicle type (2 or 4 wheeler).
        '''
        return self.free_spots_per_floor[floor][vehicleType]


class Helper:
    def __init__(self) -> None:
        return

    def print(self) -> None:
        return


# Casos de teste do enunciado

parking = [[
    [4, 4, 2, 2],
    [2, 4, 2, 0],
    [0, 2, 2, 2],
    [4, 4, 4, 0]
]]

pl = ParkingLot(Helper(), parking)

spot = pl.park(2, "bh234", "tkt4534", 0)
print("spot:", spot)  # esperado: 0-0-2

print("search bh234:", pl.searchVehicle("bh234"))   # esperado: 0-0-2
print("search tkt4534:", pl.searchVehicle("tkt4534"))  # esperado: 0-0-2

print("free 2-wheeler:", pl.getFreeSpotsCount(0, 2))  # esperado: 6

print("remove:", pl.removeVehicle("0-0-2"))  # esperado: True

print("free 2-wheeler after:", pl.getFreeSpotsCount(0, 2))  # esperado: 7
