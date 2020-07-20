# 学习笔记

## 多进程

- 创建进程
    - 函数式: Process(target=fun, args=(arg1, arg2, ...))
    - 类：新类继承Process，重写类中的run方法

- 进程间通信
    - 队列（推荐）
    - 管道（队列底层原理）
    - 共享内存

- 锁机制（解决进程间资源抢占）

- 进程池（方便管理大量的子进程）

- 死锁
    - 两个或以上的进程在执行中由于资源竞争或彼此通信而造成阻塞
    - 例：
```
    def f(q):
    q.put('X' * 1000000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()                    # this deadlocks
    obj = queue.get()
```
p子进程把队列queue塞满后会挂起等待queue中的数据被取走，而queue的取出操作在p.join()后面意味着只有p结束后才会运行，p与get()彼此依赖从而造成死锁，将最后两行互换即可解决。

## 多线程

- 创建线程
    - 函数式: 同进程
    - 类：同进程

- 线程间通信
    - 线程之间使用同一块内存，修改变量互相影响
    - 也可通过队列管理
        - 普通队列
        - 优先队列

- 锁机制（解决资源抢占）
    - 普通锁
    - RLock（可嵌套）
    - Condition（条件锁）

- 管理多线程
    - multiprocessing.dummy 的 Pool
    - concurrent.futures 的 ThreadPoolExecutor