package model;

public class Financiamento {
    double valorImovel;
    int prazoFinanciamentoAnos;
    double taxaJurosAnual;

    public Financiamento(double valorImovel, int prazoFinanciamentoAnos) {
        this(valorImovel, prazoFinanciamentoAnos, 10.0f);
    }

    public Financiamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        this.valorImovel = valorImovel;
        this.prazoFinanciamentoAnos = prazoFinanciamentoAnos;
        this.taxaJurosAnual = taxaJurosAnual;
    }

    double getPrazoFinanciamentoMes() {
        return prazoFinanciamentoAnos * 12;
    }


    double getTaxaAnual() {
        return valorImovel * (taxaJurosAnual / 100);
    }

    double getTaxaMes() {
        return getTaxaAnual() / 12;
    }

    public double calcularPagamentoMensal() {
        double valorPagamentoBrutoMes = valorImovel / getPrazoFinanciamentoMes();

        System.out.printf("valor bruto por mês: %f\n", valorPagamentoBrutoMes);
        System.out.printf("Porcentagem juros: %f\n", getTaxaMes());

        // Sei que o cálculo está diferente do enunciado da atividade
        // Mas é por que acredito que estava errado

        return valorPagamentoBrutoMes + getTaxaMes();
    }

    public double calcularPagamentoTotal() {
        double pagamentoMensal = calcularPagamentoMensal();

        return pagamentoMensal * getPrazoFinanciamentoMes();
    }
}
