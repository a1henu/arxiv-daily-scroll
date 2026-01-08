---
layout: default
title: PhysVideoGenerator: Towards Physically Aware Video Generation via Latent Physics Guidance
---

# PhysVideoGenerator: Towards Physically Aware Video Generation via Latent Physics Guidance
**arXiv**：[2601.03665v1](https://arxiv.org/abs/2601.03665) · [PDF](https://arxiv.org/pdf/2601.03665.pdf)  
**作者**：Siddarth Nilol Kundur Satish, Devesh Jaiswal, Hongyu Chen, Abhishek Bakshi  

**一句话要点**：提出PhysVideoGenerator，通过潜在物理引导增强视频生成中的物理真实性。

**关键词**：视频生成, 物理先验, 扩散模型, 潜在引导, 多任务优化

## 3 点简述
- 当前视频生成模型难以学习真实世界物理动态，导致不自然碰撞和闪烁。
- 引入PredictorP从扩散潜在中回归V-JEPA 2物理特征，注入DiT生成器。
- 验证了联合训练的技术可行性，包括潜在信息恢复和训练稳定性。

## 摘要（原文）

> Current video generation models produce high-quality aesthetic videos but often struggle to learn representations of real-world physics dynamics, resulting in artifacts such as unnatural object collisions, inconsistent gravity, and temporal flickering. In this work, we propose PhysVideoGenerator, a proof-of-concept framework that explicitly embeds a learnable physics prior into the video generation process. We introduce a lightweight predictor network, PredictorP, which regresses high-level physical features extracted from a pre-trained Video Joint Embedding Predictive Architecture (V-JEPA 2) directly from noisy diffusion latents. These predicted physics tokens are injected into the temporal attention layers of a DiT-based generator (Latte) via a dedicated cross-attention mechanism. Our primary contribution is demonstrating the technical feasibility of this joint training paradigm: we show that diffusion latents contain sufficient information to recover V-JEPA 2 physical representations, and that multi-task optimization remains stable over training. This report documents the architectural design, technical challenges, and validation of training stability, establishing a foundation for future large-scale evaluation of physics-aware generative models.

