package model;

public class Terreno extends Financiamento {

    private String tipoZona; // comercial | residencial

    public String getTipoZona() {
        return tipoZona;
    }

    public void setTipoZona(String tipoZona) {
//        if (!tipoZona.equals("residencial") && !tipoZona.equals("comercial")) {
//            throw alguma coisa (?)
//            return;
//        }

        this.tipoZona = tipoZona;
    }

    private double acrescimoInadimplencia;

    public double getAcrescimoInadimplencia() {
        return acrescimoInadimplencia;
    }

    public void setAcrescimoInadimplencia(double valor) {
        if (valor < 0) valor = 0;

        this.acrescimoInadimplencia = valor;
    }

    public Terreno(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, String tipoZona, double acrescimoInadimplencia) {
        super(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual);
        setTipoZona(tipoZona);
        setAcrescimoInadimplencia(acrescimoInadimplencia);
    }

    public Terreno(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual, String tipoZona) {
        this(valorImovel, prazoFinanciamentoAnos, taxaJurosAnual, tipoZona, 2);
    }

    @Override
    public double pagamentoMensal() {
        double valorPagamentoBrutoMes = getValorImovel() / getPrazoFinanciamentoMes();

        double valorPagamentoMes = valorPagamentoBrutoMes + getTaxaMes();

        double taxaInadimplenciaPercentual = getAcrescimoInadimplencia() / 100;

        return valorPagamentoMes * (1 + taxaInadimplenciaPercentual);
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();

        String base = super.toString();

        sb
            .append(base)
            .append(String.format("| Tipo de Zona: %s ", getTipoZona()))
            .append(String.format("| Acréscimo por Inadimplência: %.2f ", getAcrescimoInadimplencia()));

        return sb.toString();
    }
}
