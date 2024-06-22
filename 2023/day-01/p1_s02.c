/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

// AoC 2023 / Day 1 / Part 1
//
// https://adventofcode.com/2023/day/1

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// function declarations
int main(int argc, char **argv);
int calibration_value(char *line);
int find_digit(char *line, bool reverse);

// constants
static const char INPUT_FILE_NAME[] = "input.txt";


int main(int argc, char **argv)
{
        int sum_value = 0;

        FILE *fh_input;
        const int LINE_LENGTH = 100;
        char line[LINE_LENGTH];

        fh_input = fopen(INPUT_FILE_NAME, "r");
        if (fh_input == NULL) {
                exit(EXIT_FAILURE);
        }

        while (fgets (line , LINE_LENGTH , fh_input) != NULL) {
                //printf("line: '%s'\n", line);
                int cal_val = calibration_value(line);
                //printf("cal. val.: '%d'\n", cal_val);
                sum_value += cal_val;
        }

        fclose(fh_input);

        printf("%d\n", sum_value);

        return EXIT_SUCCESS;
}


int calibration_value(char *line)
{
        return (find_digit(line, false) * 10) + find_digit(line, true);
}


int find_digit(char *line, bool reverse)
{
        int length = (int) strlen(line);

        int i, start, end, step;
        if (!reverse) {
                start = 0;
                end = length + 1;
                step = 1;
        }
        else {
                start = length;
                end = -1;
                step = -1;
        }
        i = start;

        //printf("length: '%d', start: '%d', end: '%d', step: '%d'\n", length, start, end, step);

        while (i != end) {
                //printf("    char %d : '%c'\n", i, line[i]);

                switch (line[i]) {
                        case '0':
                                return 0;
                        case '1':
                                return 1;
                        case '2':
                                return 2;
                        case '3':
                                return 3;
                        case '4':
                                return 4;
                        case '5':
                                return 5;
                        case '6':
                                return 6;
                        case '7':
                                return 7;
                        case '8':
                                return 8;
                        case '9':
                                return 9;
                        default:
                                i += step;
                }
        }

        exit(EXIT_FAILURE);
}
