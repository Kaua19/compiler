      #verifica se números inteiros ou float
        if c.isdigit():
            start = i
            has_dot = False
            while i < len(codigo) and (codigo[i].isdigit() or codigo[i] == '.'):
                if codigo[i] == '.':
                    if has_dot:
                        break
                    has_dot = True
                i += 1
            numero = codigo[start:i]
            tipo = "NUMERO_FLOAT" if has_dot else "NUMERO"
            yield (linha_num, numero, tipo)
            continue
        #se não for reconhecido, retorna desconhecido
        yield (linha_num, c, "DESCONHECIDO")
        i += 1
#transdorma o resultado do analisador léxico em uma lista de tuplas
tokens = list(analisador_lexico(codigo))
#simplifica os tokens para facilitar a análise sintática
#Ex (PALAVRA_CHAVE, "int") 
tokens_simplificados = [(tipo, lexema) for _, lexema, tipo in tokens]

pos = 0

def token_atual():
    """Retorna o token atual ou EOF se não houver mais tokens."""
    return tokens_simplificados[pos] if pos < len(tokens_simplificados) else ("EOF", "EOF")

def erro(mensagem):
    """Exibe uma mensagem de erro sintático com a linha do erro."""
    linha = tokens[pos][0] if pos < len(tokens) else "EOF"
    print(f"Erro sintático na linha {linha}: {mensagem}")
    return False