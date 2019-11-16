'''
3、线程回顾：
	（1）引入：
		多任务，多个任务同时进行，多进程，多线程
		sublime 录屏 vnc服务器
		word 编辑 检查（多线程）
	（2）创建线程Thread
		面向过程
			创建对象： t = threading.Thread(target=xxx, name=xxx, args=(xx, xx))
			target : 线程启动之后要执行的函数
			name : 线程的名字
			获取线程名称： threading.current_thread().name
			args : 主线程向子线程传递参数
			t.start() 启动线程
			t.join() 让主线程结束
		面向对象
			定义一个类，继承自threading.Thread,重写一个方法run方法，需要线程名字、传递参数、重写构造方法，
			在重写构造方法的时候，一定要注意手动调用父类的构造方法。
		 线程同步：
		 	线程之间共享全局变量，

4. 队列、
	下载线程
	解析线程，通过队列进行交互
	q = Queue(5)
	q.put('xxx')
	q.put(xxx, False) 	队列满就报错
	q.put(xxx, True, 3)		等待三秒，再报错

	q.get()		如果队列为空，程序卡在这里
	q.get(False)	队列为空时报错
	q.get(False, 3)		等待3秒队列报错

	q.empty()   队列的判空
	q.full()    队列的判满
	q.qsize()   队列的长度
	
