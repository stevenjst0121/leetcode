/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Stack;
import java.util.LinkedList;
import run.TreeNode;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public List<Integer> preOrderIteration(TreeNode root){        
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> roots = new Stack<TreeNode>();
        TreeNode node = root;
        while(node != null || !roots.isEmpty()){
            if(node != null){
                res.add(node.val);
                roots.push(node);
                node = node.left;
            } else {
                node = roots.pop().right;
            }
        }
        return res;
    }
}
