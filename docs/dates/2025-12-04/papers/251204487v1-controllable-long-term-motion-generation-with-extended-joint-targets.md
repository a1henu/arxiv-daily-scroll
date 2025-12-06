---
layout: default
title: Controllable Long-term Motion Generation with Extended Joint Targets
---

# Controllable Long-term Motion Generation with Extended Joint Targets
**arXiv**：[2512.04487v1](https://arxiv.org/abs/2512.04487) · [PDF](https://arxiv.org/pdf/2512.04487.pdf)  
**作者**：Eunjong Lee, Eunhee Kim, Sanghoon Hong, Eunho Jung, Jihoon Kim  

**一句话要点**：提出COMET框架以解决实时生成可控长序列角色运动的挑战

**关键词**：角色动画, 长序列运动生成, 实时控制, Transformer, 条件VAE, 风格迁移

## 3 点简述
- 核心问题：现有方法在长序列中难以提供细粒度控制或避免运动退化
- 方法要点：基于Transformer的条件VAE实现实时交互控制，引入参考引导反馈机制确保稳定性
- 实验或效果：在复杂运动控制任务中显著优于先进方法，支持实时风格迁移

## 摘要（原文）

> Generating stable and controllable character motion in real-time is a key challenge in computer animation. Existing methods often fail to provide fine-grained control or suffer from motion degradation over long sequences, limiting their use in interactive applications. We propose COMET, an autoregressive framework that runs in real time, enabling versatile character control and robust long-horizon synthesis. Our efficient Transformer-based conditional VAE allows for precise, interactive control over arbitrary user-specified joints for tasks like goal-reaching and in-betweening from a single model. To ensure long-term temporal stability, we introduce a novel reference-guided feedback mechanism that prevents error accumulation. This mechanism also serves as a plug-and-play stylization module, enabling real-time style transfer. Extensive evaluations demonstrate that COMET robustly generates high-quality motion at real-time speeds, significantly outperforming state-of-the-art approaches in complex motion control tasks and confirming its readiness for demanding interactive applications.

