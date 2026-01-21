---
layout: default
title: Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores
---

# Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores
**arXiv**：[2601.13885v1](https://arxiv.org/abs/2601.13885) · [PDF](https://arxiv.org/pdf/2601.13885.pdf)  
**作者**：Esma Balkır, Alice Pernthaller, Marco Basaldella, José Hernández-Orallo, Nigel Collier  

**一句话要点**：提出基于连续分数的自适应LLM评估方法，以更少项目实现可靠模型排名

**关键词**：自适应测试, LLM评估, 连续分数, 模型排名, IRT扩展

## 3 点简述
- 核心问题：LLM生成任务评估依赖连续分数，传统自适应测试基于二值响应，效率受限。
- 方法要点：扩展IRT自适应测试至连续有界分数，使用异方差正态分布替代伯努利分布。
- 实验或效果：在五个基准上验证，仅用2%项目提升排名相关性0.12τ，置信预测准确率达95%。

## 摘要（原文）

> Computerized Adaptive Testing (CAT) has proven effective for efficient LLM evaluation on multiple-choice benchmarks, but modern LLM evaluation increasingly relies on generation tasks where outputs are scored continuously rather than marked correct/incorrect. We present a principled extension of IRT-based adaptive testing to continuous bounded scores (ROUGE, BLEU, LLM-as-a-Judge) by replacing the Bernoulli response distribution with a heteroskedastic normal distribution. Building on this, we introduce an uncertainty aware ranker with adaptive stopping criteria that achieves reliable model ranking while testing as few items and as cheaply as possible. We validate our method on five benchmarks spanning n-gram-based, embedding-based, and LLM-as-judge metrics. Our method uses 2% of the items while improving ranking correlation by 0.12 τ over random sampling, with 95% accuracy on confident predictions.

