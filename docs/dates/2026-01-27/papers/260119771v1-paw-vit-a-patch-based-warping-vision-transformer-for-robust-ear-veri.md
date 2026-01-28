---
layout: default
title: PaW-ViT: A Patch-based Warping Vision Transformer for Robust Ear Verification
---

# PaW-ViT: A Patch-based Warping Vision Transformer for Robust Ear Verification
**arXiv**：[2601.19771v1](https://arxiv.org/abs/2601.19771) · [PDF](https://arxiv.org/pdf/2601.19771.pdf)  
**作者**：Deeksha Arun, Kevin W. Bowyer, Patrick Flynn  

**一句话要点**：提出PaW-ViT预处理方法，基于解剖知识对齐耳部特征边界以增强ViT在耳部验证中的鲁棒性。

**关键词**：耳部验证, 视觉Transformer, 图像预处理, 特征对齐, 生物识别

## 3 点简述
- 核心问题：ViT中矩形token常包含目标外信息，影响耳部验证性能。
- 方法要点：通过解剖知识对齐token边界到耳部特征边界，归一化图像以提升ViT效果。
- 实验或效果：在多种ViT模型上验证有效性，对形状、大小和姿态变化展现鲁棒性。

## 摘要（原文）

> The rectangular tokens common to vision transformer methods for visual recognition can strongly affect performance of these methods due to incorporation of information outside the objects to be recognized. This paper introduces PaW-ViT, Patch-based Warping Vision Transformer, a preprocessing approach rooted in anatomical knowledge that normalizes ear images to enhance the efficacy of ViT. By accurately aligning token boundaries to detected ear feature boundaries, PaW-ViT obtains greater robustness to shape, size, and pose variation. By aligning feature boundaries to natural ear curvature, it produces more consistent token representations for various morphologies. Experiments confirm the effectiveness of PaW-ViT on various ViT models (ViT-T, ViT-S, ViT-B, ViT-L) and yield reasonable alignment robustness to variation in shape, size, and pose. Our work aims to solve the disconnect between ear biometric morphological variation and transformer architecture positional sensitivity, presenting a possible avenue for authentication schemes.

