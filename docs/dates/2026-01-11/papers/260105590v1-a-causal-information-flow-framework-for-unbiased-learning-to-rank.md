---
layout: default
title: A Causal Information-Flow Framework for Unbiased Learning-to-Rank
---

# A Causal Information-Flow Framework for Unbiased Learning-to-Rank
**arXiv**：[2601.05590v1](https://arxiv.org/abs/2601.05590) · [PDF](https://arxiv.org/pdf/2601.05590.pdf)  
**作者**：Haoming Gong, Qingyao Ai, Zhihao Tao, Yongfeng Zhang  

**一句话要点**：提出基于因果信息流的无偏学习排序框架，以解决点击数据中的多源偏差问题。

**关键词**：无偏学习排序, 因果推断, 信息论, 点击偏差, 结构因果模型, 双重稳健估计

## 3 点简述
- 核心问题：点击数据存在位置、选择和信任等多源偏差，影响排序模型对真实相关性的学习。
- 方法要点：结合结构因果模型与信息论工具，通过条件互信息量化偏差泄漏，并引入双重稳健估计器提升风险估计可靠性。
- 实验或效果：在标准基准测试中，该方法有效减少偏差泄漏并提升排序性能，尤其在多偏差交互场景下表现突出。

## 摘要（原文）

> In web search and recommendation systems, user clicks are widely used to train ranking models. However, click data is heavily biased, i.e., users tend to click higher-ranked items (position bias), choose only what was shown to them (selection bias), and trust top results more (trust bias). Without explicitly modeling these biases, the true relevance of ranked items cannot be correctly learned from clicks. Existing Unbiased Learning-to-Rank (ULTR) methods mainly correct position bias and rely on propensity estimation, but they cannot measure remaining bias, provide risk guarantees, or jointly handle multiple bias sources. To overcome these challenges, this paper introduces a novel causal learning-based ranking framework that extends ULTR by combining Structural Causal Models (SCMs) with information-theoretic tools. SCMs specify how clicks are generated and help identify the true relevance signal from click data, while conditional mutual information, measures how much bias leaks into the
>   learned relevance estimates. We use this leakage measure to define a rigorous notion of disentanglement and include it as a regularizer during model training to reduce bias. In addition, we incorporate a causal inference estimator, i.e., doubly robust estimator, to ensure more reliable risk estimation. Experiments on standard Learning-to-Rank benchmarks show that our method consistently reduces measured bias leakage and improves ranking performance, especially in realistic scenarios where multiple biases-such as position and trust bias-interact strongly.

