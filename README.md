# MATH260-Final-Project

## Description

This project implements the Bellman-Ford algorithm to detect arbitrage opportunities in the foreign exchange market. It converts exchange rates into graphs with log-transformed weights and identifies arbitrage opportunities by detecting negative cycles within the graph.

## Background

In currency trading, an arbitrage opportunity is an opportunity in which one can make riskless profit by simply purchasing exchanges in a certain cycle. For example, if the exchange rate for EUR->USD is 1.1 and the exchange rate for USD->EUR is 0.93, we can use an arbitrage opportunity by simply going in the cycle of EUR->USD->EUR, which creates 2.3% profit each time. Of course, there wouldn't be such easily detectable arbitrage opportunities in real market and the cycles for arbitrage are usually much longer — that's where Bellman-Ford comes in to detect cycles for traders.

## Features

1. Converts exchange rates into directed graphs with log-transformed weights
2. Detects arbitrage opportunities within the directed graphs using the Bellman-Ford Algorithm: we iterate over each node in the graph |V|-1 times to update their shortest distance from the origin and perceive if any of the shortest distance would still change after |V|-1 iterations. We record the predecessor each time a shortest distance is updated, so we can reconstruct the negative cycle once we find one.
3. Reconstructs the most profitable arbitrage cycle, if any
4. Prints the best profitable cycle and its effectiveness

## Usage

1. Define currencies to the "currencies" list
2. Input exchange rates to the "exchange_rates" dictionary
3. Call bellman_ford() with the source currency
4. Output will print the best arbitrage cycle, if there is any

## Testing

Tested with a synthetic dataset of 4 currencies and various exchange paths with different exchange rates. The algorithm successfully detected all arbitrage opportunities and identified the best one when they existed, and returns none when it doesn't. Bellman-Ford was implemented by hand for all of the test cases and the manually computed results confirmed the output of the algorithm.
