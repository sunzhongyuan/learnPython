import time as t

class MyTimer():
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.rstMsg = '未开始计时'
        self.result = []
        self.type = ['年','个月','天','小时','分钟','秒']

    def __str__(self):
        return self.rstMsg

    __repr__ = __str__


    def __add__(self,other):
        rstMsg = '总共运行了'
        result = []
        for each in range(6):
            result.append(self.result[each]+other.result[each])
            if result[each]:
                rstMsg += str(result[each])+self.type[each]
        print(rstMsg)
    
    def start(self):
        self.rstMsg = '请先调用 stop() 停止计时'
        self.begin = t.localtime()
        print('开始计时...')

    def stop(self):
        if not self.begin:
            print('请先调用 start() 开始计时')
        else:
            self.end = t.localtime()
            self._calc()
            print('计时结束...')
        

        
    def _calc(self):
        self.rstMsg = '共用时'
        for each in range(6):
            self.result.append(self.end[each] - self.begin[each])
            if self.result[each]:
                self.rstMsg += str(self.result[each]) + self.type[each]
        print(self.rstMsg)
        self.begin = 0
        self.end = 0
        

    
