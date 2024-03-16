import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter


janela = tk.Tk()
class PrincipalRAD:
    def __init__(self, win):
        self.lblNome=tk.Label(win, text="Nome do aluno")
        self.lblNota1=tk.Label(win, text="Nota 1")
        self.lblNota2=tk.Label(win, text="Nota 2")
        self.lblMedia=tk.Label(win, text="Média")
        self.txtNome=tk.Entry(bd=3)
        self.txtNota1=tk.Entry()
        self.txtNota2=tk.Entry()
        self.btnCalcular=tk.Button(win, text="Calcular média", command=self.fCalcularMedia).pack(padx=10, pady=10)

        self.dadosColunas = ("Aluno", "Nota 1", "Nota 2", "Média", "Situação")
        self.treeMedias = ttk.Treeview(win,
                                       columns=self.dadosColunas,
                                       selectmode="browse") 
        self.verscrlbar=tk.Scrollbar(win,
                                     orient="vertical",
                                    command=self.treeMedias.yview)
        self.verscrlbar.pack(side="right", fill="x")
        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)

        self.lblNome.place(x=100, y=50)
        self.txtNome.place(x=200, y=50)
        self.txtNome.pack(padx=10, pady=10)

        self.lblNota1.place(x=100, y=100)
        self.txtNota1.place(x=200, y=100)
        self.txtNota1.pack(padx=10, pady=10)

        self.lblNota2.place(x=100, y=150)
        self.txtNota2.place(x=200, y=150)
        self.txtNota2.pack(padx=10, pady=10)

        
        self.treeMedias.heading("Aluno", text="Aluno")
        self.treeMedias.heading("Nota 1", text="Nota 2")
        self.treeMedias.heading("Nota 2", text="Nota 2")
        self.treeMedias.heading("Média", text="Média")
        self.treeMedias.heading("Situação", text="Situação")

        self.treeMedias.column("Aluno", minwidth=0, width=100)
        self.treeMedias.column("Nota 1", minwidth=0, width=100)
        self.treeMedias.column("Nota 2", minwidth=0, width=100)
        self.treeMedias.column("Média", minwidth=0, width=100)
        self.treeMedias.column("Situação", minwidth=0, width=100)
        self.treeMedias.pack(padx=10, pady=10)

        self.id=0
        self.iid=0

        self.carregarDadosIniciais()
       
#-------------------------------------------------------------------------------------------------------       
    def carregarDadosIniciais(self):
        try:
            fsave = 'planilhaAlunos.xlsx'
            dados = pd.read_excel(fsave, engine='openpyxl')
            print(dados)

            nn=len(dados['Aluno'])
            for i in range(nn):
                print(i)
        
                nome = str(dados['Aluno'][i])
                nota1 = str(dados['Nota 1'][i])
                nota2 = str(dados['Nota 2'][i])
                media = str(dados['Média'][i])
                situacao = dados['Situação'][i]
                self.treeMedias.insert('', 'end',
                                            iid=self.iid,
                                           values=(nome, 
                                                    nota1,
                                                    nota2, 
                                                    media, 
                                                    situacao))
                self.id = self.id + 1
                self.iid = self.iid + 1
        
        except:
            print("Ainda não existem dados para carregar.")
    
    def fCalcularMedia(self):
        try:
            nome=self.txtNome.get()
            nota1=float(self.txtNota1.get())
            nota2=float(self.txtNota2.get())
            media, situacao = self.fVerificarSituacao(nota1, nota2)
            self.treeMedias.insert('', 'end',
                                   iid=self.iid,
                                   values=(nome,
                                           str(nota1),
                                           str(nota2), 
                                           str(media),
                                           situacao))
            self.iid=self.iid+1
            self.id=self.id+1
            self.fSalvarDados()
        except ValueError:
            print("Entre com valores válidos")
        finally:
            self.txtNome.delete(0, 'end')
            self.txtNota1.delete(0, 'end')
            self.txtNota2.delete(0, 'end')

    def fVerificarSituacao(self, nota1, nota2):
        media= (nota1+nota2)/2
        if(media>7.0):
            situacao = "Aprovado"
        elif(media>=5.0):
            situacao ="Em Recuperação"
        else:
            situacao = "Reprovado"
        
        return media, situacao
    
    def fSalvarDados(self):
        try:
            fsave='planilhaAlunos.xlsx'
            print(fsave)
            dados=[]
            for line in self.treeMedias.get_children():
                lstDados=[]
                for value in self.treeMedias.item(line)['values']:
                    lstDados.append(value)
                dados.append(lstDados)
            df = pd.DataFrame(data=dados, columns=self.dadosColunas)

            with pd.ExcelWriter(fsave) as writer:
                df.to_excel(writer)
                writer.save()
                
            #planilha = pd.ExcelWriter(fsave)
            #df.to_excel(planilha, 'dados', index=False)
            #planilha.save()
            
            print("Dados salvos")
        except:
            print("Não foi possivel salvar os dados")
        

janela.geometry("850x300")
principal=PrincipalRAD(janela)
janela.title("Bem vindo ao RAD")
janela.mainloop()