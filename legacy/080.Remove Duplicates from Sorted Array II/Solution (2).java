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
        int i = 0;
        for(int num : nums){
            if(i < 2 || num > nums[i-2]){
                nums[i++] = num;
            }
        }
        return i;
    }
}
