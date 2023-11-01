class Solution:
    def compress(chars):
        ccomp = []
        previous = chars[0]
        count = 0
        # Remember when using enumerate you must cast it to a list otherwise its a subscript error.
        charsEnum = list(enumerate(chars))

        # Add first element to list
        ccomp.append(previous)
        for i, c in charsEnum:
            # Initial case
            if (i == 0):
                count += 1
                continue
            # End case
            if ((i == charsEnum[-1][0]) and (c == previous)):
                count += 1
                if (count > 1 and count < 10):
                    ccomp.append(str(count))
                    break
                if (count > 10):
                    sNumber = str(count)
                    for n in sNumber:
                        ccomp.append(n)
                    break
            elif ((i == charsEnum[-1][0]) and (c != previous)):
                # Append the older value
                if (count > 1 and count < 10):
                    ccomp.append(str(count))
                if (count > 10):
                    sNumber = str(count)
                    for n in sNumber:
                        ccomp.append(n)
                # Append Current value
                ccomp.append(c)
                break

            # Loop through all elements and keep track of replicas
            if c == previous:
                count += 1
                continue
            else:
                previous = c
                if (count > 1 and count < 10):
                    ccomp.append(str(count))
                if (count > 10):
                    sNumber = str(count)
                    for n in sNumber:
                        ccomp.append(n)

                count = 1 
                ccomp.append(c)

        print(ccomp)
        answer = len(ccomp)

        return answer
            


chars = ["a","a","b","b","c","c","c"]
answer = Solution
print("The given compressed list len from given char list is: ", answer.compress(chars))


chars2 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
answer1 = Solution
print("The given compressed list len from given char list is: ", answer1.compress(chars2))

chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b", "b", "a"]
answer2 = Solution
print("The given compressed list len from given char list is: ", answer1.compress(chars3))