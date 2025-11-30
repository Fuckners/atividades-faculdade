package model;

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

    @Override
    public double pagamentoMensal() {
        double valorPagamentoBrutoMes = getValorImovel() / getPrazoFinanciamentoMes();

        return valorPagamentoBrutoMes + getTaxaMes() + getValorSeguroMensal();
    }
}
