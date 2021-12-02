# 0x01. Lockboxes

n number of lockboxes provided.
Each box is numbered sequentially from 0 to n - 1.
Each box may have keys that can open other boxes.
Task:
- Write method to determine if all boxes can be opened

Description:
- Prototype:
```python
def canUnlockAll(boxes)
```
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers (There can be keys that do not have boxes)
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
