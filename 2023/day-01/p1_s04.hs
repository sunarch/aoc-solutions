-- This Source Code Form is subject to the terms of the Mozilla Public
-- License, v. 2.0. If a copy of the MPL was not distributed with this
-- file, You can obtain one at http://mozilla.org/MPL/2.0/.

-- AoC 2023 / Day 1 / Part 1 / Solution 4 (Haskell)
--
-- https://adventofcode.com/2023/day/1

import System.IO
import Data.Char


inputFileName = "input.txt"


main :: IO ()
main = do
  inputFileContents <- readFile inputFileName
  let result = calculateResult inputFileContents
  print result


calculateResult :: String -> Integer
calculateResult (fileContents) = do
  let fileLines = lines fileContents
  let result1 = map calibrationValue fileLines
  let result2 = sum result1
  result2


calibrationValue :: String -> Integer
calibrationValue (line) =
  toInteger ((digitToInt (firstDigit line)) * 10 + (digitToInt (lastDigit line)))


firstDigit :: String -> Char
firstDigit (x:xs) =
  if isDigit x
    then x
    else firstDigit xs


lastDigit :: String -> Char
lastDigit (x) = do
  let reversed = reverse' x
  firstDigit(reversed)


reverse' :: [a] -> [a]
reverse' = foldl (\acc x -> x : acc) []
