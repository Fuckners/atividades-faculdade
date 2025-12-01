package model;

import util.AumentoMaiorQueJurosException;

public class Casa extends Financiamento {

    private double areaConstruida;

    public double getAreaConstruida() {
        return areaConstruida;
    }

    public void setAreaConstruida(double areaConstruida) {
        if (areaConstruida <= 0) areaConstruida = 1;

        this.areaConstruida = areaConstruida;
    }

    private double areaTerreno;

    public double getAreaTerreno() {
        return areaTerreno;
    }

    public void setAreaTerreno(double areaTerreno) {
        if (areaTerreno <= 0) areaTerreno = 1;

        if (areaTerreno < getAreaConstruida()) {
            areaTerreno = getAreaConstruida();
        }

        this.areaTerreno = areaTerreno;
    }

    private double valorSeguroMensal;

    public double getValorSeguroMensal() {
        return valorSeguroMensal;
    }

    public void setValorSeguroMensal(double valorSeguroMensal) {
        if (valorSeguroMensal <= 0) valorSeguroMensal = 0;

        this.valorSeguroMensal = valorSeguroMensal;
    }

    public Casa(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, double areaConstruida, double areaTerreno, double valorSeguroMensal) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        setAreaConstruida(areaConstruida);
        setAreaTerreno(areaTerreno);
        setValorSeguroMensal(valorSeguroMensal);
    }

    public Casa(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, double areaConstruida, double areaTerreno) {
        this(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual, areaConstruida, areaTerreno, 80);
    }

    private void validaPagamentoMensal(double taxaMes, double valorSeguroMensal) throws AumentoMaiorQueJurosException {
        if (valorSeguroMensal > taxaMes / 2) {
            throw new AumentoMaiorQueJurosException("O valor do seguro mensal não pode ser maior que metade da taxa mensal.");
        }
    }

    @Override
    public double pagamentoMensal() {
        double valorPagamentoBrutoMes = getValorImovel() / getPrazoFinanciamentoMes();
        double taxaMes = getTaxaMes();
        double valorAcrescimoSeguro = getValorSeguroMensal();

        try {
            validaPagamentoMensal(taxaMes, valorAcrescimoSeguro);
        } catch (AumentoMaiorQueJurosException e) {
            System.out.println(e.getMessage());
            valorAcrescimoSeguro = taxaMes;
        }

        return valorPagamentoBrutoMes + taxaMes + valorAcrescimoSeguro;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        String base = super.toString();

        sb
            .append(base)
            .append(String.format("| Área Construída: %.2f m² ", getAreaConstruida()))
            .append(String.format("| Área do Terreno: %.2f m² ", getAreaTerreno()))
            .append(String.format("| Valor Seguro Mensal: R$ %.2f ", getValorSeguroMensal()));

        return sb.toString();
    }
}
