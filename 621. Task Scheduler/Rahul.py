class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:        
        if n == 0:
            return len(tasks)
        
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        
        queue = []
        time = 0
        while counts or queue:
            if queue and queue[0]['wait'] == time:
                elem = queue.pop(0)
                counts[elem['task']] = elem['freq']
            
            if counts:
                task = max(counts, key=lambda t: counts[t])
                freq = counts.pop(task)
                time += 1
                wait = time + n
                
                if freq > 1:
                    queue.append(dict(task=task, freq=freq-1, wait=wait))
            else:
                time += 1

        return time
