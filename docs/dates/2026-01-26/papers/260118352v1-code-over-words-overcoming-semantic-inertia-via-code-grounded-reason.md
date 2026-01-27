---
layout: default
title: Code over Words: Overcoming Semantic Inertia via Code-Grounded Reasoning
---

# Code over Words: Overcoming Semantic Inertia via Code-Grounded Reasoning
**arXiv**：[2601.18352v1](https://arxiv.org/abs/2601.18352) · [PDF](https://arxiv.org/pdf/2601.18352.pdf)  
**作者**：Manjie Xu, Isabella Yin, Xinyi Tu, Chi Zhang, Yixin Zhu  

**一句话要点**：提出代码接地推理方法，通过代码表示解决大语言模型语义惯性问题

**关键词**：语义惯性, 代码接地推理, 先验知识抑制, 大语言模型缩放, 动态规则表示, 上下文推理

## 3 点简述
- 核心问题：大语言模型存在语义惯性，难以抑制预训练先验知识以适应动态规则变化
- 方法要点：将动态规则表示为可执行代码而非描述性文本，并引入代码接地视觉训练框架
- 实验效果：该方法在Baba Is You游戏中有效抑制先验知识，性能优于推理时搜索方法

## 摘要（原文）

> LLMs struggle with Semantic Inertia: the inability to inhibit pre-trained priors (e.g., "Lava is Dangerous") when dynamic, in-context rules contradict them. We probe this phenomenon using Baba Is You, where physical laws are mutable text rules, enabling precise evaluation of models' ability to override learned priors when rules change. We quantatively observe that larger models can exhibit inverse scaling: they perform worse than smaller models when natural language reasoning requires suppressing pre-trained associations (e.g., accepting "Lava is Safe"). Our analysis attributes this to natural language encoding, which entangles descriptive semantics and logical rules, leading to persistent hallucinations of familiar physics despite explicit contradictory rules. Here we show that representing dynamics as executable code, rather than descriptive text, reverses this trend and enables effective prior inhibition. We introduce Code-Grounded Vistas (LCV), which fine-tunes models on counterfactual pairs and identifies states with contradictory rules, thereby forcing attention to logical constraints rather than visual semantics. This training-time approach outperforms expensive inference-time search methods in both efficiency and accuracy. Our results demonstrate that representation fundamentally determines whether scaling improves or impairs contextual reasoning. This challenges the assumption that larger models are universally better, with implications for domains that require dynamic overriding of learned priors.

