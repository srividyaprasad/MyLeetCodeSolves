class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len=size(nums);
        int ret=0;
        for(int i=0; i<len && target>nums[i]; i++)
        {
            ret=i+1;
        }
        return ret;
}
};
