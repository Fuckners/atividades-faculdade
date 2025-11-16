package main;

import model.Financiamento;
import util.InterfaceUsuario;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        InterfaceUsuario interfaceUsuario = new InterfaceUsuario(sc);

        List<Financiamento> financiamentos = new ArrayList<Financiamento>();

        double totalImoveis = 0;
        double totalFinanciamentos = 0;

        int quantidadeFinanciamentos = 4;

        for (int contador = 0; contador < quantidadeFinanciamentos; contador++) {
            double valorImovel = interfaceUsuario.pedirValorImovel();
            int prazoFinanciamentoAno = interfaceUsuario.pedirPrazoFinanciamentoAno();
            double taxaJurosAno = interfaceUsuario.pedirTaxaJurosAno();

            Financiamento financiamento = new Financiamento(valorImovel, prazoFinanciamentoAno, taxaJurosAno);

            financiamento.mostrar();

            totalImoveis += financiamento.getValorImovel();
            totalFinanciamentos += financiamento.pagamentoTotal();

            financiamentos.add(financiamento);
        }

        System.out.printf("Total de todos os imóveis: R$ %.2f\n", totalImoveis);
        System.out.printf("Total de todos os financiamentos: R$ %.2f\n", totalFinanciamentos);

        sc.close();
    }
}