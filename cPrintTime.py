import time


class cPrintTime:
    m_startTime = time.time()
    m_endTime = time.time()
    def __init__(self):
        # 생성자 구현
        pass
    def startTime(self, p_stime):
        cPrintTime.m_startTime = p_stime
        print(f"start time:{cPrintTime.m_startTime} sec")
    def endTime(self, p_endstime):
        cPrintTime.m_endTime = p_endstime
        print(f"start ~ end time: [{cPrintTime.m_startTime}] ~ [{cPrintTime.m_endTime}] sec")
        print(f"elapse time: ", cPrintTime.m_endTime - cPrintTime.m_startTime)