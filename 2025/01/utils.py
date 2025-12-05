# pyright: reportOptionalMemberAccess=false
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    data: Any
    prev: Node | None = None
    next: Node | None = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.current = None  # Cursor navigation

    @property
    def current_data(self) -> Any:
        return self.current.data

    def is_empty(self) -> bool:
        return self.head is None

    def ensure_not_empty(self) -> None:
        if self.is_empty():
            raise ValueError("List is empty")

    def append(self, data: Any) -> None:
        if self.is_empty():
            new_node = Node(data)
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.current = new_node  # Initialize cursor
        else:
            assert self.head
            tail = self.head.prev
            new_node = Node(data, prev=tail, next=self.head)
            assert tail
            tail.next = new_node
            self.head.prev = new_node

    def prepend(self, data: Any) -> None:
        self.ensure_not_empty()
        self.head = self.head.prev

    def move_forward(self, steps=1) -> None:
        self.ensure_not_empty()
        for i in range(steps):
            assert self.current
            self.current = self.current.next

    def move_backward(self, steps=1) -> None:
        self.ensure_not_empty()
        for i in range(steps):
            assert self.current
            self.current = self.current.prev

    def goto(self, data: Any) -> None:
        """Moves the cursor to the first occurence of `data`."""
        self.ensure_not_empty()
        cur = self.head
        while True:
            assert cur
            if cur.data == data:
                self.current = cur
                return
            if cur.next == self.head:
                raise ValueError(f"Node with data '{data}' not found")
            cur = cur.next
