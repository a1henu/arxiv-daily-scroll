---
layout: default
title: RRNet: Configurable Real-Time Video Enhancement with Arbitrary Local Lighting Variations
---

# RRNet: Configurable Real-Time Video Enhancement with Arbitrary Local Lighting Variations
**arXiv**：[2601.01865v1](https://arxiv.org/abs/2601.01865) · [PDF](https://arxiv.org/pdf/2601.01865.pdf)  
**作者**：Wenlong Yang, Canran Jin, Weihang Yuan, Chao Wang, Lifeng Sun  

**一句话要点**：提出RRNet框架，通过虚拟光源参数估计实现实时视频增强，解决不均匀光照下的曝光控制问题。

**关键词**：实时视频增强, 局部重光照, 虚拟光源估计, 深度感知渲染, 轻量级网络, 生成式AI数据集

## 3 点简述
- 核心问题：现有方法在实时视频增强中难以平衡速度与不均匀光照下的有效曝光控制。
- 方法要点：使用轻量级网络估计虚拟光源参数，结合深度感知渲染模块进行局部重光照，无需像素对齐训练数据。
- 实验或效果：在低光增强、局部光照调整和眩光去除方面优于先前方法，支持实时高分辨率应用。

## 摘要（原文）

> With the growing demand for real-time video enhancement in live applications, existing methods often struggle to balance speed and effective exposure control, particularly under uneven lighting. We introduce RRNet (Rendering Relighting Network), a lightweight and configurable framework that achieves a state-of-the-art tradeoff between visual quality and efficiency. By estimating parameters for a minimal set of virtual light sources, RRNet enables localized relighting through a depth-aware rendering module without requiring pixel-aligned training data. This object-aware formulation preserves facial identity and supports real-time, high-resolution performance using a streamlined encoder and lightweight prediction head. To facilitate training, we propose a generative AI-based dataset creation pipeline that synthesizes diverse lighting conditions at low cost. With its interpretable lighting control and efficient architecture, RRNet is well suited for practical applications such as video conferencing, AR-based portrait enhancement, and mobile photography. Experiments show that RRNet consistently outperforms prior methods in low-light enhancement, localized illumination adjustment, and glare removal.

