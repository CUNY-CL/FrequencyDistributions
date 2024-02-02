#!/usr/bin/env python
"""Vocabulary growth rate plotter."""


import argparse

import pandas
import plotnine


def main(args: argparse.Namespace) -> None:
    n: list[int] = [0]  # Hackish but it works.
    v: list[int] = []
    lexicon: set[str] = set()
    with open(args.tok, "r") as source:
        for line in source:
            tokens = line.casefold().split()
            lexicon.update(tokens)
            n.append(n[-1] + len(tokens))
            v.append(len(lexicon))
    n.pop(0)
    df = pandas.DataFrame({"n": n, "v": v})
    aes = plotnine.aes(x="n", y="v")
    plot = plotnine.ggplot(df, aes)
    plot += plotnine.geom_line()
    plot += plotnine.xlab("$N$ (# of tokens)")
    plot += plotnine.ylab("$V$ (# of types)")
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
    parser = argparse.ArgumentParser(
        description="Vocabulary growth rate plotter"
    )
    parser.add_argument("tok")
    parser.add_argument(
        "--font", help="font family (default: %(default)s)", default="sans"
    )
    parser.add_argument(
        "--graph_path", required=True, help="path for the output PNG"
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
