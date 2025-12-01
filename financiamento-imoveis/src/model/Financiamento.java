package model;

public abstract class Financiamento {
    private double valorImovel;

    public void setValorImovel(double valor) {
        if (valor <= 0) valor = 0;

        this.valorImovel = valor;
    }
    public double getValorImovel() {
        return valorImovel;
    }

    private int prazoFinanciamentoAnos;

    public int getPrazoFinanciamentoAnos() {
        return prazoFinanciamentoAnos;
    }

    public void setPrazoFinanciamentoAnos(int valor) {
        if (valor <= 0) valor = 0;

        this.prazoFinanciamentoAnos = valor;
    }

    // Porcentagem
    private double taxaJurosAnual;

    public double getTaxaJurosAnual() {
        return taxaJurosAnual;
    }

    public void setTaxaJurosAnual(double valor) {
        if (valor <= 0) valor = 0;

        this.taxaJurosAnual = valor;
    }

    public Financiamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        setValorImovel(valorImovel);
        setPrazoFinanciamentoAnos(prazoFinanciamentoAnos);
        setTaxaJurosAnual(taxaJurosAnual);
    }

    public double getPrazoFinanciamentoMes() {
        return getPrazoFinanciamentoAnos() * 12;
    }

    public double getTaxaAnual() {
        return getValorImovel() * (getTaxaJurosAnual() / 100);
    }

    public double getTaxaMes() {
        return getTaxaAnual() / 12;
    }

    public abstract double pagamentoMensal();

    public double pagamentoTotal() {
        double pagamentoMensal = pagamentoMensal();

        return pagamentoMensal * getPrazoFinanciamentoMes();
    }

    public void mostrar() {
        System.out.println("=".repeat(55));
        System.out.printf("Valor total do imóvel: R$ %.2f\n", getValorImovel());
        System.out.printf("Valor final do financiamento: R$ %.2f\n", pagamentoTotal());
        System.out.printf("Valor parcela mensal do financiamento: R$ %.2f\n", pagamentoMensal());
        System.out.println("=".repeat(55));
        System.out.println();
    }

    public String toString() {

        StringBuilder sb = new StringBuilder();

        sb
            .append(String.format("| Valor Imóvel: R$ %.2f ", getValorImovel()))
            .append(String.format("| Prazo: %d anos ", getPrazoFinanciamentoAnos()))
            .append(String.format("| Taxa Juros Anual: %.2f ", getTaxaJurosAnual()))
            .append(String.format("| Pagamento Total: %.2f ", pagamentoTotal()))
            .append(String.format("| Pagamento Mensal: %.2f ", pagamentoMensal()));

        return sb.toString();
    }
}
