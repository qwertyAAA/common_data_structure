from collections import deque
from typing import Any, Optional, List, Dict, Generator


class Node(object):
    """
    the Node object of BidirectionalTree
    """

    def __init__(self, parent: Optional[Any] = None, data: Optional[Any] = None,
                 children: Optional[List[Any]] = None) -> None:
        self.parent = parent
        self.data = data
        self.children = children if children else list()

    def __str__(self) -> str:
        return str(self.data)


class BidirectionalTree(object):
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node

    def add_children(self, children: List[Node], parent: Optional[Node] = None) -> None:
        """
        add children Nodes to parent Node
        :param children: list composed of children Nodes
        :param parent: parent of children Nodes
        :return: None
        """
        if not parent:
            parent = self.root_node
        parent.children.extend(children)
        for child in children:
            child.parent = parent

    def breadth_first_traverse(self) -> Generator:
        """
        traverse the whole tree breadth first
        :return: Generator
        """
        assist_queue = deque()
        assist_queue.append(self.root_node)
        while assist_queue:
            current_node = assist_queue.popleft()
            yield current_node
            if current_node.children:
                for child in current_node.children:
                    assist_queue.append(child)

    def breadth_first_search(self, target: Dict) -> Optional[Node]:
        """
        execute breadth first search
        :param target: target, The filter condition is composed of the attribute name of Node object and the corresponding value
            target = {
                "data": "hello world",
                "parent": parent_node,
                "children": children_nodes
            }
            target = {
                "data": "hello world",
            }
        :return: Node
        """
        assist_queue = deque()
        assist_queue.append(self.root_node)
        while assist_queue:
            current_node: Node = assist_queue.popleft()
            flag = True
            for k, v in target.items():
                flag = flag and getattr(current_node, k) == v
                if not flag:
                    break
            if flag:
                return current_node
            if current_node.children:
                for child in current_node.children:
                    assist_queue.append(child)
        return None

    def depth_first_traverse(self) -> Generator:
        """
        traverse the whole tree depth first
        :return: Generator
        """

        def traverse(current_node: Node):
            yield current_node
            for child in current_node.children:
                for item in traverse(child):
                    yield item

        return traverse(self.root_node)

    def depth_first_search(self, target: Dict) -> Optional[Node]:
        """
        execute depth first search
        :param target: target, The filter condition is composed of the attribute name of Node object and the corresponding value
            target = {
                "data": "hello world",
                "parent": parent_node,
                "children": children_nodes
            }
            target = {
                "data": "hello world",
            }
        :return: Node
        """

        def search(current_node: Node):
            flag = True
            for k, v in target.items():
                flag = flag and getattr(current_node, k) == v
                if not flag:
                    break
            if flag:
                return current_node
            for child in current_node.children:
                ret = search(child)
                if ret:
                    return ret
        return search(self.root_node)


if __name__ == '__main__':
    # bt = BidirectionalTree(Node(data="1"))
    # bt.add_children([Node(data="1-1"), Node(data="1-2")], parent=bt.root_node)
    # bt.add_children(
    #     [Node(data="1-1-1"), Node(data="1-1-2")], parent=bt.root_node.children[0])
    # bt.add_children(
    #     [Node(data="1-2-1"), Node(data="1-2-2")], parent=bt.root_node.children[1])
    # for i in bt.breadth_first_search():
    #     print(i)
    # print("------------------------------------------------------------------------------------------------")
    #
    # for i in bt.depth_first_search():
    #     print(i)

    bt = BidirectionalTree(Node(data="1"))
    # path1 = "1htap/q/q"
    path1 = deque(["q", "q", "path1"])
    # path2 = "1htap/w/w"
    path2 = deque(["w", "w", "path1"])
    # path3 = "2htap/e/e"
    path3 = deque(["e", "e", "path2"])
    # path4 = "2htap/r/r"
    path4 = deque(["r", "r", "path2"])
    # path5 = "2htap/t/t"
    path5 = deque(["t", "t", "path2"])


    def test(reversed_path_deque: deque, parent=bt.root_node):
        if not reversed_path_deque:
            return
        # path_list = os.path.split(reversed_path)
        node = Node(data=reversed_path_deque.pop())
        temp_node = bt.depth_first_search({
            "data": node.data,
            "parent": parent
        })
        if not temp_node:
            temp_parent = bt.depth_first_search({
                "data": parent.data,
                "parent": parent.parent
            })
            bt.add_children([node, ], temp_parent if temp_parent else parent)
        test(reversed_path_deque, temp_node if temp_node else node)


    test(path1)
    test(path2)
    test(path3)
    test(path4)
    test(path5)
    # print(bt.breadth_first_search({"data": "1", "parent": bt.root_node}))
    for i in bt.depth_first_traverse():
        print(i)
    # def split_path_recursion(path: str, result: Optional[deque] = None) -> List:
    #     """
    #     递归拆分目录结构
    #     :param path: 目标目录
    #     :param result: 结果接收对象
    #     :return: list
    #     """
    #     try:
    #         if result is None:
    #             result = deque(os.path.split(path))
    #         else:
    #             if not result[0]:
    #                 result.popleft()
    #                 return list(result)
    #             if not result[-1]:
    #                 result.pop()
    #             temp = list(os.path.split(result.popleft()))
    #             result = [*temp, *result]
    #         return split_path_recursion(result[0], result)
    #     except Exception as e:
    #         raise FileException(f"拆分目录结构异常！异常信息：{e}")
    #
    #
    # def test(path, parent=bt.root_node):
    #
