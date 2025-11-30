package model;

public class Terreno extends Financiamento {

    private double acrescimoInadimplencia;

    public double getAcrescimoInadimplencia() {
        return acrescimoInadimplencia;
    }

    public void setAcrescimoInadimplencia(double valor) {
        if (valor < 0) valor = 0;

        this.acrescimoInadimplencia = valor;
    }

    public Terreno(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        setAcrescimoInadimplencia(2);
    }

    public Terreno(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, double acrescimoInadimplencia) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        setAcrescimoInadimplencia(acrescimoInadimplencia);
    }

    @Override
    public double pagamentoMensal() {
        double valorPagamentoMes = super.pagamentoMensal();
        double taxaInadimplenciaPercentual = getAcrescimoInadimplencia() / 100;

        return valorPagamentoMes * (1 + taxaInadimplenciaPercentual);
    }
}
