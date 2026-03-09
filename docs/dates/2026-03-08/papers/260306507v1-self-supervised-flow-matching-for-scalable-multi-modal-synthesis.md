---
layout: default
title: Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
---

# Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
**arXiv**：[2603.06507v1](https://arxiv.org/abs/2603.06507) · [PDF](https://arxiv.org/pdf/2603.06507.pdf)  
**作者**：Hila Chefer, Patrick Esser, Dominik Lorenz, Dustin Podell, Vikash Raja, Vinh Tong, Antonio Torralba, Robin Rombach  

**一句话要点**：提出自监督流匹配方法Self-Flow，通过双时间步调度增强多模态生成中的语义表示学习。

**关键词**：自监督学习, 流匹配, 多模态生成, 语义表示学习, 双时间步调度

## 3 点简述
- 核心问题：现有扩散和流模型依赖外部模型学习语义表示，导致训练目标不一致和缩放行为异常。
- 方法要点：引入自监督流匹配范式，利用双时间步调度在令牌间应用异质噪声，迫使模型从损坏输入推断缺失信息。
- 实验或效果：方法跨模态通用，支持多模态训练，遵循预期缩放定律，在图像、视频和音频生成中表现优异。

## 摘要（原文）

> Strong semantic representations improve the convergence and generation quality of diffusion and flow models. Existing approaches largely rely on external models, which require separate training, operate on misaligned objectives, and exhibit unexpected scaling behavior. We argue that this dependence arises from the model's training objective, which poses a denoising task with little incentive to learn semantic representations. We introduce Self-Flow: a self-supervised flow matching paradigm that integrates representation learning within the generative framework. Our key mechanism, Dual-Timestep Scheduling, applies heterogeneous noise levels across tokens, creating an information asymmetry that forces the model to infer missing information from corrupted inputs. This drives learning strong representations alongside generative capabilities without external supervision. Our method generalizes across modalities and enables multi-modal training while following expected scaling laws, achieving superior image, video, and audio generation.

