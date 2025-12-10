---
layout: default
title: Astra: General Interactive World Model with Autoregressive Denoising
---

# Astra: General Interactive World Model with Autoregressive Denoising
**arXiv**：[2512.08931v1](https://arxiv.org/abs/2512.08931) · [PDF](https://arxiv.org/pdf/2512.08931.pdf)  
**作者**：Yixuan Zhu, Jiaqi Feng, Wenzhao Zheng, Yuan Gao, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu  

**一句话要点**：提出Astra通用交互世界模型，通过自回归去噪架构实现多场景长时视频预测与精确动作控制。

**关键词**：世界模型, 自回归去噪, 长时视频预测, 动作控制, 通用交互, 扩散变换器

## 3 点简述
- 核心问题：现有世界模型在通用场景和多样化动作形式下的长时未来预测能力不足。
- 方法要点：采用自回归去噪架构，结合时间因果注意力和噪声增强历史记忆，引入动作感知适配器和动作专家混合机制。
- 实验或效果：在多个数据集上验证，Astra在保真度、长程预测和动作对齐方面优于现有先进模型。

## 摘要（原文）

> Recent advances in diffusion transformers have empowered video generation models to generate high-quality video clips from texts or images. However, world models with the ability to predict long-horizon futures from past observations and actions remain underexplored, especially for general-purpose scenarios and various forms of actions. To bridge this gap, we introduce Astra, an interactive general world model that generates real-world futures for diverse scenarios (e.g., autonomous driving, robot grasping) with precise action interactions (e.g., camera motion, robot action). We propose an autoregressive denoising architecture and use temporal causal attention to aggregate past observations and support streaming outputs. We use a noise-augmented history memory to avoid over-reliance on past frames to balance responsiveness with temporal coherence. For precise action control, we introduce an action-aware adapter that directly injects action signals into the denoising process. We further develop a mixture of action experts that dynamically route heterogeneous action modalities, enhancing versatility across diverse real-world tasks such as exploration, manipulation, and camera control. Astra achieves interactive, consistent, and general long-term video prediction and supports various forms of interactions. Experiments across multiple datasets demonstrate the improvements of Astra in fidelity, long-range prediction, and action alignment over existing state-of-the-art world models.

