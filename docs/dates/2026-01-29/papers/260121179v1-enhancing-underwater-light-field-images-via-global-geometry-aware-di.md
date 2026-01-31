---
layout: default
title: Enhancing Underwater Light Field Images via Global Geometry-aware Diffusion Process
---

# Enhancing Underwater Light Field Images via Global Geometry-aware Diffusion Process
**arXiv**：[2601.21179v1](https://arxiv.org/abs/2601.21179) · [PDF](https://arxiv.org/pdf/2601.21179.pdf)  
**作者**：Yuji Lin, Qian Zhao, Zongsheng Yue, Junhui Hou, Deyu Meng  

**一句话要点**：提出GeoDiff-LF以增强水下光场成像质量

**关键词**：水下成像, 光场增强, 扩散模型, 几何感知, 颜色校正

## 3 点简述
- 核心问题：水下4-D光场成像存在颜色失真等挑战
- 方法要点：基于SD-Turbo的扩散框架，结合几何适配器和损失函数
- 实验或效果：在视觉保真度和量化指标上优于现有方法

## 摘要（原文）

> This work studies the challenging problem of acquiring high-quality underwater images via 4-D light field (LF) imaging. To this end, we propose GeoDiff-LF, a novel diffusion-based framework built upon SD-Turbo to enhance underwater 4-D LF imaging by leveraging its spatial-angular structure. GeoDiff-LF consists of three key adaptations: (1) a modified U-Net architecture with convolutional and attention adapters to model geometric cues, (2) a geometry-guided loss function using tensor decomposition and progressive weighting to regularize global structure, and (3) an optimized sampling strategy with noise prediction to improve efficiency. By integrating diffusion priors and LF geometry, GeoDiff-LF effectively mitigates color distortion in underwater scenes. Extensive experiments demonstrate that our framework outperforms existing methods across both visual fidelity and quantitative performance, advancing the state-of-the-art in enhancing underwater imaging. The code will be publicly available at https://github.com/linlos1234/GeoDiff-LF.

