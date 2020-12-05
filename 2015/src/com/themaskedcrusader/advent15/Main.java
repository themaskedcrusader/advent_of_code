package com.themaskedcrusader.advent15;

import com.themaskedcrusader.advent15.days.DayOne;

import java.io.File;

public class Main {

    private static void usage() {
        System.out.println("Usage Note: First parameter must be the full path to the input directory");
        System.out.println("The input file must be named: day_<number>.txt");
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            usage();
        } else {
            File inputDirectory = new File(args[0]);
            new DayOne().execute(inputDirectory);


        }
    }
}
