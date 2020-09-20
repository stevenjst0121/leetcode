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
    public int findMin(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        
        if(nums.length == 2){
            return Math.min(nums[0], nums[1]);
        }
        
        int rotatePoint = nums[0];  
        int hi = nums.length-1;
        int lo = 0;
        while(lo < hi-1){
            if(nums[lo] < nums[hi]){
                return nums[lo];
            }
            
            int mid = (hi+lo)/2;
            if(nums[mid] > nums[lo]){
                lo = mid;
            }else{
                hi = mid;
            }
        }
        return Math.min(nums[lo], nums[hi]);
    }
}
