import nextcord
#! acabei de descobrir a existencia do interactive help do python
#! funciona com modulos, classes, funcoes e metodos
#* print( object .__doc__) # mostra a documentacao do objeto
#* help( object ) -> information about object, or about the interpreter if no argument is given.
#* dir( object ) -> list of attributes and methods of object, and of attributes inherited from its class.
#? não necessariamente vão ser iguais e dependendo um pode ser mais completo que o outro
#! help(nextcord.slash_command)
#print("-"*100)
#help(input)
#print("-"*100)
#print(input.__doc__)


#* fazer help da sua propria funcao
#* https://stackoverflow.com/questions/12627118/python-how-to-get-the-docstring-of-a-function
#* para deixar um parametro como opcional, basta colocar um valor padrao nele   
def soma(a=0, b=0, c=0):
    """
    docstring da funcao soma
    soma dois ou tres numeros
    printa o resultado
    """
    rsoma = a + b + c
    print(rsoma)

soma(1, 1, 1)# resultado 3
soma(1, 1)#resulta em 2
soma(1)#resposta: 1
