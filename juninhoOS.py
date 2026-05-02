import time, datetime, os, sys, random

G = "\033[92m"
Y = "\033[93m"
W = "\033[97m"
GR = "\033[37m"
C = "\033[96m"
R = "\033[91m"
M = "\033[95m"
RE = "\033[0m"

pkgs = ["firefox","vim","python3","git","curl","htop","neofetch","vlc","discord","steam"]
instalados = []
historico = []
server_ativo = False
server_inicio = None
notas = []

os.system("clear")
for txt, cor in [
    ("JuninhoOS Bootloader v1.0.4", W),
    ("Copyright (C) 2024 JuninhoOS Project", GR),
    ("", GR),
    ("Initializing hardware...", GR),
    ("[  OK  ] CPU detected: JuninhoCore x86_64", G),
    ("[  OK  ] RAM: 512MB detected", G),
    ("[  OK  ] Storage: /dev/juninho0", G),
    ("", GR),
    ("Loading kernel...", GR),
    ("[  OK  ] Kernel loaded successfully", G),
    ("", GR),
    ("Checking system integrity...", GR),
]:
    print(f"{cor}{txt}{RE}")
    time.sleep(0.4)

print(f"\n{Y}{'='*30}{RE}")
print(f"{Y}  MODIFICADO, CUIDADO{RE}")
print(f"{Y}{'='*30}{RE}")
time.sleep(2)

os.system("clear")
now = datetime.datetime.now()
print(f"\n\n{W}  JuninhoOS{RE}")
print(f"{GR}  {now.strftime('%d/%m/%Y  %H:%M:%S')}{RE}\n")
print(f"{C}  Usuário: SUPERUSER{RE}\n")
input(f"{GR}  Pressione Enter para entrar...{RE}")
os.system("clear")
print(f"{G}  Bem-vindo, SUPERUSER!{RE}\n")
time.sleep(1)

def firefox():
    os.system("clear")
    print(f"{C}  Firefox - JuninhoOS{RE}")
    print(f"{GR}  {'='*40}{RE}")
    url = input(f"{W}  URL: {RE}").strip().lower()
    if url in ["youtube.com", "www.youtube.com"]:
        os.system("clear")
        print(f"{R}  YouTube{RE}\n")
        print(f"{GR}  {'='*40}{RE}")
        print(f"{W}  [1] Minecraft - 10M views\n  [2] Linux Tutorial - 500K views\n  [3] JuninhoOS - 999M views{RE}")
        print(f"{GR}  {'='*40}{RE}")
        input(f"\n{GR}  Enter para voltar...{RE}")
    elif url in ["google.com", "www.google.com"]:
        os.system("clear")
        print(f"\n{R}G{Y}o{G}o{C}g{R}l{Y}e{RE}\n")
        busca = input(f"{W}  Pesquisar: {RE}").strip()
        os.system("clear")
        print(f"{W}  Resultados para: {C}{busca}{RE}\n")
        print(f"{C}  1. {busca} - Wikipedia{RE}\n{GR}     pt.wikipedia.org\n")
        print(f"{C}  2. Tudo sobre {busca}{RE}\n{GR}     www.google.com\n")
        print(f"{C}  3. {busca} - JuninhoOS Docs{RE}\n{GR}     docs.juninhoOS.com{RE}\n")
        input(f"{GR}  Enter para voltar...{RE}")
    elif url in ["github.com", "www.github.com"]:
        os.system("clear")
        print(f"{W}  GitHub{RE}\n{GR}  {'='*40}{RE}")
        print(f"{C}  [1] JuninhoOS/core - 9.2k stars\n  [2] JuninhoOS/kernel - 4.1k stars\n  [3] JuninhoOS/firefox-port - 1.3k stars{RE}")
        print(f"{GR}  {'='*40}{RE}")
        input(f"\n{GR}  Enter para voltar...{RE}")
    elif url in ["juninhoos.com", "www.juninhoos.com"]:
        os.system("clear")
        print(f"{C}  Bem-vindo ao site oficial do JuninhoOS!{RE}\n")
        print(f"{W}  O sistema operacional mais modificado do mundo.{RE}")
        print(f"{GR}  Versão atual: 1.0.4\n  Downloads: 999.999.999{RE}\n")
        input(f"{GR}  Enter para voltar...{RE}")
    else:
        print(f"{R}  Site não encontrado!{RE}\n")
        time.sleep(1)

