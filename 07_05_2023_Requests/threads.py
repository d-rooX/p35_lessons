import threading

def foo(result_dict):
    time.sleep(1)
    result_dict['result'] = 2 + 2
    print(result_dict is d)
    result_dict = {}
    print(result_dict is d)


d = {}

t = threading.Thread(target=foo, args=(d,))
t.start()
t.join()

print(d)
