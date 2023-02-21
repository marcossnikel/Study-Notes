
## Array

Array é uma estrutura de dados que armazena elementos do mesmo tipo, como um array de inteiros, um array de caracteres, e assim por diante. Essa estrutura de dados armazena esses elementos em um espaço contíguo na memória e, por curiosidade, vale ressaltar que uma **lista do Python** é uma implementação de um array dinâmico.

Existem dois tipos de array, o array **estático** e o array **dinâmico**. O array **estático** tem um tamanho constante, ou seja, não podemos alterar o tamanho de um array estático depois que ele é inicializado. No entanto, arrays dinâmicos podem ser redimensionados durante a execução do programa usando um mecanismo chamado alocação de memória dinâmica. Isso nos permite criar novos arrays dinamicamente e usá-los conforme necessário. O fluxo básico é o seguinte:

-   Inicialize um array de tamanho **N**;
-   Adicione mais elementos no array;
-   Complete a memória alocada para este array;
-   Inicialize outro array de tamanho **2*N**;
-   Copie os elementos para o novo array;
-   Libere a memória alocada para o array antigo;
-   E assim por diante.

### Implementação de Array Dinâmico

Esta é a implementação de um array dinâmico em C:

```C
# include <stdio.h>
# include <stdlib.h>

int main(int argc, char *argv[]) {

    // Verifica o número de argumentos da linha de comando
    if (argc < 2) {
        printf("Usage: %s <int>\n", argv[0]);
        return 1;
    }
    int size = atoi(argv[1]);

    // Passo 1: Declare um ponteiro para armazenar o array
    int* d_array;

    // Passo 2: Aloque memória para o array
    d_array = (int *) malloc(size * sizeof(int));

    if (d_array == NULL) {
        printf("%s\n", "Falha na alocação de memória!");
        return 1;
    }

    // Passo 3: Use o array
    // Exemplo de uso
    for (int i = 0; i < size; i++) {
        d_array[i] = i;
    }
    for (int i = 0; i < size; i++) {
        printf("%d ", d_array[i]);
    }

    // Passo 4: Libere a memória
    free(d_array);

    return 0;
}

```

Em Python, temos uma implementação integrada de array dinâmico, o tipo **lista**:

```python
import sys

def main(size: int):
     
    # Cria uma lista de inteiros de 0 a size - 1
    d_array = [i for i in range(size)]

    # Exibe o conteúdo do array em uma linha
    print(*d_array) # 0 1 2 ...

if __name__ == "__main__":
    # Verifica o número de argumentos da linha de comando
    if len(sys.argv) != 2:
        print("Usage: python script.py size")
        sys.exit(1)

    # Verifica se é um inteiro
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("Você deve digitar um número inteiro!")
        sys.exit(1)

    main

```

Agora em Go, poderíamos implementar um array dinâmico usando um slice do Go, que é um tipo de referência que fornece uma maneira conveniente e eficiente de trabalhar com sequência de elementos:

```go
package main

import (
    "fmt"
    "os"
    "strconv"
)

func main() {

    // Verifica o número de argumentos da linha de comando
    if len(os.Args) != 2 {
        fmt.Printf("Uso: %s tamanho\n", os.Args[0])
        os.Exit(1)
    }

    // Converte o argumento para um inteiro
    tamanho, err := strconv.Atoi(os.Args[1])
    if err != nil {
        fmt.Println("Erro: tamanho deve ser um inteiro")
        os.Exit(1)
    }

    // Cria um array de inteiros para 'tamanho' elementos
    d_array := make([]int, 0, tamanho)

    // Adiciona 5 elementos ao slice 'd_array'
    d_array = append(d_array, 1, 2, 3, 4, 5)

    fmt.Println(d_array) // [1 2 3 4 5]
}

```