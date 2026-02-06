---
layout: default
title: Orthogonal Model Merging
---

# Orthogonal Model Merging
**arXiv**：[2602.05943v1](https://arxiv.org/abs/2602.05943) · [PDF](https://arxiv.org/pdf/2602.05943.pdf)  
**作者**：Sihan Yang, Kexuan Shi, Weiyang Liu  

**一句话要点**：提出正交模型合并以在正交群流形上合并微调大语言模型，保留权重几何结构。

**关键词**：模型合并, 正交群流形, 几何结构保留, 正交微调, 灾难性遗忘缓解, 大语言模型

## 3 点简述
- 问题：现有模型合并方法在欧氏空间线性操作破坏预训练权重的几何特性，如超球面能量。
- 方法：通过正交微调学习正交矩阵，映射到李代数进行合并，并扩展至非正交微调模型的正交-残差解耦策略。
- 效果：实验显示有效缓解灾难性遗忘，保持多任务性能。

## 摘要（原文）

> Merging finetuned Large Language Models (LLMs) has become increasingly important for integrating diverse capabilities into a single unified model. However, prevailing model merging methods rely on linear arithmetic in Euclidean space, which often destroys the intrinsic geometric properties of pretrained weights, such as hyperspherical energy. To address this, we propose Orthogonal Model Merging (OrthoMerge), a method that performs merging operations on the Riemannian manifold formed by the orthogonal group to preserve the geometric structure of the model's weights. By mapping task-specific orthogonal matrices learned by Orthogonal Finetuning (OFT) to the Lie algebra, OrthoMerge enables a principled yet efficient integration that takes into account both the direction and intensity of adaptations. In addition to directly leveraging orthogonal matrices obtained by OFT, we further extend this approach to general models finetuned with non-OFT methods (i.e., low-rank finetuning, full finetuning) via an Orthogonal-Residual Decoupling strategy. This technique extracts the orthogonal components of expert models by solving the orthogonal Procrustes problem, which are then merged on the manifold of the orthogonal group, while the remaining linear residuals are processed through standard additive merging. Extensive empirical results demonstrate the effectiveness of OrthoMerge in mitigating catastrophic forgetting and maintaining model performance across diverse tasks.

