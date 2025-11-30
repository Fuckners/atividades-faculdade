package model;

public class Casa extends Financiamento {
    private double valorSeguroMensal;

    public double getValorSeguroMensal() {
        return valorSeguroMensal;
    }

    public void setValorSeguroMensal(double valorSeguroMensal) {
        if (valorSeguroMensal <= 0) valorSeguroMensal = 0;

        this.valorSeguroMensal = valorSeguroMensal;
    }

    public Casa(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, double valorSeguroMensal) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        setValorSeguroMensal(valorSeguroMensal);
    }

    public Casa(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        this(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual, 80);
    }

    @Override
    public double pagamentoMensal() {
        return super.pagamentoMensal() + getValorSeguroMensal();
    }
}
