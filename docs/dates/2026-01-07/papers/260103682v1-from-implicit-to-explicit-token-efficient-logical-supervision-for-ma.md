---
layout: default
title: From Implicit to Explicit: Token-Efficient Logical Supervision for Mathematical Reasoning in LLMs
---

# From Implicit to Explicit: Token-Efficient Logical Supervision for Mathematical Reasoning in LLMs
**arXiv**：[2601.03682v1](https://arxiv.org/abs/2601.03682) · [PDF](https://arxiv.org/pdf/2601.03682.pdf)  
**作者**：Shaojie Wang, Liang Zhang  

**一句话要点**：提出FSLR框架以解决大语言模型在数学推理中逻辑关系理解不足的问题

**关键词**：数学推理, 逻辑监督, 大语言模型, 训练效率, 显式学习

## 3 点简述
- 核心问题：大语言模型在数学推理中依赖模式匹配而非逻辑关系理解，导致错误率高。
- 方法要点：通过训练模型仅执行第一步规划（识别变量和操作），提供显式逻辑监督。
- 实验或效果：FSLR在分布内外设置下均优于CoT-SFT，训练更快且节省80%以上token。

## 摘要（原文）

> Recent studies reveal that large language models (LLMs) exhibit limited logical reasoning abilities in mathematical problem-solving, instead often relying on pattern-matching and memorization. We systematically analyze this limitation, focusing on logical relationship understanding, which is a core capability underlying genuine logical reasoning, and reveal that errors related to this capability account for over 90\% of incorrect predictions, with Chain-of-Thought Supervised Fine-Tuning (CoT-SFT) failing to substantially reduce these errors. To address this bottleneck, we propose First-Step Logical Reasoning (FSLR), a lightweight training framework targeting logical relationship understanding. Our key insight is that the first planning step-identifying which variables to use and which operation to apply-encourages the model to derive logical relationships directly from the problem statement. By training models on this isolated step, FSLR provides explicit supervision for logical relationship understanding, unlike CoT-SFT which implicitly embeds such relationships within complete solution trajectories. Extensive experiments across multiple models and datasets demonstrate that FSLR consistently outperforms CoT-SFT under both in-distribution and out-of-distribution settings, with average improvements of 3.2\% and 4.6\%, respectively. Moreover, FSLR achieves 4-6x faster training and reduces training token consumption by over 80\%.

