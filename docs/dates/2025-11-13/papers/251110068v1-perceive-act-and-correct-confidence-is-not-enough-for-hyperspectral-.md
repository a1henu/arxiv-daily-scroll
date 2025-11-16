---
layout: default
title: Perceive, Act and Correct: Confidence Is Not Enough for Hyperspectral Classification
---

# Perceive, Act and Correct: Confidence Is Not Enough for Hyperspectral Classification
**arXiv**：[2511.10068v1](https://arxiv.org/abs/2511.10068) · [PDF](https://arxiv.org/pdf/2511.10068.pdf)  
**作者**：Muzhou Yang, Wuzhou Quan, Mingqiang Wei  

**一句话要点**：提出CABIN框架以解决高光谱分类中置信度误导问题

**关键词**：高光谱图像分类, 半监督学习, 不确定性估计, 伪标签优化, 认知偏差纠正

## 3 点简述
- 核心问题：高光谱图像分类中，高置信度预测常导致错误，模型缺乏不确定性感知，易产生确认偏差。
- 方法要点：CABIN通过感知-行动-校正闭环，估计认知不确定性，采用不确定性引导采样和动态分配策略。
- 实验或效果：集成CABIN提升多种先进方法性能，提高标注效率和泛化能力。

## 摘要（原文）

> Confidence alone is often misleading in hyperspectral image classification, as models tend to mistake high predictive scores for correctness while lacking awareness of uncertainty. This leads to confirmation bias, especially under sparse annotations or class imbalance, where models overfit confident errors and fail to generalize. We propose CABIN (Cognitive-Aware Behavior-Informed learNing), a semi-supervised framework that addresses this limitation through a closed-loop learning process of perception, action, and correction. CABIN first develops perceptual awareness by estimating epistemic uncertainty, identifying ambiguous regions where errors are likely to occur. It then acts by adopting an Uncertainty-Guided Dual Sampling Strategy, selecting uncertain samples for exploration while anchoring confident ones as stable pseudo-labels to reduce bias. To correct noisy supervision, CABIN introduces a Fine-Grained Dynamic Assignment Strategy that categorizes pseudo-labeled data into reliable, ambiguous, and noisy subsets, applying tailored losses to enhance generalization. Experimental results show that a wide range of state-of-the-art methods benefit from the integration of CABIN, with improved labeling efficiency and performance.

