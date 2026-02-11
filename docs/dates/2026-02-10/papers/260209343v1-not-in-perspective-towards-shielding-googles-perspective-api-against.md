---
layout: default
title: Not-in-Perspective: Towards Shielding Google's Perspective API Against Adversarial Negation Attacks
---

# Not-in-Perspective: Towards Shielding Google's Perspective API Against Adversarial Negation Attacks
**arXiv**：[2602.09343v1](https://arxiv.org/abs/2602.09343) · [PDF](https://arxiv.org/pdf/2602.09343.pdf)  
**作者**：Michail S. Alexiou, J. Sukarno Mertoguno  

**一句话要点**：提出基于形式推理的包装方法以增强机器学习毒性检测系统对抗否定攻击的能力

**关键词**：毒性检测, 对抗攻击, 形式推理, 机器学习, 否定攻击, 社交媒体

## 3 点简述
- 核心问题：基于统计的毒性检测系统易受包含逻辑否定等对抗性攻击影响，导致准确性下降。
- 方法要点：设计形式推理包装器，作为预处理和后处理步骤，结合机器学习模型提升对否定攻击的鲁棒性。
- 实验或效果：在否定对抗数据集上评估，混合方法相比纯统计解决方案显著提高了毒性评分的准确性和有效性。

## 摘要（原文）

> The rise of cyberbullying in social media platforms involving toxic comments has escalated the need for effective ways to monitor and moderate online interactions. Existing solutions of automated toxicity detection systems, are based on a machine or deep learning algorithms. However, statistics-based solutions are generally prone to adversarial attacks that contain logic based modifications such as negation in phrases and sentences. In that regard, we present a set of formal reasoning-based methodologies that wrap around existing machine learning toxicity detection systems. Acting as both pre-processing and post-processing steps, our formal reasoning wrapper helps alleviating the negation attack problems and significantly improves the accuracy and efficacy of toxicity scoring. We evaluate different variations of our wrapper on multiple machine learning models against a negation adversarial dataset. Experimental results highlight the improvement of hybrid (formal reasoning and machine-learning) methods against various purely statistical solutions.

