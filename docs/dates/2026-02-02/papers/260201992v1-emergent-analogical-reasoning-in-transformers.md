---
layout: default
title: Emergent Analogical Reasoning in Transformers
---

# Emergent Analogical Reasoning in Transformers
**arXiv**：[2602.01992v1](https://arxiv.org/abs/2602.01992) · [PDF](https://arxiv.org/pdf/2602.01992.pdf)  
**作者**：Gouki Minegishi, Jingyuan Feng, Hiroki Furuta, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo  

**一句话要点**：提出基于范畴论函子的类比推理形式化方法，以评估Transformer中的涌现现象。

**关键词**：类比推理, Transformer机制, 范畴论, 涌现现象, 合成任务, 几何对齐

## 3 点简述
- 核心问题：Transformer如何获取和实现类比推理机制，目前理解不足。
- 方法要点：将类比推理形式化为跨范畴实体对应关系的推断，引入合成任务进行控制评估。
- 实验或效果：发现类比推理涌现对数据特征、优化选择和模型规模高度敏感，机制分析揭示几何对齐和函子应用是关键。

## 摘要（原文）

> Analogy is a central faculty of human intelligence, enabling abstract patterns discovered in one domain to be applied to another. Despite its central role in cognition, the mechanisms by which Transformers acquire and implement analogical reasoning remain poorly understood. In this work, inspired by the notion of functors in category theory, we formalize analogical reasoning as the inference of correspondences between entities across categories. Based on this formulation, we introduce synthetic tasks that evaluate the emergence of analogical reasoning under controlled settings. We find that the emergence of analogical reasoning is highly sensitive to data characteristics, optimization choices, and model scale. Through mechanistic analysis, we show that analogical reasoning in Transformers decomposes into two key components: (1) geometric alignment of relational structure in the embedding space, and (2) the application of a functor within the Transformer. These mechanisms enable models to transfer relational structure from one category to another, realizing analogy. Finally, we quantify these effects and find that the same trends are observed in pretrained LLMs. In doing so, we move analogy from an abstract cognitive notion to a concrete, mechanistically grounded phenomenon in modern neural networks.

