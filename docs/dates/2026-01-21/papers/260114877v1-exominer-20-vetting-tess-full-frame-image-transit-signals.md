---
layout: default
title: ExoMiner++ 2.0: Vetting TESS Full-Frame Image Transit Signals
---

# ExoMiner++ 2.0: Vetting TESS Full-Frame Image Transit Signals
**arXiv**：[2601.14877v1](https://arxiv.org/abs/2601.14877) · [PDF](https://arxiv.org/pdf/2601.14877.pdf)  
**作者**：Miguel J. S. Martinho, Hamed Valizadegan, Jon M. Jenkins, Douglas A. Caldwell, Joseph D. Twicken, Ben Tofflemire, Marziye Jafariyazani  

**一句话要点**：应用ExoMiner++ 2.0模型于TESS全帧图像数据，实现大规模行星信号分类与验证

**关键词**：行星凌星信号分类, TESS全帧图像, 机器学习模型, 天体物理假阳性, 仪器伪影, 大规模验证

## 3 点简述
- 核心问题：TESS全帧图像数据在行星凌星信号识别与验证中面临挑战，如数据采样率较低。
- 方法要点：将ExoMiner++框架适配至全帧图像光变曲线，进行行星与非行星信号的分类。
- 实验或效果：模型在全帧图像领域泛化有效，能区分行星信号、天体物理假阳性和仪器伪影。

## 摘要（原文）

> The Transiting Exoplanet Survey Satellite (TESS) Full-Frame Images (FFIs) provide photometric time series for millions of stars, enabling transit searches beyond the limited set of pre-selected 2-minute targets. However, FFIs present additional challenges for transit identification and vetting. In this work, we apply ExoMiner++ 2.0, an adaptation of the ExoMiner++ framework originally developed for TESS 2-minute data, to FFI light curves. The model is used to perform large-scale planet versus non-planet classification of Threshold Crossing Events across the sectors analyzed in this study. We construct a uniform vetting catalog of all evaluated signals and assess model performance under different observing conditions. We find that ExoMiner++ 2.0 generalizes effectively to the FFI domain, providing robust discrimination between planetary signals, astrophysical false positives, and instrumental artifacts despite the limitations inherent to longer cadence data. This work extends the applicability of ExoMiner++ to the full TESS dataset and supports future population studies and follow-up prioritization.

