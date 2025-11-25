---
layout: default
title: BideDPO: Conditional Image Generation with Simultaneous Text and Condition Alignment
---

# BideDPO: Conditional Image Generation with Simultaneous Text and Condition Alignment
**arXiv**：[2511.19268v1](https://arxiv.org/abs/2511.19268) · [PDF](https://arxiv.org/pdf/2511.19268.pdf)  
**作者**：Dewei Zhou, Mingwei Li, Zongxin Yang, Yu Lu, Yunqiu Xu, Zhizhong Wang, Zeyi Huang, Yi Yang  

**一句话要点**：提出BideDPO框架以解决条件图像生成中的文本与条件冲突问题

**关键词**：条件图像生成, 偏好优化, 梯度解耦, 冲突解决, 自适应损失平衡

## 3 点简述
- 核心问题：条件图像生成中文本与条件源冲突，包括输入级和模型偏置冲突
- 方法要点：使用双向解耦偏好对和自适应损失平衡策略减少梯度纠缠
- 实验或效果：在DualAlign基准上显著提升文本成功率和条件遵循度

## 摘要（原文）

> Conditional image generation enhances text-to-image synthesis with structural, spatial, or stylistic priors, but current methods face challenges in handling conflicts between sources. These include 1) input-level conflicts, where the conditioning image contradicts the text prompt, and 2) model-bias conflicts, where generative biases disrupt alignment even when conditions match the text. Addressing these conflicts requires nuanced solutions, which standard supervised fine-tuning struggles to provide. Preference-based optimization techniques like Direct Preference Optimization (DPO) show promise but are limited by gradient entanglement between text and condition signals and lack disentangled training data for multi-constraint tasks. To overcome this, we propose a bidirectionally decoupled DPO framework (BideDPO). Our method creates two disentangled preference pairs-one for the condition and one for the text-to reduce gradient entanglement. The influence of pairs is managed using an Adaptive Loss Balancing strategy for balanced optimization. We introduce an automated data pipeline to sample model outputs and generate conflict-aware data. This process is embedded in an iterative optimization strategy that refines both the model and the data. We construct a DualAlign benchmark to evaluate conflict resolution between text and condition. Experiments show BideDPO significantly improves text success rates (e.g., +35%) and condition adherence. We also validate our approach using the COCO dataset. Project Pages: https://limuloo.github.io/BideDPO/.

