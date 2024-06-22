// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// AoC 2023 / Day 1 / Part 1 / Solution 5 (Zig)
//
// https://adventofcode.com/2023/day/1

const std = @import("std");
const stdout = std.io.getStdOut().writer();

const FileOpenError = error{ AccessDenied, Unexpected, FileTooBig, NoSpaceLeft, DeviceBusy, SystemResources, WouldBlock, DiskQuota, InputOutput, InvalidArgument, BrokenPipe, OperationAborted, NotOpenForWriting, LockViolation, ConnectionResetByPeer, Other };

const NoDigitError = error{NoDigit};

const FileOpenOrNoDigitError = FileOpenError || NoDigitError;

pub fn main() u8 {
    // Main

    const cli_args_count = std.os.argv.len - 1;
    if (cli_args_count > 0) {
        stdout.print("No CLI arguments expected, got {}\n", .{cli_args_count}) catch {
            return 1;
        };
        return 1;
    }

    run("input.txt") catch {
        return 1;
    };

    return 0;
}

fn run(input_filename: []const u8) anyerror!void {
    const result: u32 = calculate_result(input_filename) catch |err| {
        if (err == NoDigitError.NoDigit) {
            try stdout.print("No digit found in one of the lines.\n", .{});
        } else {
            try stdout.print("{}\n", .{err});
        }
        return err;
    };

    try stdout.print("{}\n", .{ result });
}

fn calculate_result(input_filename: []const u8) FileOpenOrNoDigitError!u32 {
    // Calculate result

    var sum: u32 = 0;

    var file = std.fs.cwd().openFile(input_filename, .{}) catch {
        return FileOpenError.Other;
    };
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    while ((in_stream.readUntilDelimiterOrEof(&buf, '\n')) catch {
        return FileOpenError.Other;
    }) |line| {
        sum += try calibration_value(line);
    }

    return sum;
}

fn calibration_value(line: []u8) NoDigitError!u32 {
    // Calibration value

    const first = first_digit(line) orelse undefined;
    if (first == undefined) {
        return NoDigitError.NoDigit;
    }

    const last = last_digit(line) orelse undefined;
    if (last == undefined) {
        return NoDigitError.NoDigit;
    }

    return 10 * first + last;
}

fn first_digit(line: []u8) ?u8 {
    // First digit

    for (line) |char| {
        return std.fmt.charToDigit(char, 10) catch {
            continue;
        };
    }

    return null;
}

fn last_digit(line: []u8) ?u8 {
    // Last digit

    var index: usize = line.len - 1;
    while (index >= 0) {
        const char: u8 = line[index];
        return std.fmt.charToDigit(char, 10) catch {
            index -= 1;
            continue;
        };
    }

    return null;
}
