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