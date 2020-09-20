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
    public int[] plusOne(int[] digits) {
        int add = 1;
        for(int i = digits.length - 1; i >= 0; i--){
            int sum = digits[i] + add;
            int cur = sum%10;
            add = sum/10;
            digits[i] = cur;
        }
        
        if(add > 0){
            int[] res = new int[digits.length+1];
            res[0] = 1;
            return res;
        } else {
            return digits;
        }
    }
}
