"""Find miniumum for all the subarray of len M for an array with length M
    where N < M
"""
from typing import List
from min_stack_que import MinQueueOne


def get_subarray_min(arr: List[int], window_size: int):
    """Method to get min for each subarray for a fixed window of size m
    """
    que = MinQueueOne()
    res = []
    for i in range(window_size):
        que.push(arr[i])

    for idx in range(window_size, len(arr)):
        res.append(que.get_min())
        que.remove_element(arr[idx-window_size])
        que.push(arr[idx])
    return res


if __name__=="__main__":
    result = get_subarray_min(list(range(1, 11, 1)), window_size=2)
    print(result)
