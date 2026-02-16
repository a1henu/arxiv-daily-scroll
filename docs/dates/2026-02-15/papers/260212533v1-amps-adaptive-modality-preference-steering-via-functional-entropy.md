---
layout: default
title: AMPS: Adaptive Modality Preference Steering via Functional Entropy
---

# AMPS: Adaptive Modality Preference Steering via Functional Entropy
**arXiv**：[2602.12533v1](https://arxiv.org/abs/2602.12533) · [PDF](https://arxiv.org/pdf/2602.12533.pdf)  
**作者**：Zihan Huang, Xintong Li, Rohan Surana, Tong Yu, Rui Wang, Julian McAuley, Jingbo Shang, Junda Wu  

**一句话要点**：提出自适应模态偏好引导方法，通过功能熵量化信息贡献，实现实例感知控制以解决多模态大语言模型模态偏好问题。

**关键词**：多模态大语言模型, 模态偏好, 功能熵, 实例感知控制, 自适应引导

## 3 点简述
- 多模态大语言模型存在模态偏好问题，如过度依赖语言先验或视觉证据，影响推理准确性。
- 引入实例感知诊断指标量化模态信息贡献，基于此设计缩放策略和可学习模块，实现样本特异性引导。
- 实验表明，该方法在调整模态偏好时优于传统方法，有效降低生成错误率，保持标准推理性能。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) often exhibit significant modality preference, which is a tendency to favor one modality over another. Depending on the input, they may over-rely on linguistic priors relative to visual evidence, or conversely over-attend to visually salient but facts in textual contexts. Prior work has applied a uniform steering intensity to adjust the modality preference of MLLMs. However, strong steering can impair standard inference and increase error rates, whereas weak steering is often ineffective. In addition, because steering sensitivity varies substantially across multimodal instances, a single global strength is difficult to calibrate. To address this limitation with minimal disruption to inference, we introduce an instance-aware diagnostic metric that quantifies each modality's information contribution and reveals sample-specific susceptibility to steering. Building on these insights, we propose a scaling strategy that reduces steering for sensitive samples and a learnable module that infers scaling patterns, enabling instance-aware control of modality preference. Experimental results show that our instance-aware steering outperforms conventional steering in modulating modality preference, achieving effective adjustment while keeping generation error rates low.

