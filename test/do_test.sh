#!/bin/bash
for engine in google tencent
do
    for num in 1 2
    do
        echo $engine $num
        translate_tex fmt${num}.txt -engine $engine
        diff fmt${num}.tex fmt${num}_$engine.tex
        rm fmt${num}.tex
    done
done