def calc():
    os.system("clear")
    print(f"{C}  JuninhoCalc{RE}")
    print(f"{GR}  Digite 'sair' para voltar{RE}\n")
    while True:
        expr = input(f"{W}  > {RE}").strip()
        if expr == "sair":
            break
        try:
            print(f"{G}  = {eval(expr)}{RE}\n")
        except:
            print(f"{R}  Expressão inválida!{RE}\n")

def editor():
    os.system("clear")
    print(f"{C}  JuninhoEditor{RE}")
    print(f"{GR}  'SALVAR' para salvar, 'SAIR' para cancelar{RE}\n")
    linhas = []
    while True:
        linha = input(f"{W}  {len(linhas)+1}: {RE}")
        if linha == "SAIR":
            break
        elif linha == "SALVAR":
            nome = input(f"{GR}  Nome do arquivo: {RE}").strip()
            notas.append({"nome": nome, "conteudo": linhas})
            print(f"{G}  '{nome}' salvo!{RE}\n")
            time.sleep(1)
            break
        else:
            linhas.append(linha)

def bloco_notas():
    os.system("clear")
    print(f"{C}  Bloco de Notas{RE}\n{GR}  {'='*30}{RE}")
    if not notas:
        print(f"{Y}  Nenhuma nota salva ainda.{RE}\n")
    else:
        for i, n in enumerate(notas):
            print(f"{W}  [{i+1}] {n['nome']}{RE}")
        print()
        escolha = input(f"{GR}  Escolha (Enter para voltar): {RE}").strip()
        if escolha.isdigit() and 0 < int(escolha) <= len(notas):
            n = notas[int(escolha)-1]
            os.system("clear")
            print(f"{C}  {n['nome']}{RE}\n")
            for l in n['conteudo']:
                print(f"  {l}")
            print()
    input(f"{GR}  Enter para voltar...{RE}")

def weather():
    os.system("clear")
    cidades = {
        "palmas": ("32°C", "Ensolarado"),
        "sao paulo": ("22°C", "Nublado"),
        "rio": ("28°C", "Parcialmente nublado"),
        "brasilia": ("25°C", "Ventando"),
    }
    print(f"{C}  JuninhoWeather{RE}\n")
    cidade = input(f"{W}  Cidade: {RE}").strip().lower()
    os.system("clear")
    temp, clima = cidades.get(cidade, (f"{random.randint(18,38)}°C", random.choice(["Ensolarado","Nublado","Chuvoso","Ventando"])))
    print(f"{W}  {cidade.title()}{RE}")
    print(f"{Y}  {temp} - {clima}{RE}\n")
    print(f"{GR}  Umidade: {random.randint(40,90)}%\n  Vento: {random.randint(5,30)} km/h{RE}\n")
    input(f"{GR}  Enter para voltar...{RE}")

def hackermode():
    os.system("clear")
    print(f"{G}  HACKER MODE ATIVADO{RE}\n")
    time.sleep(0.5)
    for msg in ["Conectando ao servidor remoto...","Bypassando firewall...","Injetando payload...","Acessando banco de dados...","Descriptografando arquivos...","Coletando logs...","Apagando rastros...","Estabelecendo backdoor...","Download completo: 99GB","Missão concluída. Desconectando..."]:
        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        print(f"{G}  [{ip}] {msg}{RE}")
        time.sleep(random.uniform(0.3, 0.8))
    print(f"\n{Y}  [SUPERUSER] Operação finalizada.{RE}\n")
    input(f"{GR}  Enter para voltar...{RE}")

