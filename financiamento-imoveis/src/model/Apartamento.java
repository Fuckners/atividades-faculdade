package model;

public class Apartamento extends Financiamento {
    public Apartamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
    }

    @Override
    public double pagamentoMensal() {
        // Cálculo considerando PRICE
        double taxaJurosMes = getTaxaJurosAnual() / 100 / 12;
        double juros = 1 + taxaJurosMes;
        double jurosComposto = Math.pow(juros, getPrazoFinanciamentoMes());

        double valorPagamentoMes = (getValorImovel() * jurosComposto) / jurosComposto - 1;

        return valorPagamentoMes;
    }
}
