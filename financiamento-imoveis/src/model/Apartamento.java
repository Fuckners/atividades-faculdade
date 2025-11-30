package model;

public class Apartamento extends Financiamento {

    private int vagasGaragem;

    public int getVagasGaragem() {
        return vagasGaragem;
    }

    public void setVagasGaragem(int vagasGaragem) {
        if (vagasGaragem < 0) vagasGaragem = 0;

        this.vagasGaragem = vagasGaragem;
    }

    private int numeroAndar;

    public int getNumeroAndar() {
        return numeroAndar;
    }

    public void setNumeroAndar(int numeroAndar) {
        if (numeroAndar < 0) numeroAndar = 0;

        this.numeroAndar = numeroAndar;
    }

    public Apartamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, int vagasGaragem, int numeroAndar) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        setVagasGaragem(vagasGaragem);
        setNumeroAndar(numeroAndar);
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
