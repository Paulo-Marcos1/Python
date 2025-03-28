try:

    f = open("Nomes.txt")
    s = f.readline()
    i = int(s.strip())

except FileNotFoundError:

    print(f"Arquivo {f.name} não encontrado")

except IOError:

    print("Erro na abertura do arquivo.")

except ValueError:

    print("Formato invalido encontrado no arquivo")

except Exception as e:

    print(f"Erro inesperado: {e}")
    raise

finally:
    print("não quero saber se deu ruim ou não!")