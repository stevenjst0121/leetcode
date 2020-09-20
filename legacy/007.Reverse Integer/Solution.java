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
    public int reverse(int x) {
        int reversed = 0;
        int left = x;
        while(left != 0){
            int temp = reversed*10 + left%10;
            if((temp - left%10)/10 != reversed){
                return 0;
            }
            reversed = temp;
            left = left/10;
        }
        return reversed;
    }
}