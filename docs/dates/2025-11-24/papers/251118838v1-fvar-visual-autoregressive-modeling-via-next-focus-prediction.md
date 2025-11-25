---
layout: default
title: FVAR: Visual Autoregressive Modeling via Next Focus Prediction
---

# FVAR: Visual Autoregressive Modeling via Next Focus Prediction
**arXiv**：[2511.18838v1](https://arxiv.org/abs/2511.18838) · [PDF](https://arxiv.org/pdf/2511.18838.pdf)  
**作者**：Xiaofan Li, Chenming Wu, Yanpeng Sun, Jiaming Zhou, Delin Qu, Yansong Qu, Weihao Bo, Haibao Yu, Dingkang Liang  

**一句话要点**：提出FVAR通过下一焦点预测解决视觉自回归模型中的混叠伪影问题

**关键词**：视觉自回归建模, 混叠伪影消除, 多尺度表示, 焦点预测, 高频残差学习, 图像生成

## 3 点简述
- 核心问题：传统多尺度自回归模型因均匀下采样产生混叠伪影，损害细节和引入锯齿
- 方法要点：引入下一焦点预测范式，使用物理一致散焦核构建无混叠金字塔，结合高频残差学习
- 实验或效果：在ImageNet上显著减少混叠，提升细节保留和文本可读性，兼容现有框架

## 摘要（原文）

> Visual autoregressive models achieve remarkable generation quality through next-scale predictions across multi-scale token pyramids. However, the conventional method uses uniform scale downsampling to build these pyramids, leading to aliasing artifacts that compromise fine details and introduce unwanted jaggies and moiré patterns. To tackle this issue, we present \textbf{FVAR}, which reframes the paradigm from \emph{next-scale prediction} to \emph{next-focus prediction}, mimicking the natural process of camera focusing from blur to clarity. Our approach introduces three key innovations: \textbf{1) Next-Focus Prediction Paradigm} that transforms multi-scale autoregression by progressively reducing blur rather than simply downsampling; \textbf{2) Progressive Refocusing Pyramid Construction} that uses physics-consistent defocus kernels to build clean, alias-free multi-scale representations; and \textbf{3) High-Frequency Residual Learning} that employs a specialized residual teacher network to effectively incorporate alias information during training while maintaining deployment simplicity. Specifically, we construct optical low-pass views using defocus point spread function (PSF) kernels with decreasing radius, creating smooth blur-to-clarity transitions that eliminate aliasing at its source. To further enhance detail generation, we introduce a High-Frequency Residual Teacher that learns from both clean structure and alias residuals, distilling this knowledge to a vanilla VAR deployment network for seamless inference. Extensive experiments on ImageNet demonstrate that FVAR substantially reduces aliasing artifacts, improves fine detail preservation, and enhances text readability, achieving superior performance with perfect compatibility to existing VAR frameworks.

