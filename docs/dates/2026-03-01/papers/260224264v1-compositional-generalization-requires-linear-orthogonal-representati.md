---
layout: default
title: Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models
---

# Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models
**arXiv**：[2602.24264v1](https://arxiv.org/abs/2602.24264) · [PDF](https://arxiv.org/pdf/2602.24264.pdf)  
**作者**：Arnas Uselis, Andrea Dittadi, Seong Joon Oh  

**一句话要点**：提出线性正交表示理论以解释视觉嵌入模型的组合泛化能力

**关键词**：组合泛化, 线性表示假设, 视觉嵌入模型, 几何约束, 正交分解

## 3 点简述
- 核心问题：组合泛化要求表示结构支持未见组合的识别
- 方法要点：形式化三个几何约束，推导线性正交表示的必要性
- 实验或效果：在CLIP等模型中验证部分线性分解与泛化相关性

## 摘要（原文）

> Compositional generalization, the ability to recognize familiar parts in novel contexts, is a defining property of intelligent systems. Although modern models are trained on massive datasets, they still cover only a tiny fraction of the combinatorial space of possible inputs, raising the question of what structure representations must have to support generalization to unseen combinations. We formalize three desiderata for compositional generalization under standard training (divisibility, transferability, stability) and show they impose necessary geometric constraints: representations must decompose linearly into per-concept components, and these components must be orthogonal across concepts. This provides theoretical grounding for the Linear Representation Hypothesis: the linear structure widely observed in neural representations is a necessary consequence of compositional generalization. We further derive dimension bounds linking the number of composable concepts to the embedding geometry. Empirically, we evaluate these predictions across modern vision models (CLIP, SigLIP, DINO) and find that representations exhibit partial linear factorization with low-rank, near-orthogonal per-concept factors, and that the degree of this structure correlates with compositional generalization on unseen combinations. As models continue to scale, these conditions predict the representational geometry they may converge to. Code is available at https://github.com/oshapio/necessary-compositionality.

