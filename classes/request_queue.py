from queue import Queue

class Request_Queue(Queue):
    added_request_number = 0
    
    @classmethod
    def update_added_request_number(cls):
        cls.added_request_number += 1
        return cls.added_request_number

    def generate_request(self):
        added_number = Request_Queue.update_added_request_number()
        new_element = QueueElement(added_number)
        self.put(new_element)
        print(f'Request {new_element.request_number} added')
    
    def process_request(self):
        get_element = self.get()
        print(f'Request {get_element.request_number} processed')


class QueueElement:
    def __init__(self, request_number):
        self.request_number = request_number