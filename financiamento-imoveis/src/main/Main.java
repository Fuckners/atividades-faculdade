package main;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import model.Apartamento;
import model.Casa;
import model.Financiamento;
import model.Terreno;

import util.FileManager;
import util.ObjectFileManager;
import util.TextFileManager;
import util.InterfaceUsuario;

public class Main {
    public static void main(String[] args) {
        final Scanner sc = new Scanner(System.in);

        final InterfaceUsuario interfaceUsuario = new InterfaceUsuario(sc);

        final List<Financiamento> financiamentos = new ArrayList<Financiamento>();

        final String NOME_ARQUIVO_TEXTO = "financiamentos.txt";
        final String NOME_ARQUIVO_OBJETOS = "financiamentos.objetos";

        final TextFileManager textManager = new TextFileManager(NOME_ARQUIVO_TEXTO);
        final ObjectFileManager objectManager = new ObjectFileManager(NOME_ARQUIVO_OBJETOS);

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

            textManager.escrever(financiamento.toString());
            objectManager.escrever(financiamento);

            totalImoveis += financiamento.getValorImovel();
            totalFinanciamentos += financiamento.pagamentoTotal();
        }

        objectManager.finalizarOutputStream();
        textManager.finalizarOutputStream();

        List<String> linhasLidas = textManager.ler();
        System.out.println("\nConteúdo do arquivo de texto:");
        for (String linha : linhasLidas) {
            System.out.println(linha);
        }

        List<Object> objetosLidos = objectManager.ler();
        System.out.println("\nConteúdo do arquivo de objetos:");
        for (Object obj : objetosLidos) {
            System.out.println(obj.toString());
        }

        textManager.finalizarTudo();
        objectManager.finalizarTudo();

        System.out.printf("Total de todos os imóveis: R$ %.2f\n", totalImoveis);
        System.out.printf("Total de todos os financiamentos: R$ %.2f\n", totalFinanciamentos);

        sc.close();
    }
}