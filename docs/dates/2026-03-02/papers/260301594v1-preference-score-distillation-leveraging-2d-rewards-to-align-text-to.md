---
layout: default
title: Preference Score Distillation: Leveraging 2D Rewards to Align Text-to-3D Generation with Human Preference
---

# Preference Score Distillation: Leveraging 2D Rewards to Align Text-to-3D Generation with Human Preference
**arXiv**：[2603.01594v1](https://arxiv.org/abs/2603.01594) · [PDF](https://arxiv.org/pdf/2603.01594.pdf)  
**作者**：Jiaqi Leng, Shuyuan Tu, Haidong Cao, Sicheng Xie, Daoguo Dong, Zuxuan Wu, Yu-Gang Jiang  

**一句话要点**：提出偏好分数蒸馏以利用2D奖励模型实现无3D数据的人类偏好对齐文本到3D生成

**关键词**：文本到3D生成, 人类偏好对齐, 分数蒸馏, 无分类器引导, 2D奖励模型, 优化框架

## 3 点简述
- 核心问题：文本到3D生成中人类偏好对齐缺乏3D训练数据，现有方法需任务特定微调。
- 方法要点：基于优化框架，通过隐式奖励模型将偏好对齐重构为无分类器引导机制，并自适应优化偏好分数和负文本嵌入。
- 实验或效果：在美学指标上表现优越，能无缝集成多种流程，并展示强扩展性。

## 摘要（原文）

> Human preference alignment presents a critical yet underexplored challenge for diffusion models in text-to-3D generation. Existing solutions typically require task-specific fine-tuning, posing significant hurdles in data-scarce 3D domains. To address this, we propose Preference Score Distillation (PSD), an optimization-based framework that leverages pretrained 2D reward models for human-aligned text-to-3D synthesis without 3D training data. Our key insight stems from the incompatibility of pixel-level gradients: due to the absence of noisy samples during reward model training, direct application of 2D reward gradients disturbs the denoising process. Noticing that similar issue occurs in the naive classifier guidance in conditioned diffusion models, we fundamentally rethink preference alignment as a classifier-free guidance (CFG)-style mechanism through our implicit reward model. Furthermore, recognizing that frozen pretrained diffusion models constrain performance, we introduce an adaptive strategy to co-optimize preference scores and negative text embeddings. By incorporating CFG during optimization, online refinement of negative text embeddings dynamically enhances alignment. To our knowledge, we are the first to bridge human preference alignment with CFG theory under score distillation framework. Experiments demonstrate the superiority of PSD in aesthetic metrics, seamless integration with diverse pipelines, and strong extensibility.

