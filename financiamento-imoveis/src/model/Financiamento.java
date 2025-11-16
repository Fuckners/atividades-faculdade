package model;

public class Financiamento {
    private double valorImovel;

    public double getValorImovel() {
        return valorImovel;
    }

    private int prazoFinanciamentoAnos;

    public int getPrazoFinanciamentoAnos() {
        return prazoFinanciamentoAnos;
    }

    // Porcentagem
    private double taxaJurosAnual;

    public double getTaxaJurosAnual() {
        return taxaJurosAnual;
    }

    public Financiamento(double valorImovel, int prazoFinanciamentoAnos) {
        this(valorImovel, prazoFinanciamentoAnos, 10.0f);
    }

    public Financiamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        this.valorImovel = valorImovel;
        this.prazoFinanciamentoAnos = prazoFinanciamentoAnos;
        this.taxaJurosAnual = taxaJurosAnual;
    }

    public double getPrazoFinanciamentoMes() {
        return prazoFinanciamentoAnos * 12;
    }

    public double getTaxaAnual() {
        return valorImovel * (taxaJurosAnual / 100);
    }

    public double getTaxaMes() {
        return getTaxaAnual() / 12;
    }

    public double pagamentoMensal() {
        double valorPagamentoBrutoMes = valorImovel / getPrazoFinanciamentoMes();

        // Sei que o cálculo está diferente do enunciado da atividade
        // Mas é por que acredito que estava errado

        return valorPagamentoBrutoMes + getTaxaMes();
    }

    public double pagamentoTotal() {
        double pagamentoMensal = pagamentoMensal();

        return pagamentoMensal * getPrazoFinanciamentoMes();
    }

    public void mostrar() {
        System.out.printf("Valor total do imóvel: R$ %.2f\n", valorImovel);
        System.out.printf("Valor final do financiamento: R$ %.2f\n", pagamentoTotal());
        System.out.printf("Valor parcela mensal do financiamento: R$ %.2f\n", pagamentoMensal());
    }
}
