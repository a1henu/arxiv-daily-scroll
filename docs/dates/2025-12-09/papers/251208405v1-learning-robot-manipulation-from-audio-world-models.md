---
layout: default
title: Learning Robot Manipulation from Audio World Models
---

# Learning Robot Manipulation from Audio World Models
**arXiv**：[2512.08405v1](https://arxiv.org/abs/2512.08405) · [PDF](https://arxiv.org/pdf/2512.08405.pdf)  
**作者**：Fan Zhang, Michael Gienger  

**一句话要点**：提出生成式潜在流匹配模型以预测未来音频，增强机器人操作中的多模态推理能力。

**关键词**：机器人操作学习, 多模态推理, 音频世界模型, 生成式模型, 潜在流匹配

## 3 点简述
- 核心问题：机器人操作任务中仅依赖视觉信息可能不完整，需结合音频的时序演化进行推理。
- 方法要点：使用生成式潜在流匹配模型预测未来音频观测，集成到机器人策略中以推理长期后果。
- 实验或效果：在需要感知真实音频或音乐信号的操作任务中，相比无未来预测的方法展现优越性能。

## 摘要（原文）

> World models have demonstrated impressive performance on robotic learning tasks. Many such tasks inherently demand multimodal reasoning; for example, filling a bottle with water will lead to visual information alone being ambiguous or incomplete, thereby requiring reasoning over the temporal evolution of audio, accounting for its underlying physical properties and pitch patterns. In this paper, we propose a generative latent flow matching model to anticipate future audio observations, enabling the system to reason about long-term consequences when integrated into a robot policy. We demonstrate the superior capabilities of our system through two manipulation tasks that require perceiving in-the-wild audio or music signals, compared to methods without future lookahead. We further emphasize that successful robot action learning for these tasks relies not merely on multi-modal input, but critically on the accurate prediction of future audio states that embody intrinsic rhythmic patterns.

