package com.themaskedcrusader.advent15.util;

import java.io.*;

public class AdventUtils {

    public String get_first_line(File directory, String problem) {
        String ret = "";
        File input = new File(directory.getAbsolutePath() + File.separator + problem.concat(".txt"));
        try {
            BufferedReader in = new BufferedReader(new FileReader(input));
            ret = in.readLine();
            in.close();

        } catch (IOException e) {
            System.err.println("Could not read from file, Cannot Continue");
            e.printStackTrace();
            System.exit(Constants.FILE_READ_ERROR);
        }
        return ret;
    }

}
