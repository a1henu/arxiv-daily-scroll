---
layout: default
title: Learning Depth from Past Selves: Self-Evolution Contrast for Robust Depth Estimation
---

# Learning Depth from Past Selves: Self-Evolution Contrast for Robust Depth Estimation
**arXiv**：[2511.15167v1](https://arxiv.org/abs/2511.15167) · [PDF](https://arxiv.org/pdf/2511.15167.pdf)  
**作者**：Jing Cao, Kui Jiang, Shenyi Li, Xiaocheng Feng, Yong Huang  

**一句话要点**：提出自进化对比学习框架以提升恶劣天气下自监督深度估计的鲁棒性

**关键词**：自监督深度估计, 对比学习, 恶劣天气鲁棒性, 零样本评估, 时延模型

## 3 点简述
- 核心问题：现有自监督深度估计方法在雨雾等恶劣天气下性能显著下降
- 方法要点：利用训练中间参数构建时延模型，设计自进化对比损失以自适应调整学习目标
- 实验或效果：在零样本评估中显著增强鲁棒性，可无缝集成多种基线模型

## 摘要（原文）

> Self-supervised depth estimation has gained significant attention in autonomous driving and robotics. However, existing methods exhibit substantial performance degradation under adverse weather conditions such as rain and fog, where reduced visibility critically impairs depth prediction. To address this issue, we propose a novel self-evolution contrastive learning framework called SEC-Depth for self-supervised robust depth estimation tasks. Our approach leverages intermediate parameters generated during training to construct temporally evolving latency models. Using these, we design a self-evolution contrastive scheme to mitigate performance loss under challenging conditions. Concretely, we first design a dynamic update strategy of latency models for the depth estimation task to capture optimization states across training stages. To effectively leverage latency models, we introduce a self-evolution contrastive Loss (SECL) that treats outputs from historical latency models as negative samples. This mechanism adaptively adjusts learning objectives while implicitly sensing weather degradation severity, reducing the needs for manual intervention. Experiments show that our method integrates seamlessly into diverse baseline models and significantly enhances robustness in zero-shot evaluations.

