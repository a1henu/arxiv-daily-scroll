---
layout: default
title: Language Models Struggle to Use Representations Learned In-Context
---

# Language Models Struggle to Use Representations Learned In-Context
**arXiv**：[2602.04212v1](https://arxiv.org/abs/2602.04212) · [PDF](https://arxiv.org/pdf/2602.04212.pdf)  
**作者**：Michael A. Lepori, Tal Linzen, Ann Yuan, Katja Filippova  

**一句话要点**：揭示大语言模型难以灵活运用上下文学习到的语义表示

**关键词**：上下文学习, 语义表示, 自适应世界建模, 大语言模型评估, 表示部署

## 3 点简述
- 核心问题：大语言模型能否将上下文学习到的语义表示应用于下游任务
- 方法要点：评估模型在下一词预测和自适应世界建模任务中的表现
- 实验或效果：发现模型即使编码了语义，也难以可靠地利用新语义模式

## 摘要（原文）

> Though large language models (LLMs) have enabled great success across a wide variety of tasks, they still appear to fall short of one of the loftier goals of artificial intelligence research: creating an artificial system that can adapt its behavior to radically new contexts upon deployment. One important step towards this goal is to create systems that can induce rich representations of data that are seen in-context, and then flexibly deploy these representations to accomplish goals. Recently, Park et al. (2024) demonstrated that current LLMs are indeed capable of inducing such representation from context (i.e., in-context representation learning). The present study investigates whether LLMs can use these representations to complete simple downstream tasks.
>   We first assess whether open-weights LLMs can use in-context representations for next-token prediction, and then probe models using a novel task, adaptive world modeling. In both tasks, we find evidence that open-weights LLMs struggle to deploy representations of novel semantics that are defined in-context, even if they encode these semantics in their latent representations. Furthermore, we assess closed-source, state-of-the-art reasoning models on the adaptive world modeling task, demonstrating that even the most performant LLMs cannot reliably leverage novel patterns presented in-context. Overall, this work seeks to inspire novel methods for encouraging models to not only encode information presented in-context, but to do so in a manner that supports flexible deployment of this information.

