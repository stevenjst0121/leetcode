/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package run;

import data.*;
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
    public void connect(TreeLinkNode root) {  
        List<TreeLinkNode> store = new ArrayList<TreeLinkNode>();
        connectHelper(root, store, 0);
    }
    
    public void connectHelper(TreeLinkNode root, List<TreeLinkNode> store, int height){
        if(root == null){
            return;
        }
        
        if(store.size() <= height){
            store.add(root);
        } else {
            TreeLinkNode node = store.get(height);
            node.next = root;
            store.set(height, root);
        }
        connectHelper(root.left, store, height+1);
        connectHelper(root.right, store, height+1);
    }
}
