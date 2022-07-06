*join()
''join()  -> 리스트에 있는 '문자열'을 합치는 것
따라서 리스트에 int형으로 존재한다면 map(str, 리스트명) 으로 각각의 int를 str로 바꿔준 다음, join을 사용해줘야 한다.


* or 조건문 쓸 때 주의

내가 원하는 조건문이 만약: head 또는 head.next가 None이라면, 이라는 조건을 달고 싶을 때
if head or head.next is None  -> (X)

if (head is None) or (head.next is None) -> (O) 이렇게 해줘야 한다!

그냥 영어식 표현대로 따라서 쓰면 시간 날리고 이거 맞는데 왜 안되지..? 시전된다
