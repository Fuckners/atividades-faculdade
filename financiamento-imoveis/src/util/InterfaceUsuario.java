package util;

import java.util.Scanner;

public class InterfaceUsuario {

    private Scanner sc;

    public InterfaceUsuario(Scanner sc) {
        this.sc = sc;
    }

    public void validaValorImovel(double valorImovel) throws ValorImovelNegativoException {
        if (valorImovel <= 0) {
            throw new ValorImovelNegativoException("O valor do imóvel precisa ser maior que zero.");
        }
    }

    public double pedirValorImovel() {
        double valorImovel;

        while (true) {
            System.out.print("Digite o valor total do imóvel (Sem limite máximo de valor): ");
            valorImovel = sc.nextDouble();

            try {
                validaValorImovel(valorImovel);
                break;
            } catch (ValorImovelNegativoException error) {
                System.out.println(error.getMessage());
            }
        }

        return valorImovel;
    }

    public void validaPrazoFinanciamento(int prazoFinanciamentoAno) throws PrazoFinanciamentoInvalidoException {
        if (prazoFinanciamentoAno <= 0) {
            throw new PrazoFinanciamentoInvalidoException("O prazo do financiamento precisa ser maior que zero.");
        }

        if (prazoFinanciamentoAno > 50) {
            throw new PrazoFinanciamentoInvalidoException("O prazo de financiamento precisa ser menor que 50 anos. Dúvido que vá viver muito mais que isso.");
        }
    }

    // Fiquei na dúvida se o financiamento pode ter apenas anos inteiros ou se posso financiar em 1 ano e meio, por exemplo.
    // Mas decidi tratar apenas anos inteiros 👍
    public int pedirPrazoFinanciamentoAno() {
        int prazoFinanciamentoAno;

        while (true) {
            System.out.print("Digite quantos anos até financiar: ");
            prazoFinanciamentoAno = sc.nextInt();

            try {
                validaPrazoFinanciamento(prazoFinanciamentoAno);
                break;
            } catch (PrazoFinanciamentoInvalidoException error) {
                System.out.println(error.getMessage());
            }
        }

        return prazoFinanciamentoAno;
    }

    public void validaTaxaJuros(double taxaJurosAno) throws TaxaJurosInvalidaException {
        if (taxaJurosAno <= 0) {
            throw new TaxaJurosInvalidaException("A taxa de juros anual precisa ser positiva.");
        }

        if (taxaJurosAno >= 200) {
            throw new TaxaJurosInvalidaException("A taxa de juros anual precisa ser menor que 200. É financiamento ou agiotagem?");
        }
    }

    public double pedirTaxaJurosAno() {
        double taxaJurosAno;

        while (true) {
            System.out.print("Digite a taxa de juros anual: ");
            taxaJurosAno = sc.nextDouble();

            try {
                validaTaxaJuros(taxaJurosAno);
                break;
            } catch (TaxaJurosInvalidaException error) {
                System.out.println(error.getMessage());
            }
        }

        return taxaJurosAno;
    }
}
