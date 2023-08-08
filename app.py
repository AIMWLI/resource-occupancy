import argparse
import time
from multiprocessing import Process
from multiprocessing import cpu_count


def exec_func(bt):
    while True:
        for i in range(0, 9600000):
            pass
        time.sleep(bt)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='runing')

    parse.add_argument(
        "-c",
        "--count",
        default=cpu_count(),
        help='cpu count'
    )
    parse.add_argument(
        "-t",
        "--time",
        default=0.01,
        help='cpu time'
    )
    parse.add_argument(
        "-m",
        "--memory",
        default=1,
        help='memory'
    )

    args = parse.parse_args()

    cpu_logical_count = int(args.count)
    cpu_sleep_time = args.time
    memory_used_gb = int(args.memory)

    try:
        cpu_sleep_time = int(args.time)
    except ValueError:
        try:
            cpu_sleep_time = float(args.time)
        except ValueError as ex:
            raise ValueError(ex)

    _doc = """
    python runing.py -c 2 -t 0.01 -m 1
    -c 指定cpu核数，不加-c参数默认为当前cpu最大核数
    -t cpu运算频率时间间隔，越小占用越高
    -m 内存占用，最低单位GB，当为0时不占用内存

     CPU使用率需要手动增加减少-t参数来达到预期使用率。
     """

    # print("\n====================使用说明=========================")
    # print("{0}".format(_doc))
    # print("\n====================================================")
    print('\ncpu count:{0}'.format(cpu_logical_count))
    print('\nmemory:{0}GB'.format(memory_used_gb))
    print('\nModel in training.......')

    try:
        # 内存占用
        for i in range(memory_used_gb):
            locals()['A' + str(i)] = ' ' * (1 * 1024 * 1024 * 1024)
    except MemoryError:
        print("剩余内存不足，内存有溢出......")

    try:
        ps_list = []

        for i in range(0, cpu_logical_count):
            ps_list.append(Process(target=exec_func, args=(cpu_sleep_time,)))

        for p in ps_list:
            p.start()

        for p in ps_list:
            p.join()
    except KeyboardInterrupt:
        print("资源浪费结束!")
