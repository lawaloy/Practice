/**
     * O(log(n)^2)
     *
     * @param root
     * @return
     */
    public TreeNode getLastNodeInCompleteBinaryTree(TreeNode root) {

        /**
         * if root is null, then add at root it self
         * O(1)
         */
        if (null == root)
            return root;


        /**
         * if root don't have left child, then add at left side
         * O(1)
         */
        if (root.left == null)
            return root;

        /**
         * if root don't have right child but has left child, then add at right side
         *
         * O(1)
         */
        if (root.right == null)
            return root;


        /**
         * check does tree rooted at this node has left and right height same.
         * If yes, then it will only possible when this tree is full binary tree.
         * Then we can simply add a node at the left side of leftmost node
         */

        if (leftRightHeightAreSame(root)) { //O(log(n))

            return getLeftMostNode(root); //O(log(n))

        } else if (leftRightHeightAreSame(root.left)) { //O(log(n))
            /**
             * if left and right are not same but its true for left sub-tree
             * i.e. left is full binary tree [keep in mind we talk about the complete binary as input]
             * we need to add at right sub-tree
             */
            return getLastNodeInCompleteBinaryTree(root.right);  //O(log(n))
        } else
            return getLastNodeInCompleteBinaryTree(root.left); //O(log(n))

    }

    /**
     * O(log(n))
     *
     * @param root
     * @return
     */
    private boolean leftRightHeightAreSame(TreeNode root) {
        if (root == null)
            return true;

        if (root.left == null && root.right == null)
            return true;

        return leftHeight(root) == rightHeight(root);
    }


    /**
     * O(log(n))
     *
     * @param root
     * @return
     */
    private int leftHeight(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + leftHeight(root.left);
    }

    /**
     * O(log(n))
     *
     * @param root
     * @return
     */
    private int rightHeight(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + rightHeight(root.right);
    }

    /**
     * O(log(n))
     *
     * @param root
     * @return
     */
    private TreeNode getLeftMostNode(TreeNode root) {

        while (root != null && root.left != null)
            root = root.left;

        return root;

    }
Driver

public static void main(String[] args) {

        LastNodeInCompleteBinaryTree binaryTree = new LastNodeInCompleteBinaryTree();
        /**
         * *     1
         * *    / \
         * *   2   3
         * *  / \  /
         * * 4  5 6
         *
         * @return
         */
        System.out.println(binaryTree.getLastNodeInCompleteBinaryTree(Helper.getTree1()));

        /**
         * *     1
         * *    / \
         * *   2   3
         * *  / \  /\
         * * 4  5 6 7
         *
         * @return
         */
        System.out.println(binaryTree.getLastNodeInCompleteBinaryTree(Helper.getTree2()));


        /**
         * *           1
         * *          /  \
         * *         2    3
         * *         / \  /\
         * *        4  5 6 7
         * *      /  \
         * *     8    9
         *
         * @return
         */
        System.out.println(binaryTree.getLastNodeInCompleteBinaryTree(Helper.getTree3()));


        /**
         * *           1
         * *          /  \
         * *         2    3
         * *        /    /
         * *       4    6
         *
         * @return
         */
        System.out.println(binaryTree.getLastNodeInCompleteBinaryTree(Helper.notCompleteBinaryTree()));
    }
	
Output

TreeNode{val=3, left=TreeNode{val=6, left=null, right=null}, right=null}
TreeNode{val=4, left=null, right=null}
TreeNode{val=5, left=null, right=null}
TreeNode{val=2, left=TreeNode{val=4, left=null, right=null}, right=null}
