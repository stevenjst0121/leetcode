/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

/**
 *
 * @author sitengjin
 */
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        
        int min_dis = Integer.MAX_VALUE;
        int best_sum = Integer.MAX_VALUE;
        
        for(int i = 0; i < nums.length; i++){
            int j = i + 1;
            int k = nums.length-1;
            
            while(j < k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == target){
                    return sum;
                } else if (sum < target) {
                    int diff = target - sum;
                    if(diff < min_dis){
                        min_dis = diff;
                        best_sum = sum;
                    }
                    j++;
                } else {
                    int diff = sum - target;
                    if(diff < min_dis){
                        min_dis = diff;
                        best_sum = sum;
                    }
                    k--;
                }
            }
        }
        return best_sum;
    }
}