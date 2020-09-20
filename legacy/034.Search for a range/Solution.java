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
    public int[] searchRange(int[] nums, int target) {
        // zero conditions
        int[] res = new int[] {-1,-1};
        int l_lo = 0;
        int l_hi = nums.length-1;
        while(l_lo <= l_hi){
            int mid = (l_lo + l_hi)/2;
            if(nums[mid] >= target){
                l_hi = mid-1;
            } else {
                l_lo = mid+1;
            }
        }
        
        if(l_lo < nums.length && nums[l_lo] == target){
            res[0] = l_lo;
        } else {
            return res;
        }
        
        int r_lo = l_lo;
        int r_hi = nums.length-1;
        while(r_lo <= r_hi){
            int mid = (r_lo + r_hi)/2;
            if(nums[mid] <= target){
                r_lo = mid+1;
            } else {
                r_hi = mid-1;
            }
        }
        res[1] = r_hi;
        return res;
    }
}