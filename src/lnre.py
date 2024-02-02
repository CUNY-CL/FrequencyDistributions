#!/usr/bin/env python
"""LNRE calculator.

This script computes a number of statistics characterizing LNRE data:

* N: corpus size
* V: vocabulary size
* V(1): the number of _hapax legomena_ (symbols occuring once)
* V(2): the number of _dis legomena_ (symbols occurring twice)
* V/N: vocabulary growth rate
* V1/N: hapax growth rate (also the Good-Turing estimate)
* Frequency mean
* Frequency median (rounding down for ties)
* Frequency mode (if a unique solution exists)
* alpha: the "Zipf slope" in the equation log f = log C - \\alpha V
* R^2: the r-squared of the Zipf slope fit

Optionally, it also produces a PNG graph of the "Zipf curve": log rank vs. log
frequency.

The data is provided in a two-column TSV in which the first column is a string
key, and the second is an integral count of that item, and a tab separates the 
two columns."""

import argparse
import collections
import statistics

from typing import Dict

import numpy
import pandas
import plotnine
import statsmodels.api as statsmodels


def main(args: argparse.ArgumentParser) -> None:
    # Collects counts.
    freqdict: Dict[str, int] = {}
    V1 = 0
    V2 = 0
    with open(args.tsv, "r") as source:
        for line in source:
            (symbol, count) = line.rstrip().split("\t", 1)
            count = int(count)
            freqdict[symbol] = count
            if count == 1:
                V1 += 1
            elif count == 2:
                V2 += 1
    # Computes basic stats.
    freqs = freqdict.values()
    N = sum(freqs)
    V = len(freqs)
    print(f"N:\t{N:,}")
    print(f"V:\t{V:,}")
    print(f"V(1):\t{V1:,}")
    print(f"V(2):\t{V2:,}")
    print(f"V/N:\t{V / N:.4f}")
    print(f"V1/N:\t{V1 / N:.4f}")
    print(f"mean:\t{statistics.mean(freqs):.4f}")
    print(f"median:\t{statistics.median_low(freqs):,}")
    try:
        print(f"mode:\t{statistics.mode(freqs):,}")
    except statistics.StatisticsError:
        print("mode:\t(no unique mode)")
    rank = numpy.arange(1, 1 + len(freqs))
    freq = numpy.array(list(freqs))
    log_rank = numpy.log10(rank)
    log_freq = numpy.log10(freq)
    design = statsmodels.add_constant(log_rank)
    results = statsmodels.OLS(log_freq, design).fit()
    print(f"alpha:\t{results.params[1]:.4f}")
    print(f"R^2:\t{results.rsquared:.4f}")
    if not args.graph_path:
        return
    # Makes PNG graph.
    df = pandas.DataFrame({"rank": rank, "freq": freq})
    aes = plotnine.aes(x="rank", y="freq")
    plot = plotnine.ggplot(df, aes)
    plot += plotnine.geom_point(alpha=0.5)
    plot += plotnine.xlab("$r$ (rank)") + plotnine.ylab("$c$ (count)")
    plot += plotnine.scale_x_continuous(trans="log10")
    plot += plotnine.scale_y_continuous(trans="log10")
    plot += plotnine.theme_bw(base_family=args.font)
    plot.save(
        args.graph_path,
        width=args.graph_size,
        height=args.graph_size,
        dpi=args.graph_dpi,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LNRE calculator")
    parser.add_argument("tsv")
    parser.add_argument(
        "--font", help="font family (default: %(default)s)", default="sans"
    )
    parser.add_argument(
        "--graph_path",
        help="path for the output PNG (if not provided, no PNG is generated)",
    )
    parser.add_argument(
        "--graph_size",
        type=int,
        default=4,
        help="size for graph in inches (default: %(default)s)",
    )
    parser.add_argument(
        "--graph_dpi", default=300, help="DPI for graph (default: %(default)s)"
    )
    main(parser.parse_args())
