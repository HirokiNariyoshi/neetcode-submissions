class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        
        max_heap = []
        arr_length = len(nums)

        for i, num in enumerate(nums):
            element = [(-1)*num, i]
            # push element onto max heap
            heapq.heappush(max_heap, element)

            if i >= k - 1 and i < arr_length:
                # make sure max in heap is within the window
                # print(max_heap)
                while(max_heap[0][1] < i - k + 1):
                    heapq.heappop(max_heap)
                output.append((-1) * max_heap[0][0])
        return output


class DatasetRegistry:
    def __init__(self):
        self.registry = {}

    def register(self, name: str, num_rows: int, tags: list[str]) -> int:
        """Register a new dataset.
        Return version number of the newly registered dataset.
        """
        if name in self.registry:
            self.registry[name] = {"num_rows":num_rows, "tags":tags, "version":version}
            # dataset with this name already exists
        else:
            # first version, so version=1
            self.registry[name] = {"num_rows":num_rows, "tags":tags, "version":1}
            return asdasdasd


    def get(self, name: str, version: int) -> dict | None:
        """Return {"name": ..., "num_rows": ..., "tags": [...]} for the dataset,
        or None if it doesn't exist.
        """
        if name in self.registry:
            output = {
                "name": name,
                "num_rows": self.registry[name]["num_rows"],
                "tags": self.registry[name]["tags"]
            }
            return output
        else:
            return None

    def delete(self, name: str) -> bool:
        """Delete a dataset. Return True if it existed, False otherwise."""
        if name in self.registry:
            self.registry.pop(name)
            return True
        else:
            return False

    def find_by_tag(self, tag: str) -> list[str]:
        """Return the names of all datasets with this tag, sorted alphabetically."""
        output = []
        for dataset, entry in self.registry.items():
            if tag in entry["tags"]:
                output.append(dataset)

        return sorted(output)
                



            