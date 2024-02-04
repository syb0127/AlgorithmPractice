class Solution {
    public int removeElement(int[] nums, int val) {
        int numslength = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[numslength] = nums[i];
                numslength += 1;
            }
        }
        return numslength;
    }
}