---
layout: default
title: On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks
---

# On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks
**arXiv**：[2602.15460v1](https://arxiv.org/abs/2602.15460) · [PDF](https://arxiv.org/pdf/2602.15460.pdf)  
**作者**：Yannic Neuhaus, Nicolas Flammarion, Matthias Hein, Francesco Croce  

**一句话要点**：提出评估框架以检验多模态大模型在简单视觉规划任务中的分布外泛化能力

**关键词**：多模态大模型, 推理泛化, 思维链, 视觉规划, 分布外泛化, 文本表示

## 3 点简述
- 核心问题：多模态大模型的推理泛化能力定义模糊且理解不足
- 方法要点：基于网格导航任务，微调不同输入表示和思维链策略的模型变体
- 实验或效果：思维链推理提升分布内泛化，但分布外泛化有限，文本模型优于图像模型

## 摘要（原文）

> Integrating reasoning in large language models and large vision-language models has recently led to significant improvement of their capabilities. However, the generalization of reasoning models is still vaguely defined and poorly understood. In this work, we present an evaluation framework to rigorously examine how well chain-of-thought (CoT) approaches generalize on a simple planning task. Specifically, we consider a grid-based navigation task in which a model is provided with a map and must output a sequence of moves that guides a player from a start position to a goal while avoiding obstacles. The versatility of the task and its data allows us to fine-tune model variants using different input representations (visual and textual) and CoT reasoning strategies, and systematically evaluate them under both in-distribution (ID) and out-of-distribution (OOD) test conditions. Our experiments show that, while CoT reasoning improves in-distribution generalization across all representations, out-of-distribution generalization (e.g., to larger maps) remains very limited in most cases when controlling for trivial matches with the ID data. Surprisingly, we find that reasoning traces which combine multiple text formats yield the best (and non-trivial) OOD generalization. Finally, purely text-based models consistently outperform those utilizing image-based inputs, including a recently proposed approach relying on latent space reasoning.

