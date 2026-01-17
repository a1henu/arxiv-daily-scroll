---
layout: default
title: Multi-Property Synthesis
---

# Multi-Property Synthesis
**arXiv**：[2601.10651v1](https://arxiv.org/abs/2601.10651) · [PDF](https://arxiv.org/pdf/2601.10651.pdf)  
**作者**：Christoph Weinhuber, Yannik Schnitzer, Alessandro Abate, David Parker, Giuseppe De Giacomo, Moshe Y. Vardi  

**一句话要点**：提出符号化算法以解决多属性LTLf综合中最大化可实现目标集的问题。

**关键词**：LTLf综合, 多属性合成, 符号化算法, 不动点计算, 最大化可实现集

## 3 点简述
- 研究多属性LTLf综合，当所有属性无法同时满足时，避免枚举子集。
- 通过单次不动点计算，紧凑表示状态与可实现目标集的关系，并合成策略。
- 符号化算法利用布尔目标变量和单调性，性能比基线快达两个数量级。

## 摘要（原文）

> We study LTLf synthesis with multiple properties, where satisfying all properties may be impossible. Instead of enumerating subsets of properties, we compute in one fixed-point computation the relation between product-game states and the goal sets that are realizable from them, and we synthesize strategies achieving maximal realizable sets. We develop a fully symbolic algorithm that introduces Boolean goal variables and exploits monotonicity to represent exponentially many goal combinations compactly. Our approach substantially outperforms enumeration-based baselines, with speedups of up to two orders of magnitude.

