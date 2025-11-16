package util;

import java.util.Scanner;

public class InterfaceUsuario {

    private Scanner sc;

    public InterfaceUsuario(Scanner sc) {
        this.sc = sc;
    }
    public double pedirValorImovel() {
        double valorImovel;
        boolean ehNegativo;

        while (true) {
            System.out.print("Digite o valor total do imóvel (Sem limite máximo de valor): ");
            valorImovel = sc.nextDouble();

            ehNegativo = valorImovel <= 0;

            if (ehNegativo) {
                System.out.println("O valor do imóvel precisa ser maior que zero.");
                continue;
            }

            break;
        };

        return valorImovel;
    }

    // Fiquei na dúvida se o financiamento pode ter apenas anos inteiros ou se posso financiar em 1 ano e meio, por exemplo.
    // Mas decidi tratar apenas anos inteiros 👍
    public int pedirPrazoFinanciamentoAno() {
        int prazoFinanciamentoAno;

        int maxAnos = 50;

        boolean ehNegativo;
        boolean ehMaiorMax;

        while (true) {
            System.out.print("Digite quantos anos até financiar: ");
            prazoFinanciamentoAno = sc.nextInt();

            ehNegativo = prazoFinanciamentoAno <= 0;
            ehMaiorMax = prazoFinanciamentoAno > maxAnos;

            if (ehNegativo) {
                System.out.println("O prazo do financiamento precisa ser maior que zero.");
                continue;
            }

            if (ehMaiorMax) {
                System.out.printf("O prazo de financiamento precisa ser menor que %d anos. Dúvido que vá viver muito mais que isso.\n", maxAnos);
                continue;
            }

            break;
        };

        return prazoFinanciamentoAno;
    }

    public double pedirTaxaJurosAno() {
        double taxaJurosAno;

        int max = 200;

        boolean ehNegativo;
        boolean ehMaiorMax;

        while (true) {
            System.out.print("Digite a taxa de justos anual: ");
            taxaJurosAno = sc.nextDouble();

            ehNegativo = taxaJurosAno <= 0;
            ehMaiorMax = taxaJurosAno >= max;

            if (ehNegativo) {
                System.out.print("A taxa de juros anual precisa ser positiva.");
                continue;
            }

            if (ehMaiorMax) {
                System.out.printf("A taxa de juros anual precisa ser menor que %d. É financiamento ou agiotagem?\n", max);
                continue;
            }

            break;
        };

        return taxaJurosAno;
    }
}
