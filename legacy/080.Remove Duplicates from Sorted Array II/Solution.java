/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 3){
            return nums.length;
        }
        
        int i = 0;
        int j = 1;
        boolean foundOneDuplicate = false;
        for(; j < nums.length; j++){
            if(nums[i] == nums[j]){
                if(!foundOneDuplicate){
                    nums[++i] = nums[j];
                    foundOneDuplicate = true;
                }
            } else {
                nums[++i] = nums[j];
                foundOneDuplicate = false;
            }
        }
        return i+1;
    }
}
