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
    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        
        return isEqual(root.left, root.right);
    }
    
    public boolean isEqual(TreeNode root1, TreeNode root2){
        if(root1 == null || root2 == null){
            return root1 == root2;
        }
        
        if(root1.val == root2.val){
            return isEqual(root1.left, root2.right) && isEqual(root1.right, root2.left);
        } else {
            return false;
        }
    }
}
