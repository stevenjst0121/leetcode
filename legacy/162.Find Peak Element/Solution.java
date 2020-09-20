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
    public int findPeakElement(int[] nums) {
        if(nums.length == 0){
            return -1;
        }
        
        int lo = 0;
        int hi = nums.length-1;
        while(lo <= hi){
            int mid = (lo+hi)/2;
            
            if((mid == 0 || nums[mid-1] < nums[mid]) && 
               (mid == nums.length-1 || nums[mid+1] < nums[mid])){
                return mid;
            } else if (mid > 0 && nums[mid-1] > nums[mid]){
                hi = mid-1;
            } else {
                lo = mid+1;
            }
        }
        return -1;
    }
}