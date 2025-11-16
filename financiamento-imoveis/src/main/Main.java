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

        financiamento.mostrar();

        sc.close();
    }
}