package main;

import model.Financiamento;
import util.InterfaceUsuario;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        InterfaceUsuario interfaceUsuario = new InterfaceUsuario(sc);

        double valorImovel = interfaceUsuario.pedirValorImovel();
        int prazoFinanciamentoAno = interfaceUsuario.pedirPrazoFinanciamentoAno();
        double taxaJurosAno = interfaceUsuario.pedirTaxaJurosAno();

        Financiamento financiamento = new Financiamento(valorImovel, prazoFinanciamentoAno, taxaJurosAno);

        System.out.printf("O valor total do seu financiamento ficou em R$ %.2f e você terá que pagar R$ %.2f por mês.", financiamento.calcularPagamentoTotal(), financiamento.calcularPagamentoMensal());

        sc.close();
    }
}