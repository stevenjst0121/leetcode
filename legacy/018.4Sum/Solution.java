/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Arrays;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        
        for(int i = 0; i < nums.length-3;){
            for(int j = i+1; j < nums.length-2;){
                int k = j+1;
                int l = nums.length-1;
                while(k < l){
                    int sum = nums[i] + nums[j] + nums[k] + nums[l];
                    if(sum == target){
                        List<Integer> sol = new ArrayList<Integer>();
                        sol.add(nums[i]);
                        sol.add(nums[j]);
                        sol.add(nums[k]);
                        sol.add(nums[l]);
                        res.add(sol);
                        k++;
                        l--;
                        while(k < nums.length-1 && nums[k] == nums[k-1]){
                            k++;
                        }
                        while(l > 2 && nums[l] == nums[l+1]){
                            l--;
                        }
                    } else if (sum > target){
                        l--;
                        while(l > 2 && nums[l] == nums[l+1]){
                            l--;
                        }
                    } else {
                        k++;
                        while(k < nums.length-1 && nums[k] == nums[k-1]){
                            k++;
                        }
                    }
                }
                j++;
                while(j < nums.length-2 && nums[j] == nums[j-1]){
                    j++;
                }
            }
            i++;
            while(i < nums.length-3 && nums[i] == nums[i-1]){
                i++;
            }
        }
        return res;
    }
}
