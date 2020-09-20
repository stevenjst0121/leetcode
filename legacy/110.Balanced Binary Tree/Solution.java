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
import data.TreeNode;
import java.util.Stack;

/**
 *
 * @author sitengjin
 */
public class Solution {
    public boolean isBalanced(TreeNode root) {
        return getHeight(root) >= 0;
    }
    
    public int getHeight(TreeNode root){
        if(root == null){
            return 0;
        }
        
        int leftHeight = getHeight(root.left);
        if(leftHeight == -1){
            return -1;
        }
        int rightHeight = getHeight(root.right);
        if(rightHeight == -1){
            return -1;
        }
        return Math.abs(leftHeight - rightHeight) > 1 ? -1 : Math.max(leftHeight, rightHeight)+1;
    }
}