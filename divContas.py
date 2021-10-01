# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created on May 2019
@author: zemarchezi
"""
import numpy as np
import operator

__author__ = 'Jose P. Marchezi'


class DivideContas():
    """Dividir contas entre um grupo de pessoas
    Input:
        pagamentos -> Dicionario com a quantidade que cada um pagou

    Output:
        quanto cada um paga ao outro
    """

    def __init__(self, pagamentos):
        super(DivideContas, self).__init__()
        self.pag = pagamentos


    def divContas (self):
        total = np.sum(list(self.pag.values()))
        media = float(total / len(self.pag))

        receber = {}
        for i in self.pag.keys():
            receber[i] = self.pag[i] - media

        transacao = 0
        paga = {}
        while sorted(receber.items(), key=operator.itemgetter(1),reverse=True)[0][1]>0.001:
            transacao+=1
            receber_sort = sorted(receber.items(), key=operator.itemgetter(1),reverse=True)

            diff_maior_menor = receber_sort[0][1]+receber_sort[-1][1]
            if diff_maior_menor > 0:
                paga[receber_sort[-1][0] + " paga " + receber_sort[0][0]] = abs(receber_sort[-1][1])
                receber[receber_sort[-1][0]]=0
                receber[receber_sort[0][0]] = diff_maior_menor
            else:
                paga[receber_sort[-1][0] + " paga " + receber_sort[0][0]] =  abs(receber_sort[0][1])
                receber[receber_sort[-1][0]]=diff_maior_menor
                receber[receber_sort[0][0]]=0

        return paga


if __name__ == '__main__':


    pagamentos = {'P1': 200,
                  'P2': 50
                  }

    Div = DivideContas(pagamentos=pagamentos)
    deb = Div.divContas()

    print (deb)
