---
layout: default
title: Transform-Augmented GRPO Improves Pass@k
---

# Transform-Augmented GRPO Improves Pass@k
**arXiv**：[2601.22478v1](https://arxiv.org/abs/2601.22478) · [PDF](https://arxiv.org/pdf/2601.22478.pdf)  
**作者**：Khiem Le, Youssef Mroueh, Phuc Nguyen, Chi-Heng Lin, Shangqian Gao, Ting Hua, Nitesh V. Chawla  

**一句话要点**：提出TA-GRPO以解决GRPO在推理任务中的多样性崩溃和梯度消失问题

**关键词**：强化学习, 语言模型推理, 策略优化, 语义增强, 数学推理

## 3 点简述
- 核心问题：GRPO导致多样性崩溃和梯度消失，恶化模型对表面措辞的敏感性
- 方法要点：通过语义等价变换生成问题变体，并跨组池化奖励计算优势
- 实验或效果：在数学推理基准上提升Pass@k，AMC12/AIME24增益达9.84点

## 摘要（原文）

> Large language models trained via next-token prediction are fundamentally pattern-matchers: sensitive to superficial phrasing variations even when the underlying problem is identical. Group Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards. We propose TA-GRPO (Transform-Augmented GRPO), which generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group. This pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. We provide theoretical justification showing that TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift. Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

