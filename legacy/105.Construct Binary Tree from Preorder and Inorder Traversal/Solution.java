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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder.length == 0 || inorder.length == 0 || 
           preorder.length != inorder.length){
            return null;
        }
        
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for(int i = 0; i < inorder.length; i++){
            hm.put(inorder[i], i);
        }
        
        return buildTreePreIn(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1, hm);
    }
    
    public TreeNode buildTreePreIn(int[] preorder, int ps, int pe, 
                                   int[] inorder, int is, int ie, HashMap<Integer, Integer> hm){
        if(ps > pe || is > ie){
            return null;
        }
        
        int rootVal = preorder[ps];
        int rootIdx = hm.get(rootVal);
        TreeNode root = new TreeNode(rootVal);
        if(ps == pe){
            return root;
        }
        
        if(rootIdx != ie){ //right
            int gap = ie - rootIdx;
            root.right = buildTreePreIn(preorder, pe-gap+1, pe, inorder, rootIdx+1, ie, hm);
        }
        
        if(rootIdx != is){ //left
            int gap = rootIdx - is;
            root.left = buildTreePreIn(preorder, ps+1, ps+gap, inorder, is, rootIdx-1, hm);
        }
        return root;
    }
}