def top():
    os.system("clear")
    print(f"{C}  JuninhoTop - Processos{RE}\n{GR}  {'='*40}{RE}")
    print(f"{W}  PID    PROCESSO              CPU   RAM{RE}\n{GR}  {'='*40}{RE}")
    for pid, proc, cpu, ram in [("1001","junishshell","0.1%","12MB"),("1002","juninhokernel","2.3%","64MB"),("1003","firefox","5.1%","128MB"),("1004","juninhoOS-ui","1.2%","32MB"),("1005","pkg-daemon","0.0%","8MB"),("1006","weather-service","0.2%","16MB"),("1007","server-daemon","0.8%","24MB")]:
        print(f"  {pid}    {proc:<20} {cpu:<6} {ram}")
    print(f"{GR}  {'='*40}{RE}\n")
    input(f"{GR}  Enter para voltar...{RE}")

def server():
    global server_ativo, server_inicio
    os.system("clear")
    print(f"{C}  JuninhoServer{RE}\n{GR}  {'='*40}{RE}")
    if not server_ativo:
        print(f"{Y}  Servidor offline{RE}\n")
        op = input(f"{W}  Iniciar servidor? (s/n): {RE}").strip().lower()
        if op == "s":
            for s in ["Iniciando banco de dados...","Carregando módulo HTTP...","Configurando SSL...","Abrindo porta 80...","Abrindo porta 443...","Abrindo porta 8080...","Iniciando cache...","Configurando firewall...","Verificando integridade..."]:
                print(f"{GR}  {s}{RE}")
                time.sleep(0.4)
            server_ativo = True
            server_inicio = datetime.datetime.now()
            print(f"\n{G}  [OK] Servidor iniciado!")
            print(f"  IP Local:   192.168.0.{random.randint(1,254)}")
            print(f"  IP Público: 177.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")
            print(f"  Portas: 80, 443, 8080{RE}\n")
            input(f"{GR}  Enter para continuar...{RE}")
    else:
        while True:
            os.system("clear")
            uptime = datetime.datetime.now() - server_inicio
            seg = int(uptime.total_seconds())
            print(f"{C}  JuninhoServer - ONLINE{RE}\n{GR}  {'='*40}{RE}")
            print(f"{G}  Status:      ONLINE{RE}")
            print(f"{GR}  Uptime:      {seg//3600}h {(seg%3600)//60}m {seg%60}s")
            print(f"  Conexões:    {random.randint(50,500)}")
            print(f"  Requisições: {random.randint(1000,99999)}")
            print(f"  CPU:         {random.randint(1,40)}%")
            print(f"  RAM:         {random.randint(100,400)}MB / 512MB")
            print(f"  Banda:       {random.randint(1,100)} MB/s{RE}")
            print(f"{GR}  {'='*40}{RE}")
            print(f"{C}  [1] Logs ao vivo  [2] Serviços  [3] Conexões  [4] Parar  [0] Voltar{RE}")
            op = input(f"\n{W}  Escolha: {RE}").strip()
            if op == "1":
                os.system("clear")
                print(f"{C}  Logs ao vivo - Ctrl+C para parar{RE}\n")
                rotas = ["/","/api/data","/login","/home","/status","/upload","/download","/config"]
                try:
                    while True:
                        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                        metodo = random.choice(["GET","GET","GET","POST","PUT"])
                        codigo = random.choice([200,200,200,201,304])
                        ms = random.randint(5,150)
                        print(f"{GR}  [{datetime.datetime.now().strftime('%H:%M:%S')}]{RE} {ip} {C}{metodo}{RE} {random.choice(rotas)} {G}{codigo}{RE} {ms}ms")
                        time.sleep(random.uniform(0.2, 0.8))
                except KeyboardInterrupt:
                    print(f"\n{Y}  Logs pausados.{RE}\n")
                    input(f"{GR}  Enter para voltar...{RE}")
            elif op == "2":
                os.system("clear")
                print(f"{C}  Serviços rodando:{RE}\n")
                for nome, porta in [("HTTP","80"),("HTTPS","443"),("API","8080"),("Database","5432"),("Cache","6379"),("SSH","22")]:
                    print(f"  {G}[ONLINE]{RE} {nome:<12} porta {porta}")
                print()
                input(f"{GR}  Enter para voltar...{RE}")
            elif op == "3":
                os.system("clear")
                print(f"{C}  Conexões ativas:{RE}\n")
                for _ in range(8):
                    ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                    estado = random.choice(["ESTABLISHED","ESTABLISHED","ESTABLISHED","TIME_WAIT"])
                    cor = G if estado == "ESTABLISHED" else Y
                    print(f"  {ip}:{random.randint(1024,65535)}  {cor}{estado}{RE}")
                print()
                input(f"{GR}  Enter para voltar...{RE}")
            elif op == "4":
                print(f"\n{Y}  Parando servidor...{RE}")
                time.sleep(1)
                server_ativo = False
                server_inicio = None
                print(f"{R}  Servidor offline.{RE}\n")
                time.sleep(1)
                break
            elif op == "0":
                break

def terminal():
    global historico
    os.system("clear")
    print(f"{G}  JuninhoOS Terminal{RE}")
    print(f"{GR}  Digite 'ajuda' para ver os comandos{RE}\n")
    while True:
        cmd = input(f"{C}  SUPERUSER@juninhoOS:~$ {RE}").strip()
        if cmd:
            historico.append(cmd)
        if cmd == "sair":
            os.system("clear")
            break
        elif cmd == "ajuda":
            print(f"\n{W}  Comandos disponíveis:{RE}")
            print(f"{C}  pkg install/remove/list{GR} - gerenciar pacotes")
            print(f"{C}  firefox{GR}                - navegador")
            print(f"{C}  calc{GR}                   - calculadora")
            print(f"{C}  editor{GR}                 - editor de texto")
            print(f"{C}  weather{GR}                - previsão do tempo")
            print(f"{C}  hackermode{GR}             - modo hacker")
            print(f"{C}  top{GR}                    - processos")
            print(f"{C}  server{GR}                 - gerenciar servidor")
            print(f"{C}  ping <site>{GR}            - ping")
            print(f"{C}  whoami{GR}                 - info do usuário")
            print(f"{C}  history{GR}                - histórico")
            print(f"{C}  neofetch{GR}               - info do sistema")
            print(f"{C}  clear{GR}                  - limpar tela")
            print(f"{C}  ERRO INESPERADO{GR}        - ???{RE}\n")
        elif cmd == "clear":
            os.system("clear")
        elif cmd == "ERRO INESPERADO":
            os.system("clear")
            print(f"{R}  [  KERNEL PANIC  ]{RE}\n")
            print(f"{W}  Oops! Algo deu muito errado.{RE}")
            print(f"{GR}  Erro: UNEXPECTED_ERROR_0x000000")
            print(f"  Processo: junishshell.exe")
            print(f"  Endereço: 0xDEADBEEF{RE}\n")
            print(f"{R}  O sistema travou para evitar danos.{RE}")
            print(f"{Y}  Reinicie o JuninhoOS.{RE}\n")
            input(f"{GR}  Pressione Enter para reiniciar...{RE}")
            os.system("clear")
            print(f"{Y}  Reiniciando...{RE}")
            time.sleep(2)
            os.execv(sys.executable, ["python3"] + sys.argv)
        elif cmd == "neofetch":
            print(f"\n{C}  JuninhoOS v1.0.4{RE}")
            print(f"{W}  Kernel:{RE} JuninhoKernel 5.0")
            print(f"{W}  CPU:{RE}    JuninhoCore x86_64")
            print(f"{W}  RAM:{RE}    512MB")
            print(f"{W}  User:{RE}   SUPERUSER\n")
        elif cmd == "whoami":
            print(f"\n{W}  Usuário: {C}SUPERUSER{RE}")
            print(f"{W}  Grupo:   {C}root{RE}")
            print(f"{W}  Shell:   {C}junishshell 1.0{RE}")
            print(f"{W}  Home:    {C}/home/superuser{RE}\n")
        elif cmd == "history":
            print(f"\n{W}  Histórico:{RE}")
            for i, h in enumerate(historico[-10:]):
                print(f"{GR}  {i+1}. {h}{RE}")
            print()
        elif cmd.startswith("ping "):
            site = cmd[5:]
            print(f"\n{GR}  Pingando {site}...{RE}")
            for i in range(4):
                time.sleep(0.4)
                print(f"{G}  64 bytes de {site}: icmp_seq={i+1} tempo={random.randint(10,200)}ms{RE}")
            print()
        elif cmd == "firefox":
            if "firefox" not in instalados:
                print(f"{R}  firefox não instalado! Use: pkg install firefox{RE}\n")
            else:
                firefox()
                os.system("clear")
                print(f"{G}  JuninhoOS Terminal{RE}\n{GR}  Digite 'ajuda' para ver os comandos{RE}\n")
        elif cmd in ["calc","editor","weather","hackermode","top","server"]:
            {"calc":calc,"editor":editor,"weather":weather,"hackermode":hackermode,"top":top,"server":server}[cmd]()
            os.system("clear")
            print(f"{G}  JuninhoOS Terminal{RE}\n{GR}  Digite 'ajuda' para ver os comandos{RE}\n")
        elif cmd.startswith("pkg install "):
            p = cmd[12:]
            if p in instalados:
                print(f"{Y}  {p} já instalado!{RE}\n")
            elif p in pkgs:
                for msg in ["Buscando...","Baixando...","Instalando..."]:
                    print(f"{GR}  {msg}{RE}")
                    time.sleep(0.6)
                instalados.append(p)
                print(f"{G}  [OK] {p} instalado!{RE}\n")
            else:
                print(f"{R}  Pacote '{p}' não encontrado!{RE}\n")
        elif cmd.startswith("pkg remove "):
            p = cmd[11:]
            if p in instalados:
                instalados.remove(p)
                print(f"{G}  [OK] {p} removido!{RE}\n")
            else:
                print(f"{R}  {p} não está instalado!{RE}\n")
        elif cmd == "pkg list":
            for p in pkgs:
                st = f"{G}[instalado]{RE}" if p in instalados else f"{GR}[disponível]{RE}"
                print(f"  {p} {st}")
            print()
        elif cmd == "":
            continue
        else:
            print(f"{R}  Comando não encontrado: {cmd}{RE}\n")

while True:
    os.system("clear")
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{W}  JuninhoOS  {GR}{hora}{RE}")
    print(f"{GR}  {'='*28}{RE}")
    print(f"{C}  [1] Terminal")
    print(f"  [2] Bloco de Notas")
    print(f"  [3] Calculadora")
    print(f"  [4] Previsão do Tempo")
    print(f"  [5] Servidor")
    print(f"  [0] Desligar{RE}")
    print(f"{GR}  {'='*28}{RE}")
    op = input(f"\n{W}  Escolha: {RE}")
    if op == "1": terminal()
    elif op == "2": bloco_notas()
    elif op == "3": calc()
    elif op == "4": weather()
    elif op == "5": server()
    elif op == "0":
        os.system("clear")
        print(f"{Y}  Desligando JuninhoOS...{RE}\n")
        time.sleep(1)
        break
    else:
        print(f"{Y}  Opção inválida!{RE}\n")
        time.sleep(1)
