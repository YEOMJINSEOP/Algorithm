class MyHashMap:
    
    class ListNode:
        def __init__(self, key = None, value = None):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        
        #인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].val is None:
            self.table[index] = ListNode(key, val)
            return
        
        #해시 충돌이 발생한 경우, 개별 체이닝 방식으로 해결하는 과정
        p = self.table[index]
        while p:
            # 이미 해당 키가 존재할 경우 해당 값을 업데이트 한다
            if p.key == key:
                p.value = value
                return
            
            if p.next is None:
                break
            
            # p의 다음으로 이동해 새로운 노드로 저장한다.
            p = p.next
        p.next = ListNode(key, value)
            

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
        
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev = p
            p = p.next
        
