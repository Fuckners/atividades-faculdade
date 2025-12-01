package util;

public abstract class FileManager {
    protected final int maxFileNameLength = 50;
    private String fileName;

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        if (fileName.length() > maxFileNameLength) {
            fileName = fileName.substring(0, maxFileNameLength);
            System.out.printf("O nome do arquivo foi truncado para 50 caracteres. (%s)\n", fileName);
        }

        this.fileName = fileName;
    }

    public FileManager(String fileName) {
        setFileName(fileName);
    }

//    public abstract void escrever(Object conteudo);
//    public abstract void escrever(String conteudo);

    public abstract void iniciarInputStream();

    public abstract void finalizarInputStream();

    public abstract void iniciarOutputStream();
    public abstract void finalizarOutputStream();

    public void finalizarTudo() {
        finalizarInputStream();
        finalizarOutputStream();
    }
}
