Claro! Aqui está uma **To-Do List detalhada**, organizada em **etapas progressivas**, para você implementar uma coleção de estruturas de dados clássicas, seguindo princípios de **Clean Code**, **SOLID** e **design extensível**.

---

## ✅ **To-Do List: Implementação de Estruturas de Dados em Python**

### 📁 Estrutura base do projeto

```
data_structures/
├── abstract/
│   ├── abstract_list.py
│   ├── abstract_stack.py
│   ├── abstract_queue.py
│   ├── abstract_deque.py
├── linked/
│   ├── singly_linked_list.py
│   ├── doubly_linked_list.py
│   ├── list_node.py
├── array/
│   ├── static_array_list.py
│   ├── dynamic_array_list.py
├── queue/
│   ├── queue_array.py
│   ├── queue_linked.py
├── deque/
│   ├── deque_array.py
│   ├── deque_linked.py
├── stack/
│   ├── stack_array.py
│   ├── stack_linked.py
├── tests/
│   ├── test_singly_linked_list.py
│   ├── test_dynamic_array_list.py
│   └── ...
```

---

### 1️⃣ **Infraestrutura genérica**

* [ ] Criar `AbstractList[T]` com todos os contratos:

  * append, prepend, insert, pop, pop\_first, remove, get, set, reverse, clear, etc.
* [ ] Criar `AbstractStack[T]`, `AbstractQueue[T]`, `AbstractDeque[T]`
* [ ] Criar tipo `Comparator[T] = Callable[[T, T], bool]`

---

### 2️⃣ **Singly Linked List**

* [ ] `ListNode[T]`
* [ ] `LinkedList[T]`
* [ ] Implementar todos os métodos obrigatórios definidos em `AbstractList`
* [ ] Testes com `pytest`

---

### 3️⃣ **Doubly Linked List**

* [ ] `DoubleListNode[T]`
* [ ] `DoublyLinkedList[T]`
* [ ] Métodos especiais de iteração reversa, remoção eficiente, etc.
* [ ] Testes com `pytest`

---

### 4️⃣ **Static Array List**

* [ ] Criar classe `StaticArrayList[T]` com capacidade fixa
* [ ] Implementar contratos de `AbstractList`
* [ ] Lançar exceção se exceder o tamanho
* [ ] Testes com `pytest`

---

### 5️⃣ **Dynamic Array List**

* [ ] Criar classe `DynamicArrayList[T]` que dobra de tamanho
* [ ] Implementar contratos de `AbstractList`
* [ ] Comparar performance com `LinkedList`
* [ ] Testes com `pytest`

---

### 6️⃣ **Stacks (Pilha)**

* [ ] Criar `StackArray[T]` usando `DynamicArrayList`
* [ ] Criar `StackLinked[T]` usando `LinkedList`
* [ ] Implementar `AbstractStack` (push, pop, peek, is\_empty)
* [ ] Testes com `pytest`

---

### 7️⃣ **Queues (Fila)**

* [ ] `QueueArray[T]` (com circular array para eficiência)
* [ ] `QueueLinked[T]` (head para remoção, tail para inserção)
* [ ] Implementar `AbstractQueue`
* [ ] Testes com `pytest`

---

### 8️⃣ **Deques (Fila Dupla)**

* [ ] `DequeArray[T]` com expansão circular
* [ ] `DequeLinked[T]` com `DoublyLinkedList`
* [ ] Implementar `AbstractDeque` (append, appendleft, pop, popleft)
* [ ] Testes com `pytest`

---

### 9️⃣ **Extras e boas práticas**

* [ ] Criar fábricas de comparadores (por id, por nome, por chave)
* [ ] Criar `for_each` em todas as listas
* [ ] Suporte a `__iter__`, `__len__`, `__getitem__`, `__contains__`
* [ ] Adicionar `__repr__` amigável em todas as estruturas
* [ ] Documentação por docstrings e README

---

### 🔟 (Opcional) Benchmark

* [ ] Comparar performance de:

  * `LinkedList` vs `DynamicArrayList`
  * `QueueArray` vs `QueueLinked`
  * `DequeArray` vs `DequeLinked`
