---
layout: default
title: [Re] Benchmarking LLM Capabilities in Negotiation through Scoreable Games
---

# [Re] Benchmarking LLM Capabilities in Negotiation through Scoreable Games
**arXiv**：[2602.18230v1](https://arxiv.org/abs/2602.18230) · [PDF](https://arxiv.org/pdf/2602.18230.pdf)  
**作者**：Jorge Carrasco Pollo, Ioannis Kapetangeorgis, Joshua Rosenthal, John Hua Yao  

**一句话要点**：复现并评估基于可评分游戏的LLM谈判基准，揭示其复杂性与局限性

**关键词**：大语言模型, 多智能体谈判, 基准评估, 可评分游戏, 模型比较, 信息泄漏

## 3 点简述
- 核心问题：LLM在多智能体谈判任务中缺乏稳健且可泛化的评估基准。
- 方法要点：复现原始实验，引入额外模型和指标以验证谈判质量和评估公平性。
- 实验或效果：发现基准复杂但模型比较模糊，识别实验设置中的信息泄漏和消融研究不足。

## 摘要（原文）

> Large Language Models (LLMs) demonstrate significant potential in multi-agent negotiation tasks, yet evaluation in this domain remains challenging due to a lack of robust and generalizable benchmarks. Abdelnabi et al. (2024) introduce a negotiation benchmark based on Scoreable Games, with the aim of developing a highly complex and realistic evaluation framework for LLMs. Our work investigates the reproducibility of claims in their benchmark, and provides a deeper understanding of its usability and generalizability. We replicate the original experiments on additional models, and introduce additional metrics to verify negotiation quality and evenness of evaluation. Our findings reveal that while the benchmark is indeed complex, model comparison is ambiguous, raising questions about its objectivity. Furthermore, we identify limitations in the experimental setup, particularly in information leakage detection and thoroughness of the ablation study. By examining and analyzing the behavior of a wider range of models on an extended version of the benchmark, we reveal insights that provide additional context to potential users. Our results highlight the importance of context in model-comparative evaluations.

