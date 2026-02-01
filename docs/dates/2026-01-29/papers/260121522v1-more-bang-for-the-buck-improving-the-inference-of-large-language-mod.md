---
layout: default
title: More Bang for the Buck: Improving the Inference of Large Language Models at a Fixed Budget using Reset and Discard (ReD)
---

# More Bang for the Buck: Improving the Inference of Large Language Models at a Fixed Budget using Reset and Discard (ReD)
**arXiv**：[2601.21522v1](https://arxiv.org/abs/2601.21522) · [PDF](https://arxiv.org/pdf/2601.21522.pdf)  
**作者**：Sagi Meir, Tommer D. Keidar, Noam Levi, Shlomi Reuveni, Barak Hirshberg  

**一句话要点**：提出Reset-and-Discard方法以在固定预算下提升大语言模型推理效率

**关键词**：大语言模型推理, 覆盖率优化, 预算约束, 查询策略, 效率提升

## 3 点简述
- 核心问题：固定预算下，大语言模型推理存在收益递减，覆盖率增长缓慢
- 方法要点：通过重置和丢弃策略优化查询，提高覆盖率，可预测节省量
- 实验或效果：在HumanEval上验证，显著减少尝试次数、令牌和成本

## 摘要（原文）

> The performance of large language models (LLMs) on verifiable tasks is usually measured by pass@k, the probability of answering a question correctly at least once in k trials. At a fixed budget, a more suitable metric is coverage@cost, the average number of unique questions answered as a function of the total number of attempts. We connect the two metrics and show that the empirically-observed power-law behavior in pass@k leads to a sublinear growth of the coverage@cost (diminishing returns). To solve this problem, we propose Reset-and-Discard (ReD), a query method of LLMs that increases coverage@cost for any given budget, regardless of the pass@k form. Moreover, given a pass@k, we can quantitatively predict the savings in the total number of attempts using ReD. If pass@k is not available for the model, ReD can infer its power-law exponent. Experiments on three LLMs using HumanEval demonstrate that ReD substantially reduces the required attempts, tokens, and USD cost to reach a desired coverage, while also offering an efficient way to measure inference power-laws.

