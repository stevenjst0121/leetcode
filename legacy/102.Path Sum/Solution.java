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
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        return hasPathSumHelper(root, sum, 0);
    }
    
    public boolean hasPathSumHelper(TreeNode root, int sum, int preSum){
        if(root == null){
            return false;
        }
        
        int curSum = preSum + root.val;
        if(root.left == null && root.right == null){
            if(curSum == sum){
                return true;
            } else {
                return false;
            }
        } else {
            return hasPathSumHelper(root.left, sum, curSum) || hasPathSumHelper(root.right, sum, curSum);
        }
    }
}
