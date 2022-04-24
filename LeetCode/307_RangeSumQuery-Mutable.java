class NumArray {
    // SegmentTree
    class TreeNode{
        public int sum;
        public int start, end;
        public TreeNode left, right;
        public TreeNode(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    TreeNode root = null;
    public NumArray(int[] nums) {
        root = buildTree(nums, 0, nums.length - 1);
    }
    
    public void update(int index, int val) {
        update(root, index, val);
    }
    
    public int sumRange(int left, int right) {
        return query(root, left, right);
    }

    private int query(TreeNode root, int left, int right){
        if(root.start == left && root.end == right){
            return root.sum;
        }else{
            int mid = root.start + (root.end - root.start) / 2;
            if(right <= mid){
                return query(root.left, left, right);
            }else if(left > mid){
                return query(root.right, left, right);
            }else{
                return query(root.left, left, mid) + query(root.right, mid + 1, right);
            }
        }
    }

    private void update(TreeNode root, int index, int val){
        if(root.start == root.end){ // return if it is the end node
            root.sum = val; // update sum
            return;
        }else{
            int mid = root.start + (root.end - root.start) / 2;
            if(index <= mid){
                update(root.left, index, val);
            }else{
                update(root.right, index, val);
            }
            root.sum = root.left.sum + root.right.sum; // update sum
        }
    }

    private TreeNode buildTree(int[] nums, int start, int end){
        if(start > end) // return null if start index greater than end index
            return null;
        else if(start == end){ // return if it is end node
            TreeNode node = new TreeNode(start, end);
            node.sum = nums[start]; // initialise sum
            return node;
        }else{
            TreeNode node = new TreeNode(start, end);
            int mid = start + (end - start) / 2;

            node.left = buildTree(nums, start, mid); // create left node
            node.right = buildTree(nums, mid + 1, end); // create right node

            node.sum = node.left.sum + node.right.sum; // initialise sum
            return node;
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */