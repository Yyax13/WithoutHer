#importando a lib "apt"
import misc.apt

#instalando as dependencias
package_001 = "yollor"
misc.apt.pip_update(package_001)
package_002 = "requests"
misc.apt.pip_update(package_002)
package_003 = "pyautogui"
misc.apt.pip_update(package_003)
package_004 = "selenium"
misc.apt.pip_update(package_004)

#importando a lib "misc" e a lib "prints"
import misc.tools
import misc.prints

#limpando a tela e exibindo o banner
misc.tools.clear()
misc.prints.banner()

#importando a lib "login"
import misc.login

#iniciando o sistema de login
login_checker = misc.login.start()

#verificando o login
if login_checker == "passCompleteStatus": 
    
    #limpando a tela
    misc.tools.clear()
    misc.prints.banner()
    
    #importando as libs "brute" e "server"
    import misc.brute
    
    #perguntando oq ele quer
    brute_choose = misc.brute.opt()
    
    #verificando a escolha do usuario
    if brute_choose == "dirs":
    
        #faz o brute force em diretórios
        common = "misc/common.txt"
        
        misc.brute.dirs(url="https://yyax13.github.io/brute-force-target/", wordlist=common)
        
    elif brute_choose == "login":
        
        #faz o brute force no login
        misc.brute.login()
        
        
    else:
        
        #exibe o erro
        print(f"ERRO")
        
elif login_checker == "non":
    
    #sai da ferramenta
    misc.misc.exit()
    
else:
    
    #exibe o erro
    print(f"ERRO")