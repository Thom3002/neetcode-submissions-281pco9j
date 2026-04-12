class TrainPlatformManager:
    # rules:
    # 1. i.e. if train A departs from platform p at time t,
    # then another train B can't arrive at platform p before time t+1
    # if multiple platforms have minimum wait time, choose the one with lowest index.
    # you must assign a platform with lowest wait time.
    # departureTime = arrivalTime + waitTime - 1 + delay

    # platforms = {'platform_id': Platform}


    # trem 1) chega na P01 em t = 1, waitTime = 2, dep = 2. next_free_time = 3
    # trem 2) pega o next_free_time, e calcula o delay. ex: t = 2, waitTime = 0. ent dep = 2. 3 - 2 = 1 é o delay

    # 1. percorrer as platforms pegando o next_free_time e calculando o delay. Achou o menor delay escolhe ela, se empatar escolhe a com menor id
    #
    class Platform():

        #
        def __init__(self, platformNum) -> None:
            self.num = platformNum
            self.next_free_time = 0
            self.trains = {}
            # '(arr, dep) '

        def get_next_free_time(self) -> int:
            return self.next_free_time

        def set_train(self, trainId, arr, wait, delay) -> None:
            dep_time = arr + wait - 1 + delay
            self.next_free_time = dep_time + 1
            self.trains[(arr, dep_time)] = trainId

        def get_train_from_timestamp(self, timestamp) -> str:
            if self.trains:
                for arr, dep in self.trains:
                    if timestamp in range(arr, dep + 1):
                        return self.trains[(arr, dep)]
            return ''


    class Train():
        def __init__(self, trainId) -> None:
            self.id = trainId
            self.platform = None
            self.arr = None
            self.dep = None

        def set_platform(self, plat_num, arr, wait, delay):
            self.platform = plat_num
            self.arr = arr
            self.dep = arr + wait - 1 + delay

        def get_platform_from_timestamp(self, timestamp):
            if timestamp in range(self.arr, self.dep + 1):
                return self.platform
            return -1



    def __init__(self, platformCount: int) -> None:
        self.platforms = {}
        self.trains = {}
        for i in range(platformCount):
            self.platforms[i] = self.Platform(i)
        pass

    def assignPlatform(self, trainId: str, arrivalTime: int, waitTime: int) -> str: # O(n log n)
        train = self.Train(trainId)
        delays = []
        for platform in self.platforms:
            nxt_free_t = self.platforms[platform].get_next_free_time()
            delays.append((self._get_delay(arrivalTime, nxt_free_t), self.platforms[platform].num)) # (delay, platNum)

        delays = sorted(delays)
        chosen_platform_num = delays[0][1]
        delay = delays[0][0]
        self.platforms[chosen_platform_num].set_train(trainId, arrivalTime, waitTime, delay)
        train.set_platform(chosen_platform_num, arrivalTime, waitTime, delay)
        self.trains[train.id] = train

        res = str(chosen_platform_num) + ',' + str(delay)
        return res


    def getTrainAtPlatform(self, platformNumber: int, timestamp: int) -> str:
        if platformNumber in self.platforms:
            platform = self.platforms[platformNumber]
            return platform.get_train_from_timestamp(timestamp)

        return ""

    def getPlatformOfTrain(self, trainId: str, timestamp: int) -> int:
        if trainId in self.trains:
            train = self.trains[trainId]
            return train.get_platform_from_timestamp(timestamp)
        return -1


    def _get_delay(self, arr: int, next_free_time: int) -> int:
            delay = next_free_time - arr
            if delay <= 0:
                return 0
            return delay

# Inicialização das plataformas
mgr = TrainPlatformManager(3)

print("--- 1) Primeiras Chegadas ---")
# T1: Chega 0, espera 5. Ocupa [0, 4]. Libera em 5.
res1 = mgr.assignPlatform("T1", 0, 5)
print(f"T1: {res1}")  # Esperado: "0,0"

# T2: Chega 2, espera 3. P0 ocupada até 4. P1 livre. Ocupa [2, 4]. Libera em 5.
res2 = mgr.assignPlatform("T2", 2, 3)
print(f"T2: {res2}")  # Esperado: "1,0"

# T3: Chega 4, espera 4. P0 e P1 ocupadas até 4. P2 livre. Ocupa [4, 7]. Libera em 8.
res3 = mgr.assignPlatform("T3", 4, 4)
print(f"T3: {res3}")  # Esperado: "2,0"


print("\n--- 2) Passagem de bastão (Handoff) ---")
# T4: Chega 5. P0 liberou em 5. Sem delay. Ocupa [5, 9]. Libera em 10.
res4 = mgr.assignPlatform("T4", 5, 5)
print(f"T4: {res4}")  # Esperado: "0,0"


print("\n--- 3) Empate no tempo livre futuro ---")
# T5: Chega 9. P0 busy até 9. P1 livre desde 5. P2 livre desde 8. Menor index: P1. Ocupa [9, 9]. Libera 10.
res5 = mgr.assignPlatform("T5", 9, 1)
print(f"T5: {res5}")  # Esperado: "1,0"

# T6: Chega 9. P1 agora busy [9,9]. P0 busy [5,9]. P2 livre desde 8. Sem delay. Ocupa [9, 10]. Libera 11.
res6 = mgr.assignPlatform("T6", 9, 2)
print(f"T6: {res6}")  # Esperado: "2,0"


print("\n--- 4) Atribuição com Delay e Desempate ---")
# T7: Chega 9.
# P0 libera em 10 (delay 1), P1 libera em 10 (delay 1), P2 libera em 11 (delay 2).
# Menor delay: 1. Empate P0 e P1 -> Escolhe P0. Inicia em 10. Ocupa [10, 12].
res7 = mgr.assignPlatform("T7", 9, 3)
print(f"T7: {res7}")  # Esperado: "0,1"


print("\n--- Consultas por Timestamp (Plataforma) ---")
print(f"P0 em t=4:  {mgr.getTrainAtPlatform(0, 4)}")   # Esperado: "T1"
print(f"P0 em t=5:  {mgr.getTrainAtPlatform(0, 5)}")   # Esperado: "T4"
print(f"P1 em t=9:  {mgr.getTrainAtPlatform(1, 9)}")   # Esperado: "T5"
print(f"P2 em t=10: {mgr.getTrainAtPlatform(2, 10)}")  # Esperado: "T6"
print(f"P0 em t=10: {mgr.getTrainAtPlatform(0, 10)}")  # Esperado: "T7"


print("\n--- Consultas por Trem (Pode variar se sua plataforma é 0 ou 1-based) ---")
# Nota: O enunciado diz que retorna o número da plataforma (1..platformCount) ou -1.
# Verifique se no seu código você retorna 0 ou 1 para a P0.
print(f"T7 em t=9:  {mgr.getPlatformOfTrain('T7', 9)}")   # Esperado: -1
print(f"T7 em t=10: {mgr.getPlatformOfTrain('T7', 10)}")  # Esperado: 0 (ou 1 se for 1-based)
print(f"T5 em t=10: {mgr.getPlatformOfTrain('T5', 10)}")  # Esperado: -1
print(f"T6 em t=11: {mgr.getPlatformOfTrain('T6', 11)}")  # Esperado: -1
