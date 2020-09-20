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
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || k == 0){
            return head;
        }
        
        ListNode p1 = head;
        ListNode p2 = head;
        
        int n = 1;
        while(p1.next != null){
            p1 = p1.next;
            n++;
        }
        int k1 = k%n; 
        if(k1 == 0){
            return head;
        }
        
        for(int i = 0; i < k1; i++){
            p2 = p2.next;
        }
        
        p1 = head;
        while(p2.next != null){
            p1 = p1.next;
            p2 = p2.next;
        }
        
        ListNode newHead = p1.next;
        p1.next = null;
        p2.next = head;
        return newHead;
    }
    
    public ListNode rotateRight2(ListNode head, int k) {
        if(head == null){
            return null;
        }
        
        ListNode p = head;
        int n = 1; // length of list
        while(p.next != null){
            p = p.next;
            n++;
        }
        
        p.next = head; // make a circle
        p = head;
        int steps = n - k%n;
        while(steps > 1){
            p = p.next;
            steps--;
        }
        ListNode newHead = p.next;
        p.next = null;
        return newHead;
    }
}