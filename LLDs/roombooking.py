from typing import List

class RoomBooking:
    def __init__(self, roomsIds: List[str]) -> None:
        self.rooms_dict = {}
        for r in roomsIds:
            self.rooms_dict[r] = {
                "id": r,
                'meetings': []
            }
        self.meeting_to_room = {}

        self.rooms_ids = sorted(roomsIds)


    def bookMeeting(self, meetingId: str, startTime: int, endTime: int):

        for r_id in self.rooms_ids:
            is_available = True
            r = self.rooms_dict[r_id]
            for meeting in r['meetings']:
                if startTime <= meeting['endTime'] and meeting['startTime'] <= endTime:
                    is_available = False
                    break

            if is_available:
                r['meetings'].append({
                        'id': meetingId,
                        'startTime': startTime,
                        'endTime': endTime
                    })
                self.meeting_to_room[meetingId] = r['id']
                return r['id']


        return ''

    def cancelMeeting(self, meetingId: str):
        if meetingId not in self.meeting_to_room:
            return False

        roomId = self.meeting_to_room[meetingId]

        for i, meeting in enumerate(self.rooms_dict[roomId]['meetings']):
            if meeting['id'] == meetingId:
                self.rooms_dict[roomId]['meetings'].pop(i)
                return True


rb = RoomBooking(["roomA", "roomB"])

print(f"Teste 1.1 (m1): {rb.bookMeeting('m1', 10, 20)}")   # Esperado: "roomA"
print(f"Teste 1.2 (m2): {rb.bookMeeting('m2', 15, 25)}")   # Esperado: "roomB"
print(f"Teste 1.3 (m3): {rb.bookMeeting('m3', 20, 30)}")   # Esperado: ""
print(f"Teste 1.4 (Cancel m1): {rb.cancelMeeting('m1')}")  # Esperado: True
print(f"Teste 1.5 (m4): {rb.bookMeeting('m4', 20, 30)}")   # Esperado: "roomA"
