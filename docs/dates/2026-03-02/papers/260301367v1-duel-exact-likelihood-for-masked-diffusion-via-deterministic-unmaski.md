---
layout: default
title: DUEL: Exact Likelihood for Masked Diffusion via Deterministic Unmasking
---

# DUEL: Exact Likelihood for Masked Diffusion via Deterministic Unmasking
**arXiv**：[2603.01367v1](https://arxiv.org/abs/2603.01367) · [PDF](https://arxiv.org/pdf/2603.01367.pdf)  
**作者**：Gilad Turok, Chris De Sa, Volodymyr Kuleshov  

**一句话要点**：提出DUEL框架以解决掩码扩散模型缺乏准确困惑度评估的问题

**关键词**：掩码扩散模型, 困惑度评估, 确定性位置选择, 精确似然计算, 采样策略比较, 零样本基准

## 3 点简述
- 核心问题：掩码扩散模型缺乏在测试时分布下的准确困惑度评估，现有方法如ELBO和生成困惑度存在偏差或忽略多样性。
- 方法要点：通过形式化确定性位置选择，统一主流采样策略，并证明DUEL允许通过简单算法计算精确似然。
- 实验或效果：DUEL显著缩小MDM与自回归模型的困惑度差距，在零样本基准上达82%，并揭示MDM性能上限未达，AG News上可达36.47困惑度。

## 摘要（原文）

> Masked diffusion models (MDMs) generate text by iteratively selecting positions to unmask and then predicting tokens at those positions. Yet MDMs lack proper perplexity evaluation: the ELBO is a loose bound on likelihood under the training distribution, not the test-time distribution, while generative perplexity requires a biased external model and ignores diversity. To address this, we introduce the \textsc{DUEL} framework, which formalizes \emph{deterministic} position selection, unifying leading MDM sampling strategies. We prove \textbf{\textsc{DUEL} admits \emph{exact} likelihood computation} via a simple algorithm, evaluated under the same position selection used at test time. This \textbf{gives MDMs proper perplexity for the first time} -- the natural analogue of autoregressive perplexity. With proper perplexity in hand, we revisit key questions about MDMs. \textbf{MDMs are substantially better than previously thought}: the MDM-autoregressive perplexity gap shrinks by up to 32\% on in-domain data and 82\% on zero-shot benchmarks. \textsc{DUEL} enables the first principled comparison of fast, parallel samplers across compute budgets -- an analysis impossible with the ELBO and unreliable with generative perplexity -- identifying probability margin \citep{kim2025train} as a strong default. Finally, oracle search over position orderings reveals MDMs can far surpass autoregressive models -- achieving 36.47 vs.\ 52.11 perplexity on AG News -- demonstrating the ceiling of MDM performance has not yet been reached.

