#! usr/bin bash
#!-*- CODING:UTF-8 -*-

## Excepciones
## TODO: Crear excepciones para cada uno de los errores.



def calculoReposicionesSoloCapital(numIntentos,profit,inicio=None,capitalTotalRiesgo=None):
    # se mitiga el riesgo usando solo reposiciones que recuperen el capital perdido
    # pero solo se cuenta la ganancia de la ultima operacion
    # para casos de mucho fallo.
    if inicio == None and capitalTotalRiesgo == None:
        raise  NameError("Faltan datos correspondientes al capital")

    try:

        if numIntentos < 0 or profit < 0:
            raise NameError("numIntentos debe ser mayor a 0 o su profit es bajo, reingrese correctamente los datos")

        inversiones = []
        inversiones.append(inicio)
        # La formula a utilizar es:
        # x(n+1) = (100-p)/100 * (sumatoria desde i=0 hasta n de x(i) + p/100 * inicio)
        for i in range(1,numIntentos):
            res = (sum(inversiones) + inicio + profit/100 * inicio) *100/(100+profit)
            inversiones.append(round(res,2))

    except Exception as e:
        print(e)
    finally:
        return inversiones





if __name__ == '__main__':
    print(calculoReposicionesSoloCapital(10,80,1))
