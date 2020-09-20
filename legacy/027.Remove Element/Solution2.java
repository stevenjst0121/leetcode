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
public class Solution2 {
    public static int removeElement(int[] nums, int val){
        int i = 0;
        int n = nums.length;
        for(; i < n;){
            if(nums[i] == val){
                nums[i] = nums[n-1];
                n--;
            } else {
                i++;
            }
        }
        return n;
    }
}
