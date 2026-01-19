---
layout: default
title: Do explanations generalize across large reasoning models?
---

# Do explanations generalize across large reasoning models?
**arXiv**：[2601.11517v1](https://arxiv.org/abs/2601.11517) · [PDF](https://arxiv.org/pdf/2601.11517.pdf)  
**作者**：Koyena Pal, David Bau, Chandan Singh  

**一句话要点**：评估大型推理模型解释的泛化性，提出句子级集成策略以提高一致性。

**关键词**：大型推理模型, 思维链解释, 解释泛化性, 模型一致性, 句子级集成

## 3 点简述
- 核心问题：大型推理模型生成的解释是否捕获通用模式而非模型特有模式。
- 方法要点：通过解释在不同模型间诱导相同行为来评估泛化性，并分析条件。
- 实验或效果：发现解释能提高模型间一致性，且与人类偏好和强化学习后训练相关。

## 摘要（原文）

> Large reasoning models (LRMs) produce a textual chain of thought (CoT) in the process of solving a problem, which serves as a potentially powerful tool to understand the problem by surfacing a human-readable, natural-language explanation. However, it is unclear whether these explanations generalize, i.e. whether they capture general patterns about the underlying problem rather than patterns which are esoteric to the LRM. This is a crucial question in understanding or discovering new concepts, e.g. in AI for science. We study this generalization question by evaluating a specific notion of generalizability: whether explanations produced by one LRM induce the same behavior when given to other LRMs. We find that CoT explanations often exhibit this form of generalization (i.e. they increase consistency between LRMs) and that this increased generalization is correlated with human preference rankings and post-training with reinforcement learning. We further analyze the conditions under which explanations yield consistent answers and propose a straightforward, sentence-level ensembling strategy that improves consistency. Taken together, these results prescribe caution when using LRM explanations to yield new insights and outline a framework for characterizing LRM explanation generalization.

