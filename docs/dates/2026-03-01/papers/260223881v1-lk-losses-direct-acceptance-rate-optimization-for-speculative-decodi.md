---
layout: default
title: LK Losses: Direct Acceptance Rate Optimization for Speculative Decoding
---

# LK Losses: Direct Acceptance Rate Optimization for Speculative Decoding
**arXiv**：[2602.23881v1](https://arxiv.org/abs/2602.23881) · [PDF](https://arxiv.org/pdf/2602.23881.pdf)  
**作者**：Alexander Samarin, Sergei Krutikov, Anton Shevtsov, Sergei Skvortsov, Filipp Fisin, Alexander Golubev  

**一句话要点**：提出LK损失函数以直接优化推测解码中的接受率

**关键词**：推测解码, 接受率优化, 损失函数设计, 大语言模型推理, 草稿模型训练

## 3 点简述
- 核心问题：标准KL散度训练在小草稿模型中无法最大化接受率，导致推测解码加速受限
- 方法要点：设计LK损失函数，直接以接受率为训练目标，无需额外计算开销
- 实验或效果：在多种模型配置和领域测试中，平均接受长度提升达8-10%，效果一致优于KL训练

## 摘要（原文）

> Speculative decoding accelerates autoregressive large language model (LLM) inference by using a lightweight draft model to propose candidate tokens that are then verified in parallel by the target model. The speedup is significantly determined by the acceptance rate, yet standard training minimizes Kullback-Leibler (KL) divergence as a proxy objective. While KL divergence and acceptance rate share the same global optimum, small draft models, having limited capacity, typically converge to suboptimal solutions where minimizing KL does not guarantee maximizing acceptance rate. To address this issue, we propose LK losses, special training objectives that directly target acceptance rate. Comprehensive experiments across four draft architectures and six target models, ranging from 8B to 685B parameters, demonstrate consistent improvements in acceptance metrics across all configurations compared to the standard KL-based training. We evaluate our approach on general, coding and math domains and report gains of up to 8-10% in average acceptance length. LK losses are easy to implement, introduce no computational overhead and can be directly integrated into any existing speculator training framework, making them a compelling alternative to the existing draft training objectives.

