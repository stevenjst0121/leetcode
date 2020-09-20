/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package run;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Arrays;

/**
 *
 * @author Siteng Jin
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int add_one = 0;
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode newHead = new ListNode(0);
        ListNode p = newHead;
        
        while(p1 != null || p2 != null || add_one != 0){
            int sum = add_one + (p1 == null ? 0 : p1.val) + (p2 == null ? 0 : p2.val);
            add_one = sum/10;
            p.next = new ListNode(sum%10);
            p = p.next;
            if(p1 != null){
                p1 = p1.next;
            }
            if (p2 != null){
                p2 = p2.next;
            }
        }
        return newHead.next;
    }
}
