class Solution:
    def maximumTime(self, time: str) -> str:
        if "?" not in time:
            return time
        else:
            time_array = [char for char in time]
            if time_array[0] == '?' and time_array[1] == '?':
                time_array[0] = '2'
                time_array[1] = '3'

            # first position
            if time_array[0] == '?' and time_array[1] != '?' and int(time_array[1]) < 4:
                time_array[0] = '2'
            elif time_array[0] == '?':
                time_array[0] = '1'

            # second position
            if time_array[0] == '2' and time_array[1] == '?':
                time_array[1] = '3'
            elif time_array[1] == '?' and (time_array[0] == '1' or time_array[0] == '0'):
                time_array[1] = '9'

            # third position
            if time_array[3] == '?':
                time_array[3] = '5'

            # fourth position
            if time_array[4] == '?':
                time_array[4] = '9'

        return ''.join(time_array)
