---
layout: default
title: FLEx: Language Modeling with Few-shot Language Explanations
---

# FLEx: Language Modeling with Few-shot Language Explanations
**arXiv**：[2601.04157v1](https://arxiv.org/abs/2601.04157) · [PDF](https://arxiv.org/pdf/2601.04157.pdf)  
**作者**：Adar Avsian, Christopher Richardson, Anirudh Sundar, Larry Heck  

**一句话要点**：提出FLEx方法，通过少量语言解释改进语言模型行为，无需修改权重。

**关键词**：语言模型, 少样本学习, 解释增强, 提示工程, 错误纠正

## 3 点简述
- 核心问题：语言模型错误在相关查询中重复，大规模收集自然语言解释不可行。
- 方法要点：基于嵌入聚类选择代表性错误，验证解释纠正错误，总结为推理时提示前缀。
- 实验或效果：在CounterBench、GSM8K和ReasonIF上优于思维链提示，减少最多83%错误。

## 摘要（原文）

> Language models have become effective at a wide range of tasks, from math problem solving to open-domain question answering. However, they still make mistakes, and these mistakes are often repeated across related queries. Natural language explanations can help correct these errors, but collecting them at scale may be infeasible, particularly in domains where expert annotators are required. To address this issue, we introduce FLEx ($\textbf{F}$ew-shot $\textbf{L}$anguage $\textbf{Ex}$planations), a method for improving model behavior using a small number of explanatory examples. FLEx selects representative model errors using embedding-based clustering, verifies that the associated explanations correct those errors, and summarizes them into a prompt prefix that is prepended at inference-time. This summary guides the model to avoid similar errors on new inputs, without modifying model weights. We evaluate FLEx on CounterBench, GSM8K, and ReasonIF. We find that FLEx consistently outperforms chain-of-thought (CoT) prompting across all three datasets and reduces up to 83\% of CoT's remaining errors.

