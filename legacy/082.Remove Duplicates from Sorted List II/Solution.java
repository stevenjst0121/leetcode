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

/**
 *
 * @author sitengjin
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null){
            return null;
        }
        
        ListNode prev = new ListNode(0);
        ListNode p = head;
        prev.next = p;
        while(p != null && p.next != null){
            if(p.val != p.next.val){
                prev = p;
                p = p.next;
            } else {
                int val = p.val;
                ListNode n = p.next.next;
                while(n != null && n.val == val){
                    n = n.next;
                }
                prev.next = n;
                p = n;
            }
        }
        return prev.next;
    }
}