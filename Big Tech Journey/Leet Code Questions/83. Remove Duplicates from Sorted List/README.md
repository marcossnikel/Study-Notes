-> Em listas , sempre para acessarmos algum valor temos que percorrer a lista , não é possível realizar acesso por indices como em arrays, o node em uma lista é composto por um valor + um pointer que aponta para o próximo elemento ,para esse exercício é necessário manter o valor da nossa head (primeiro elemento) a uma variável e então usar um 'runner' node para percorrer a lista e ir checando os valores dos elementos, caso vc chegue em um valor diferente da nossa 'head', então diga que o próximo valor da head na lista sera o 'runner' , assim então eliminando os valores iguais.


Create a dummy node for the linked list to simplify edge cases and eliminate the need for special cases at the head of the list.

Initialize a slow pointer to the dummy node and a fast pointer to the head of the linked list.

Loop through the linked list using the fast pointer:
a. If the data of the fast node is not equal to the data of the node before it (slow node), update the next node of the slow pointer to be the fast node and move the slow pointer to the next node.
b. Move the fast pointer to the next node.

Return the dummy node's next node, which is the head of the linked list with duplicates removed.

Note: The goal of this problem is to remove all duplicates from a singly linked list. The slow pointer is used to track the unique elements and the fast pointer is used to traverse the linked list. By updating the next node of the slow pointer only if the data of the fast node is unique, we can maintain the unique elements in the linked list and effectively remove the duplicates.