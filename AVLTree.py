class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def _insert(self, root, key, value):
        if root is None:
            return AVLNode(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        else:
            root.right = self._insert(root.right, key, value)

        self.update_height(root)

        balance = self.balance_factor(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_key_value_pair(self, key, value):
        self.root = self._insert(self.root, key, value)

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.find_min(root.right).key
            root.value = self.find_min(root.right).value
            root.right = self._delete(root.right, root.key)

        self.update_height(root)

        balance = self.balance_factor(root)

        if balance > 1:
            if self.balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        if balance < -1:
            if self.balance_factor(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete_key(self, key):
        self.root = self._delete(self.root, key)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def search_key(self, key):
        result = self.search(self.root, key)
        if result is not None:
            return result.value
        else:
            return None

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value)
            self.inorder_traversal(root.right)

    def inorder(self):
        self.inorder_traversal(self.root)

# Example usage:
avl_tree = AVLTree()
avl_tree.insert_key_value_pair(10, "Book 1")
avl_tree.insert_key_value_pair(20, "Book 2")
avl_tree.insert_key_value_pair(30, "Book 3")
avl_tree.insert_key_value_pair(40, "Book 4")
avl_tree.insert_key_value_pair(50, "Book 5")
avl_tree.insert_key_value_pair(25, "Book 2.5")

def print_menu():
    print("\nAVL Tree Operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Print List")
    print("5. Exit")

def run_avl_tree_cli():
    

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            key = int(input("Enter the key: "))
            value = input("Enter the value: ")
            avl_tree.insert_key_value_pair(key, value)
            print(f"Inserted key {key} with value '{value}' into the AVL tree.")
        elif choice == "2":
            key = int(input("Enter the key to delete: "))
            avl_tree.delete_key(key)
            print(f"Deleted key {key} from the AVL tree.")
        elif choice == "3":
            key = int(input("Enter the key to search: "))
            result = avl_tree.search_key(key)
            if result is not None:
                print(f"Found key {key} with value '{result}'.")
            else:
                print(f"Key {key} not found in the AVL tree.")
        elif choice == "4":
            print("Inorder traversal of the AVL tree:")
            avl_tree.inorder()
        elif choice == "5":
            print("Exiting the AVL tree command line runner.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    run_avl_tree_cli()