package util;

import java.util.Scanner;

public class InterfaceUsuario {

    Scanner sc;

    public InterfaceUsuario(Scanner sc) {
        this.sc = sc;
    }
    public double pedirValorImovel() {
        System.out.print("Digite o valor total do imóvel: ");
        double valorImovel = sc.nextDouble();

        return valorImovel;
    }

    // Fiquei na dúvida se o financiamento pode ter apenas anos inteiros ou se posso financiar em 1 ano e meio, por exemplo.
    // Mas decidi tratar apenas anos inteiros 👍
    public int pedirPrazoFinanciamentoAno() {
        System.out.print("Digite quantos anos até financiar: ");
        int prazoFinanciamentoAno = sc.nextInt();

        return prazoFinanciamentoAno;
    }

    public double pedirTaxaJurosAno() {
        System.out.print("Digite a taxa de justos anual: ");
        double taxaJurosAno = sc.nextDouble();

        return taxaJurosAno;
    }
}
