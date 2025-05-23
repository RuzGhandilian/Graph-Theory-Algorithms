# Problem 5: Jump Game II

def jump_game_ii(nums):
    jumps = 0
    end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        # find the farthest we can go
        farthest = max(farthest, i + nums[i])
        # if we reach end of current jump range
        if i == end:
            jumps += 1
            end = farthest

    return jumps
