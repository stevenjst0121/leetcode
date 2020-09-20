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

/**
 *
 * @author sitengjin
 */
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder.length == 0 || postorder.length == 0){
            return null;
        }
        
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for(int i = 0; i < inorder.length; i++){
            hm.put(inorder[i], i);
        }
        
        return buildTreePostIn(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1, hm);
    }
    
    private TreeNode buildTreePostIn(int[] inorder, int is, int ie, 
            int[] postorder, int ps, int pe, HashMap<Integer, Integer> hm){
        if(is > ie || ps > pe){
            return null;
        }
        
        int rootVal = postorder[pe];
        TreeNode root = new TreeNode(rootVal);
        if(ps == pe){
            return root;
        }
        
        int rootIndex = hm.get(rootVal);
        if(rootIndex != is){
            int gap = rootIndex - is;
            root.left = buildTreePostIn(inorder, is, rootIndex-1, postorder, ps, ps+gap-1, hm);
        }
        if(rootIndex != ie){
            int gap = ie - rootIndex;
            root.right = buildTreePostIn(inorder, rootIndex+1, ie, postorder, pe-gap, pe-1, hm);
        }
        return root;
    }
}