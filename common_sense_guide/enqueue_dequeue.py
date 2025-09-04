# class Queue:
#     def __init__(self):
#         self.data = []

#     def _enqueue(self, element):
#         self.data.append(element)

#     def _dequeue(self):
#         if len(self.data) > 0:
#             return self.data.pop(0)
#         else:
#             return None
        
#     def read(self):
#         if len(self.data) > 0:
#             return self.data[0]
#         else:
#             return None

# Printer queue example
import queue

class PrintManager:
    def __init__(self):
        self.queue = queue.Queue()

    def queue_print_job(self, document):
        self.queue.put(document) #enqueue

    def run(self):
        while not self.queue.empty(): #use empty instead of read()
            self.print_document(self.queue.get())

    def print_document(self, document):
        print(document)


pm = PrintManager()
pm.queue_print_job("Document 1")
pm.queue_print_job("Document 2") 
pm.run()