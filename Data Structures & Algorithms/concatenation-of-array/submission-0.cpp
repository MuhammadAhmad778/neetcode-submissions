class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int counter = 0;
        vector<int> ans(nums.size()*2);

        for (int i = 0;i < nums.size();i++, counter++)
        {
            ans[i] = nums[i];
        }

		for (int i = 0;i < nums.size();i++, counter++)
		{
			ans[counter] = nums[i];
		}
       

        return ans;
    }
};