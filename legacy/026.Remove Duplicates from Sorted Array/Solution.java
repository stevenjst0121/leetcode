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
        if(nums.length == 1){
            return 1;
        }
        
        int i = 0;
        int j = 1;
        for(; j < nums.length; j++){
            if(nums[i] == nums[j]){
                continue;
            } else {
                nums[++i] = nums[j];
            }
        }
        return i+1;
    }
}
