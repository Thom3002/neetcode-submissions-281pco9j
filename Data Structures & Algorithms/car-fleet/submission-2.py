class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # t = 0
        # 0-car(1) 1-car(2) 2- 3- 4-car(2) 5- 6- 7-car(1) 8- 9- 10-
        # t = 1
        # 0- 1-car(1) 2- 3-car(2) 4- 5- 6-car(2) 7- 8-car(1) 9- 10-
        # t = 2
        # 0- 1- 2-car(1) 3- 4- 5-car(2) 6- 7- 8-car(1) 9-car(1) 10-
        # t = 3
        # 0- 1- 2- 3-car(1) 4- 5- 6- 7-car(2) 8- 9-car(1) 10-car(1)
        # t = 4
        # 0- 1- 2- 3- 4-car(1) 5- 6- 7- 8- 9-car(2) 10-car(1)  

        # car pos 4 
        # target - pos * speed = 
        #  pos + (speed) * t = target
        # 4 + (2) * t = 10
        # 4 + 2t = 10
        # 2t = 6
        # t = 3
        # t = (target - pos) / speed
        # se um carro que está na frente tiver um t > do que um carro que está atras então isso é um fleet 
        # 0. criar um array auxiliar que guarda a pos_ini e a speed
        # 1. ordenar o array por pos_ini 
        # 2. calcular o t para chegar ao destino do atual e do anterior (fila)
        # 3. se t anterior >= t atual, então fleet_cout += 1. Pop em ambos
        if not position:
            return 0
        fleet_count = 1
        stack = [None] * len(position)
        for i in range(len(position)):
            stack[i] = (position[i], speed[i])
        
        def get_t(target, pos, speed):
            return (target - pos) / speed
        
        stack.sort(key= lambda x: x[0])
        # [(0, 1), (1, 2), (4, 2), (7, 1)]
        # t = 10 - 7 / 1 = 3
        last_pos, last_speed = stack.pop()
        last_t = get_t(target, last_pos, last_speed)
        while stack:
            curr_pos, curr_speed = stack.pop()
            curr_t = get_t(target, curr_pos, curr_speed)
            if curr_t <= last_t:
                continue
            else:
                fleet_count += 1
                last_t = curr_t
        
        return fleet_count

         