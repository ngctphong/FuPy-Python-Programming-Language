import time

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_stop_time = time.time() - gen_start_time
print(gen_stop_time)