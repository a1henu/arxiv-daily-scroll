---
layout: default
title: Representation Invariance and Allocation: When Subgroup Balance Matters
---

# Representation Invariance and Allocation: When Subgroup Balance Matters
**arXiv**：[2512.09496v1](https://arxiv.org/abs/2512.09496) · [PDF](https://arxiv.org/pdf/2512.09496.pdf)  
**作者**：Anissa Alloula, Charles Jones, Zuzanna Wakefield-Skorniewska, Francesco Quinzan, Bartłomiej Papież  

**一句话要点**：提出潜在分离假说以优化基础模型微调中的子群数据平衡决策

**关键词**：子群平衡, 潜在分离假说, 基础模型微调, 数据表示, 模型泛化, 计算机视觉

## 3 点简述
- 核心问题：训练数据中子群表示不平衡对模型泛化性能的影响机制未知
- 方法要点：基于预训练模型潜在空间子群分离度，提出潜在分离假说解释性能敏感性
- 实验或效果：在四个视觉和语言模型中验证假说，并应用于基础模型微调实践

## 摘要（原文）

> Unequal representation of demographic groups in training data poses challenges to model generalisation across populations. Standard practice assumes that balancing subgroup representation optimises performance. However, recent empirical results contradict this assumption: in some cases, imbalanced data distributions actually improve subgroup performance, while in others, subgroup performance remains unaffected by the absence of an entire subgroup during training. We conduct a systematic study of subgroup allocation across four vision and language models, varying training data composition to characterise the sensitivity of subgroup performance to data balance. We propose the latent separation hypothesis, which states that a partially fine-tuned model's dependence on subgroup representation is determined by the degree of separation between subgroups in the latent space of the pre-trained model. We formalise this hypothesis, provide theoretical analysis, and validate it empirically. Finally, we present a practical application to foundation model fine-tuning, demonstrating that quantitative analysis of latent subgroup separation can inform data collection and balancing decisions.

