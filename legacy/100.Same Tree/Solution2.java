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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null || q == null){
            return p == q;
        }
        
        Stack<TreeNode> p_roots = new Stack<TreeNode>();
        Stack<TreeNode> q_roots = new Stack<TreeNode>();
        p_roots.push(p);
        q_roots.push(q);
        while(!p_roots.isEmpty() && !q_roots.isEmpty()){
            TreeNode np = p_roots.pop();
            TreeNode nq = q_roots.pop();
            if(np.val == nq.val){
                if(np.left == null || nq.left == null) {
                    if(np.left != nq.left){
                        return false;
                    }
                } else {
                    p_roots.push(np.left);
                    q_roots.push(nq.left);
                }
                
                if(np.right == null || nq.right == null){                    
                    if(np.right != nq.right){
                        return false;
                    }
                } else {
                    p_roots.push(np.right);
                    q_roots.push(nq.right);
                }
            } else {
                return false;
            }
        }
        return true;
    }
}