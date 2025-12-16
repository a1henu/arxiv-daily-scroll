---
layout: default
title: What Happens Next? Next Scene Prediction with a Unified Video Model
---

# What Happens Next? Next Scene Prediction with a Unified Video Model
**arXiv**：[2512.13015v1](https://arxiv.org/abs/2512.13015) · [PDF](https://arxiv.org/pdf/2512.13015.pdf)  
**作者**：Xinjie Li, Zhimin Chen, Rui Zhao, Florian Schiffers, Zhenyu Liao, Vimal Bhat  

**一句话要点**：提出Next Scene Prediction任务与统一框架，以增强视频模型的时序与因果推理能力。

**关键词**：Next Scene Prediction, 统一视频模型, 时序推理, 因果一致性奖励, 多模态系统, 强化学习

## 3 点简述
- 核心问题：统一视频模型在时序推理方面潜力未充分探索，需预测未来场景。
- 方法要点：结合Qwen-VL和LTX，通过潜在查询嵌入和连接模块，分三阶段训练。
- 实验或效果：在新数据集上实现最佳性能，提升多模态系统预测能力。

## 摘要（原文）

> Recent unified models for joint understanding and generation have significantly advanced visual generation capabilities. However, their focus on conventional tasks like text-to-video generation has left the temporal reasoning potential of unified models largely underexplored. To address this gap, we introduce Next Scene Prediction (NSP), a new task that pushes unified video models toward temporal and causal reasoning. Unlike text-to-video generation, NSP requires predicting plausible futures from preceding context, demanding deeper understanding and reasoning. To tackle this task, we propose a unified framework combining Qwen-VL for comprehension and LTX for synthesis, bridged by a latent query embedding and a connector module. This model is trained in three stages on our newly curated, large-scale NSP dataset: text-to-video pre-training, supervised fine-tuning, and reinforcement learning (via GRPO) with our proposed causal consistency reward. Experiments demonstrate our model achieves state-of-the-art performance on our benchmark, advancing the capability of generalist multimodal systems to anticipate what happens next.

