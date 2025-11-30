package main;

import model.Apartamento;
import model.Casa;
import model.Financiamento;
import model.Terreno;
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

        double valorImovel = interfaceUsuario.pedirValorImovel();
        int prazoFinanciamentoAno = interfaceUsuario.pedirPrazoFinanciamentoAno();
        double taxaJurosAno = interfaceUsuario.pedirTaxaJurosAno();

        financiamentos.add(new Casa(valorImovel, prazoFinanciamentoAno, taxaJurosAno, 200, 300));
        financiamentos.add(new Casa(valorImovel, prazoFinanciamentoAno, taxaJurosAno, 100, 150));
        financiamentos.add(new Apartamento(valorImovel, prazoFinanciamentoAno, taxaJurosAno, 2, 505));
        financiamentos.add(new Apartamento(valorImovel, prazoFinanciamentoAno, taxaJurosAno, 1, 404));
        financiamentos.add(new Terreno(valorImovel, prazoFinanciamentoAno, taxaJurosAno, "comercial"));

        for (Financiamento financiamento : financiamentos) {
            financiamento.mostrar();

            totalImoveis += financiamento.getValorImovel();
            totalFinanciamentos += financiamento.pagamentoTotal();
        }

        System.out.printf("Total de todos os imóveis: R$ %.2f\n", totalImoveis);
        System.out.printf("Total de todos os financiamentos: R$ %.2f\n", totalFinanciamentos);

        sc.close();
    }
}