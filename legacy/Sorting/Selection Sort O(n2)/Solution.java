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
    public int[] selectionSort(int[] nums){
        if(nums.length == 0){
            return nums;
        }
        
        for(int i = 0; i < nums.length; i++){
            int min = Integer.MAX_VALUE;
            int pos = -1;
            for(int j = i; j < nums.length; j++){
                if(nums[j] < min){
                    min = nums[j];
                    pos = j;
                }
            }
            if(pos != i){
                int temp = nums[i];
                nums[i] = min;
                nums[pos] = temp;
            }
        }
        return nums;
    }
}