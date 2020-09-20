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
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        fast = slow.next;
        slow.next = null;
        
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(fast);
        
        return merge(l1, l2);
    }
    
    public ListNode merge(ListNode l1, ListNode l2){
        if(l1 == null){
            return l2;
        } else if (l2 == null){
            return l1;
        }
        
        ListNode newHead = new ListNode(0);
        ListNode p = newHead;
        ListNode p1 = l1;
        ListNode p2 = l2;
        while(p1!= null || p2!= null){
            if(p1 == null){
                p.next = p2;
                p2 = p2.next;
                p = p.next;
                continue;
            } else if(p2 == null){
                p.next = p1;
                p1 = p1.next;
                p = p.next;
                continue;
            }
            
            if(p1.val <= p2.val){
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            p = p.next;
        }
        return newHead.next;
    }
}