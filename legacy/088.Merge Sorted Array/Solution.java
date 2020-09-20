/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package run;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m+n-1;
        
        for(; k >= 0; k--){
            if(i < 0){
                nums1[k] = nums2[j];
                j--;
                continue;
            }
            
            if(j < 0){
                nums1[k] = nums1[i];
                i--;
                continue;
            }
            
            if(nums1[i] >= nums2[j]){
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
        }
    }
}
