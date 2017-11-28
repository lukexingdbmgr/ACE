{1, 1, 1, 3}
k = 2

## check if the array can be separated into k equal groups

def search(groups, nums):
    if not nums: return True
    v = nums.pop()
    # v = 1
    for i, group in enumerate(groups):
        i = 0
        if group + v <= target:
            groups[i] += v
            if search(groups): return True

            groups[i] -= v
        if not group: break
    nums.append(v)
    return False

'''
def search(groups, nums):
    if not nums: return True
    v = nums.pop()
    # v = 1
    for i, group in enumerate(groups):
        i = 0
        if group + v <= target:
            ## target = 3
            groups[i] += v
            ## group = [0, 0]
            ## group = [1, 0]
            if search(groups): return True

            ##################################################
            def search(groups, nums):
                ## group = [1, 0]
                ## nums = [1,1,3]
                if not nums: return True
                v = nums.pop()
                # v = 1
                # nums = [1, 3]
                for i, group in enumerate(groups):
                    i = 0
                    if group + v <= target:
                        groups[i] += v
                        ## group = [1, 0] ->
                        ## group = [2, 0]
                        if search(groups): return True

                        ###############################################return
                        def search(groups, nums):
                            ## group = [2, 0]
                            ## nums = [1, 3]
                            if not nums: return True
                            v = nums.pop()
                            # v = 1
                            # nums = [3]
                            for i, group in enumerate(groups):
                                i = 0
                                # group = 2
                                if group + v <= target:
                                    groups[i] += v
                                    # groups = {3, 0}
                                    if search(groups): return True

                                    ############################################return


                                    def search(groups, nums):
                                        if not nums: return True
                                        v = nums.pop()
                                        # v = 3
                                        # nums = []
                                        for i, group in enumerate(groups):
                                            i = 0
                                            # groups = [3, 0]
                                            # i = 1
                                            # group = 0
                                            if group + v <= target:
                                                groups[i] += v
                                                # groups = {3, 3}
                                                if search(groups): return True

                                                ######################################### rreturn
                                                def search(groups, nums):
                                                    if not nums: return True
                                                    return True

                                                groups[i] -= v
                                            if not group: break
                                        nums.append(v)
                                        return False

                                    groups[i] -= v
                                if not group: break
                            nums.append(v)
                            return False

                    groups[i] -= v
                if not group: break

            nums.append(v)
            return False

    groups[i] -= v

'''
