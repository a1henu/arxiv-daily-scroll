---
layout: default
title: DreamVAR: Taming Reinforced Visual Autoregressive Model for High-Fidelity Subject-Driven Image Generation
---

# DreamVAR: Taming Reinforced Visual Autoregressive Model for High-Fidelity Subject-Driven Image Generation
**arXiv**：[2601.22507v1](https://arxiv.org/abs/2601.22507) · [PDF](https://arxiv.org/pdf/2601.22507.pdf)  
**作者**：Xin Jiang, Jingwen Chen, Yehao Li, Yingwei Pan, Kezhou Chen, Zechao Li, Ting Yao, Tao Mei  

**一句话要点**：提出DreamVAR框架，基于视觉自回归模型实现高保真主题驱动图像生成。

**关键词**：主题驱动图像生成, 视觉自回归模型, 多尺度特征, 强化学习, 高保真图像合成

## 3 点简述
- 核心问题：视觉自回归模型在主题驱动图像生成中潜力未充分挖掘，存在多尺度条件训练-测试差异。
- 方法要点：采用先填充完整主题特征序列再预测目标图像令牌的设计，简化自回归依赖并引入强化学习增强语义对齐和主题一致性。
- 实验或效果：在实验中优于领先的基于扩散的方法，实现更优的外观保持。

## 摘要（原文）

> Recent advances in subject-driven image generation using diffusion models have attracted considerable attention for their remarkable capabilities in producing high-quality images. Nevertheless, the potential of Visual Autoregressive (VAR) models, despite their unified architecture and efficient inference, remains underexplored. In this work, we present DreamVAR, a novel framework for subject-driven image synthesis built upon a VAR model that employs next-scale prediction. Technically, multi-scale features of the reference subject are first extracted by a visual tokenizer. Instead of interleaving these conditional features with target image tokens across scales, our DreamVAR pre-fills the full subject feature sequence prior to predicting target image tokens. This design simplifies autoregressive dependencies and mitigates the train-test discrepancy in multi-scale conditioning scenario within the VAR paradigm. DreamVAR further incorporates reinforcement learning to jointly enhance semantic alignment and subject consistency. Extensive experiments demonstrate that DreamVAR achieves superior appearance preservation compared to leading diffusion-based methods.

