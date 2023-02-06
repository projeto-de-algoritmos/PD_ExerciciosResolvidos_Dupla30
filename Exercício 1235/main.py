import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tasks = list(zip(startTime,endTime ,profit ))
        tasks.sort(key=lambda x:x[0])
        n = len(tasks)
        
        start = [tasks[i][0] for i in range(n) ]
        total = [0 for _ in range(n)]
        total[n-1] = tasks[n-1][2]
        
        for i in range(n-2,-1,-1):
            idx = bisect.bisect_left(start, tasks[i][1], i, n)			
            total[i] = max(total[i+1], tasks[i][2]+ (total[idx] if idx < n else 0) )
        
        return total[0]