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
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if(m == 0){
            return false;
        }
        int n = matrix[0].length;
        if(n == 0){
            return false;
        }
        int i = 0;
        int j = n-1;
        while(i < matrix.length && j >= 0){
            if(matrix[i][j] < target){
                i++;
            } else if (matrix[i][j] > target){
                j--;
            } else {
                return true;
            }
        }
        return false;
    }
}