class Solution:
    def buildArray(target, n):
        stream = []
        sstack = []
        track = []
        for i in range(n):
            stream.append(i+1)

        if (len(track) == 0):
            track.append(stream[0])
            sstack.append("PUSH")
            
        
        while (len(stream) != 0):
            for n in range(1, (len(stream))):
                track.append(stream[n])
                sstack.append("PUSH")

                if (track == target):
                    return sstack

                if (len(track) > 0):
                    track.pop()
                    sstack.append("POP")

target = [1,3]
n = 3

ans = Solution.buildArray(target, n)

print(ans)

#public:
#    vector<string> buildArray(vector<int>& target, int n) {
#        vector<string> sstack;
#        vector<int> nstack;
#        vector<int> track;
#        for (int i = 0; i < n; i++) {
#            nstack.push_back(i + 1);
#        }

#        if (track.size() == 0) {
#            track.push_back(nstack[0]);
#            sstack.push_back("PUSH");
#        }

#        while (nstack.size() != 0) {
#            for (int i = 1; i < nstack.size(); ++i) {
#                track.push_back(nstack[i]);
#                sstack.push_back("PUSH");
#                if (track == target) {
#                    return sstack;
#                }
#                if (track.size() > 0) {
#                    track.pop_back();
#                    sstack.push_back("POP");
#                }
                

#            }

#        }
        
#    }
#};