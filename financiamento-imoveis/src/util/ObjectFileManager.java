package util;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ObjectFileManager extends FileManager {

    private ObjectOutputStream writeStream = null;

    private ObjectInputStream readStream = null;

    public ObjectFileManager(String fileName) {
        super(fileName);
    }

    public void escrever(Object conteudo) {
        iniciarOutputStream();

        try {
            writeStream.writeObject(conteudo);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public List<Object> ler() {
        iniciarInputStream();

        List<Object> items = new ArrayList<Object>();

        try {
            Object conteudo;
            while (true) {
                conteudo = readStream.readObject();
                items.add(conteudo);
            }
        } catch (EOFException e) {
            // fim do arquivo
        } catch (Exception e) {
            e.printStackTrace();
            return new ArrayList<Object>();
        }

        return items;
    }

    public void iniciarInputStream() {
        if (readStream != null) {
            return;
        }

        try {
            FileInputStream fileInputStream = new FileInputStream(getFileName());
            readStream = new ObjectInputStream(fileInputStream);
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
            FileOutputStream outputStream = new FileOutputStream(getFileName());
            writeStream = new ObjectOutputStream(outputStream);
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
