'''
Created on Dec 19, 2015
@author: Arun Sambargi
This program should be able to take Single Statements
or Multiple Functions or Methods
and then compute time for each
and compare the Results and return the Results
References : 
https://github.com/Karlheinzniebuhr/pythonbenchmark
http://pythoncentral.io/time-a-python-function/
'''
import timeit
import operator

#Decorator function
def measure(method):
    def run(*args, **kwargs):
        runTime = run_time(method,*args, **kwargs)
        print('%r %9.8f MilliSec/pass' % (method.__name__, 1000 * runTime))
    return run

#Decorator Pattern for Wrapping Function Calls  
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

#Runtime Function
def run_time(method,*args, **kwargs):
    wrappedFunc = wrapper(method, *args, **kwargs)
    runTime = timeit.timeit(wrappedFunc,number=1)
    return runTime #Return the Results in Milli Secs

def compareInternal(times_average,func_list, *args, **kwargs):
    
    if len(func_list) == 0:
        return
    
    totalTime = dict()
    
    for i in range(times_average):
        
        for func in func_list:
            
            if str(func.__name__) not in totalTime:
                totalTime[str(func.__name__)] = float(0)
            
            totalTime[str(func.__name__)] = totalTime[str(func.__name__)] + run_time(func,*args, **kwargs)
            
    for func in func_list:
        
        totalTime[str(func.__name__)] = 1000 * totalTime[str(func.__name__)]/times_average
    
    for key in sorted(totalTime, key=operator.itemgetter(1)):
        print("Result: "+ key + " Time Take is "+ "%9.8f MilliSec/pass" % (totalTime[key]) )
    
    
def calcSumMaxMin(lss,lsm,lsn,te):
    print(te)
    return sum(lss), max(lsm), min(lsn)

def calcSumMaxMin2(lss,lsm,lsn,te):
    print('DD')

@measure    
def calcSumMaxMinDeco(lss,lsm,lsn,te):
    print('DD')
        
    return sum(lss), max(lsm), min(lsn)
        
        
if __name__=='__main__':

    ks = dict()
    ks['lss'] = list(i for i in range(100))
    ks['lsm'] = list(i for i in range(100))
    ks['lsn'] = list(i for i in range(100))
    ks['te']  = 'AS'
    
    func_list = list()
    func_list.append(calcSumMaxMin)
    func_list.append(calcSumMaxMin2)
 
    lss = list(i for i in range(100))
    lsm = list(i for i in range(100))
    lsn = list(i for i in range(100))
    te  = 'AS'
        
    compareInternal(10,func_list, lss,lsm,lsn, te)
    compareInternal(10,func_list, **ks)
    
    print('-'*80)
    
    calcSumMaxMinDeco(lss,lsm,lsn,te)