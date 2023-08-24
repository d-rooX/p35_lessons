# def __getitem__(self, index):
#     if not isinstance(index, int):
#         raise IndexError(f"Indexes are ints, not {type(index)}")
#
#     current = self.head
#     current_index = 0
#     while current_index != index:
#         current = current.next
#         if current is None:
#             raise IndexError("Out of range")
#         current_index += 1
#     return current.data
