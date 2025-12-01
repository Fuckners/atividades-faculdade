package util;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class TextFileManager extends FileManager {

    private FileWriter writeStream = null;

    private FileReader readStream = null;

    public TextFileManager(String fileName) {
        super(fileName);
    }

    public void escrever(String conteudo) {
        iniciarOutputStream();

        try {
            writeStream.write(conteudo + "\n");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public List<String> ler() {
        iniciarInputStream();

        BufferedReader bufferedReader = new BufferedReader(readStream);
        List<String> linhas = new ArrayList<String>();

        try {
            String linha;
            while ((linha = bufferedReader.readLine()) != null) {
                linhas.add(linha);
            }
        } catch (Exception e) {
            e.printStackTrace();
            return new ArrayList<String>();
        }

        return linhas;
    }

    public void iniciarInputStream() {
        if (readStream != null) {
            return;
        }

        try {
            readStream = new FileReader(getFileName());
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void finalizarInputStream() {
        if (readStream == null) {
            return;
        }

        try {
            readStream.close();
            readStream = null;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void iniciarOutputStream() {
        if (writeStream != null) {
            return;
        }

        try {
            writeStream = new FileWriter(getFileName());
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void finalizarOutputStream() {
        if (writeStream == null) {
            return;
        }

        try {
            writeStream.flush();
            writeStream.close();
            writeStream = null;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
