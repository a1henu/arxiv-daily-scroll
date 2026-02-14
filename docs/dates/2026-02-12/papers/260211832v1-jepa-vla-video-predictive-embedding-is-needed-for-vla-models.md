---
layout: default
title: JEPA-VLA: Video Predictive Embedding is Needed for VLA Models
---

# JEPA-VLA: Video Predictive Embedding is Needed for VLA Models
**arXiv**：[2602.11832v1](https://arxiv.org/abs/2602.11832) · [PDF](https://arxiv.org/pdf/2602.11832.pdf)  
**作者**：Shangchen Miao, Ningya Feng, Jialong Wu, Ye Lin, Xu He, Dong Li, Mingsheng Long  

**一句话要点**：提出JEPA-VLA，通过集成预测嵌入提升视觉语言动作模型的样本效率和泛化能力

**关键词**：视觉语言动作模型, 视频预测嵌入, 样本效率, 泛化能力, 机器人操作, V-JEPA

## 3 点简述
- 当前视觉语言动作模型因视觉表示不足导致样本效率低和泛化受限
- 引入视频预测嵌入V-JEPA 2以编码任务相关动态并补偿现有表示缺陷
- 实验在多个基准和真实机器人任务中验证了性能显著提升

## 摘要（原文）

> Recent vision-language-action (VLA) models built upon pretrained vision-language models (VLMs) have achieved significant improvements in robotic manipulation. However, current VLAs still suffer from low sample efficiency and limited generalization. This paper argues that these limitations are closely tied to an overlooked component, pretrained visual representation, which offers insufficient knowledge on both aspects of environment understanding and policy prior. Through an in-depth analysis, we find that commonly used visual representations in VLAs, whether pretrained via language-image contrastive learning or image-based self-supervised learning, remain inadequate at capturing crucial, task-relevant environment information and at inducing effective policy priors, i.e., anticipatory knowledge of how the environment evolves under successful task execution. In contrast, we discover that predictive embeddings pretrained on videos, in particular V-JEPA 2, are adept at flexibly discarding unpredictable environment factors and encoding task-relevant temporal dynamics, thereby effectively compensating for key shortcomings of existing visual representations in VLAs. Building on these observations, we introduce JEPA-VLA, a simple yet effective approach that adaptively integrates predictive embeddings into existing VLAs. Our experiments demonstrate that JEPA-VLA yields substantial performance gains across a range of benchmarks, including LIBERO, LIBERO-plus, RoboTwin2.0, and real-robot tasks.

