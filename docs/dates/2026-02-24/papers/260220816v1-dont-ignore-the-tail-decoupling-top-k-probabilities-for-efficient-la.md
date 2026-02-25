---
layout: default
title: Don't Ignore the Tail: Decoupling top-K Probabilities for Efficient Language Model Distillation
---

# Don't Ignore the Tail: Decoupling top-K Probabilities for Efficient Language Model Distillation
**arXiv**：[2602.20816v1](https://arxiv.org/abs/2602.20816) · [PDF](https://arxiv.org/pdf/2602.20816.pdf)  
**作者**：Sayantan Dasgupta, Trevor Cohn, Timothy Baldwin  

**一句话要点**：提出解耦顶部概率的尾感知散度，以提升语言模型蒸馏中低概率成分的影响。

**关键词**：语言模型蒸馏, KL散度优化, 尾感知学习, 解码器模型, 高效训练

## 3 点简述
- 核心问题：传统KL散度在语言模型蒸馏中过度关注教师模型的高概率预测，忽略低概率但信息丰富的尾部成分。
- 方法要点：设计一种尾感知散度，解耦教师模型顶部K个概率与低概率预测的贡献，保持与KL散度相同的计算复杂度。
- 实验或效果：在解码器模型的预训练和监督蒸馏中，该方法在多个数据集上表现竞争性，且计算高效，适合学术预算。

## 摘要（原文）

> The core learning signal used in language model distillation is the standard Kullback-Leibler (KL) divergence between the student and teacher distributions. Traditional KL divergence tends to be dominated by the next tokens with the highest probabilities, i.e., the teacher's modes, thereby diminishing the influence of less probable yet potentially informative components of the output distribution. We propose a new tail-aware divergence that decouples the contribution of the teacher model's top-K predicted probabilities from that of lower-probability predictions, while maintaining the same computational profile as the KL Divergence. Our decoupled approach reduces the impact of the teacher modes and, consequently, increases the contribution of the tail of the distribution. Experimental results demonstrate that our modified distillation method yields competitive performance in both pre-training and supervised distillation of decoder models across various datasets. Furthermore, the distillation process is efficient and can be performed with a modest academic budget for large datasets, eliminating the need for industry-scale computing.

