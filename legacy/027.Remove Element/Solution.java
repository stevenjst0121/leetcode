/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.Arrays;

/**
 *
 * @author sitengjin
 */
public class Solution {
    public static int removeElement(int[] nums, int val) {
        
        int i = 0;
        int j = 0;
        System.out.println(Arrays.toString(nums) + " i=" + i + ", j=" + j);
        for(; j < nums.length; j++){
            System.out.println(Arrays.toString(nums) + " i=" + i + ", j=" + j);
            if(nums[j] != val){
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}