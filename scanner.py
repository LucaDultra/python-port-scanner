import socket

target = input("Digite o IP alvo: ")

print(f"\nEscaneando portas em {target}...\n")

for porta in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    resultado = sock.connect_ex((target, porta))

    if resultado == 0:
        print(f"Porta {porta} está ABERTA")

    sock.close()
