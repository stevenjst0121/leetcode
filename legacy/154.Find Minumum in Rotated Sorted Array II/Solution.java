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
    public int findMin(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        
        if(nums.length == 2){
            return Math.min(nums[0], nums[1]);
        }
        
        int lo = 0;
        int hi = nums.length-1;
        while(lo < hi-1){
            if(nums[lo] < nums[hi]){
                return nums[lo];
            }
            int mid = (lo+hi)/2;
            if(nums[mid] < nums[hi]){
                hi = mid;
                while(hi > 0 && nums[hi] == nums[hi-1]){
                    hi--;
                }
            } else if(nums[mid] > nums[hi]) {
                lo = mid;
                while(lo < nums.length && nums[lo] == nums[lo+1]){
                    lo++;
                }
            } else {
                hi--;
            }
        }
        return Math.min(nums[lo], nums[hi]);
    }
}