---
layout: default
title: BLITZRANK: Principled Zero-shot Ranking Agents with Tournament Graphs
---

# BLITZRANK: Principled Zero-shot Ranking Agents with Tournament Graphs
**arXiv**：[2602.05448v1](https://arxiv.org/abs/2602.05448) · [PDF](https://arxiv.org/pdf/2602.05448.pdf)  
**作者**：Sheshansh Agrawal, Thien Hang Nguyen, Douwe Kiela  

**一句话要点**：提出基于锦标赛图的零样本排序框架，以高效解决LLM重排序中的信息利用不足问题。

**关键词**：零样本排序, 锦标赛图, LLM重排序, 信息增益最大化, 非传递偏好处理, 检索增强生成

## 3 点简述
- 现有LLM重排序方法依赖启发式或效率低下，未能充分利用排序决策揭示的信息。
- 引入锦标赛图框架，通过聚合成对偏好并利用传递闭包，减少模型调用次数。
- 在14个基准测试和5个LLM上，实现准确率相当或更高，同时显著降低计算成本。

## 摘要（原文）

> Large language models have emerged as powerful zero-shot rerankers for retrieval-augmented generation, offering strong generalization without task-specific training. However, existing LLM reranking methods either rely on heuristics that fail to fully exploit the information revealed by each ranking decision or are inefficient when they do. We introduce a tournament graph framework that provides a principled foundation for $k$-wise reranking. Our key observation is that each $k$-document comparison reveals a complete tournament of $\binom{k}{2}$ pairwise preferences. These tournaments are aggregated into a global preference graph, whose transitive closure yields many additional orderings without further model invocations. We formalize when a candidate's rank is certifiably determined and design a query schedule that greedily maximizes information gain towards identifying the top-$m$ items. Our framework also gracefully handles non-transitive preferences - cycles induced by LLM judgments - by collapsing them into equivalence classes that yield principled tiered rankings. Empirically, across 14 benchmarks and 5 LLMs, our method achieves Pareto dominance over existing methods: matching or exceeding accuracy while requiring 25-40% fewer tokens than comparable approaches, and 7$\times$ fewer than pairwise methods at near-identical quality.

