class Solution(object):
    def largestAltitude(self, gain):

        current_altitude = 0
        highest_altitude = 0

        for i in range(len(gain)):
            current_altitude += gain[i]
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude



        