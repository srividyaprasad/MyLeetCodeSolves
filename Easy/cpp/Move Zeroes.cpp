#include <vector>
class Solution {
public:

    void moveZeroes(vector<int>& nums) {

        int length = size(nums);
        vector<int>::iterator i =nums.begin();
        int count = 0;
        while(i!= nums.end()){
            if(*i == 0){
                nums.erase(i);
                count+=1;
            }
            else{
                i+=1;
            }
        }
        for(int i=0; i<count; i++){
            nums.push_back(0);
        }
    }
};
