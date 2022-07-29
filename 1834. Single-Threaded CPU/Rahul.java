class Solution {
    class Task {        
        int taskId;
        int enqueueTime;
        int beginTime;
        int processingTime;
        
        Task(int taskId, int enqueueTime, int processingTime) {
            this.taskId = taskId;
            this.enqueueTime = enqueueTime;
            this.processingTime = processingTime;
        }
    }
    
    public int[] getOrder(int[][] tasks) {
        int nextTaskId = 0;
        Queue<Task> taskQueue = new PriorityQueue<>((t1, t2) -> Integer.compare(t1.enqueueTime, t2.enqueueTime));    
        for (int[] task : tasks) {
            taskQueue.offer(new Task(nextTaskId++, task[0], task[1]));
        }
        
        int[] order = new int[taskQueue.size()];
        int orderIndex = 0;
        
        Queue<Task> schedulerQueue = new PriorityQueue<>((t1, t2) -> (t1.processingTime == t2.processingTime) ? Integer.compare(t1.taskId, t2.taskId) : Integer.compare(t1.processingTime, t2.processingTime));
        
        if (!taskQueue.isEmpty()) {
            int currentTime = taskQueue.peek().enqueueTime;
            Task currentTask = null;
            while (!schedulerQueue.isEmpty() || !taskQueue.isEmpty()) {              
                while (!taskQueue.isEmpty() && taskQueue.peek().enqueueTime <= currentTime) {
                    schedulerQueue.offer(taskQueue.poll());
                }

                if (currentTask == null) {
                    currentTask = schedulerQueue.poll();
                } else if (currentTask.beginTime + currentTask.processingTime >= currentTime) {
                    currentTask = null;
                }

                if (currentTask != null) {
                    order[orderIndex++] = currentTask.taskId;
                    currentTask.beginTime = currentTime;   
                    currentTime += currentTask.processingTime;
                } else if (schedulerQueue.isEmpty() && !taskQueue.isEmpty()) {
                    currentTime = taskQueue.peek().enqueueTime;
                }
            }
        }
        
        return order;
    }
}
