package leet_java;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> numIndex = new HashMap<>();

        for(int i=0; i<nums.length; i++)
        {
            int dif=target-nums[i];
            if(numIndex.containsKey(dif))
                return(new int[]{numIndex.get(dif), i});
            else
                numIndex.put(nums[i],i);
        }
        return new int[]{};
    }
}

public class TwoSum {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums={2,7,11,15};
        System.out.println(Arrays.toString(s.twoSum(nums, 9)));
    }

}
