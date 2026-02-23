---
layout: default
title: MeanVoiceFlow: One-step Nonparallel Voice Conversion with Mean Flows
---

# MeanVoiceFlow: One-step Nonparallel Voice Conversion with Mean Flows
**arXiv**：[2602.18104v1](https://arxiv.org/abs/2602.18104) · [PDF](https://arxiv.org/pdf/2602.18104.pdf)  
**作者**：Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Yuto Kondo  

**一句话要点**：提出MeanVoiceFlow以解决非并行语音转换中迭代推理慢的问题

**关键词**：语音转换, 平均流, 一步推理, 非并行训练, 结构边缘重建损失, 条件扩散输入

## 3 点简述
- 核心问题：扩散和流匹配模型在语音转换中因迭代推理导致转换速度慢
- 方法要点：基于平均流的一步非并行模型，引入结构边缘重建损失和条件扩散输入训练
- 实验或效果：性能与多步和基于蒸馏的模型相当，无需预训练或蒸馏

## 摘要（原文）

> In voice conversion (VC) applications, diffusion and flow-matching models have exhibited exceptional speech quality and speaker similarity performances. However, they are limited by slow conversion owing to their iterative inference. Consequently, we propose MeanVoiceFlow, a novel one-step nonparallel VC model based on mean flows, which can be trained from scratch without requiring pretraining or distillation. Unlike conventional flow matching that uses instantaneous velocity, mean flows employ average velocity to more accurately compute the time integral along the inference path in a single step. However, training the average velocity requires its derivative to compute the target velocity, which can cause instability. Therefore, we introduce a structural margin reconstruction loss as a zero-input constraint, which moderately regularizes the input-output behavior of the model without harmful statistical averaging. Furthermore, we propose conditional diffused-input training in which a mixture of noise and source data is used as input to the model during both training and inference. This enables the model to effectively leverage source information while maintaining consistency between training and inference. Experimental results validate the effectiveness of these techniques and demonstrate that MeanVoiceFlow achieves performance comparable to that of previous multi-step and distillation-based models, even when trained from scratch. Audio samples are available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/meanvoiceflow/.

