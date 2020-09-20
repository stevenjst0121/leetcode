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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null){
            return;
        }
        
        ListNode p1 = head;
        ListNode p2 = head;
        while(p2.next != null && p2.next.next != null){
            p1 = p1.next;
            p2 = p2.next.next;
        }
        
        ListNode head2 = reverseList(p1.next);
        p1.next = null;
        p1 = head;
        p2 = head2;
        while(p2 != null){
            ListNode p2_next = p2.next;
            p2.next = p1.next;
            p1.next = p2;
            p2 = p2_next;
            p1 = p1.next.next;
        }
    }
    
    public ListNode reverseList(ListNode head){
        if(head == null){
            return head;
        }
        
        ListNode newHead = new ListNode(0);
        ListNode p = head;
        newHead.next = p;
        while(p.next != null){
            ListNode p1 = p.next;
            p.next = p1.next;
            p1.next = newHead.next;
            newHead.next = p1;
        }
        return newHead.next;
    }
}