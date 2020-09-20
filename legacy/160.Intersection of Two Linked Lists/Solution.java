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
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null){
            return null;
        }
        
        ListNode endA = headA;
        while(endA.next != null){
            endA = endA.next;
        }
        endA.next = headB;
        ListNode slow = headA;
        ListNode fast = headA;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                slow = headA;
                while(slow != fast){
                    slow = slow.next;
                    fast = fast.next;
                }
                endA.next = null;
                return slow;
            }
        }
        endA.next = null;
        return null;
    }
}