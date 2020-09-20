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
import data.ListNode;

/**
 *
 * @author sitengjin
 */
public class Solution {
    public int[] mergeSort(int[] nums){
        if(nums.length == 0 || nums.length == 1){
            return nums;
        }
        
        // merge(mergeSort(nums1), mergeSort(nums2));
    }
    
    public int[] merge(int[] nums1, int[] nums2){
        if(nums1.length == 0){
            return nums2;
        }
        
        if(nums2.length == 0){
            return nums1;
        }
        
        int[] res = new int[nums1.length + nums2.length];
        int n = 0;
        int i = 0;
        int j = 0;
        while(i < nums1.length || j < nums2.length){
            if(i >= nums1.length){
                res[n++] = nums2[j++];
            } else if(j >= nums2.length){
                res[n++] = nums1[i++];
            } else {
                res[n++] = nums1[i] < nums2[j] ? nums1[i++] : nums2[j++];
            }
        }
        return res;
    }
}