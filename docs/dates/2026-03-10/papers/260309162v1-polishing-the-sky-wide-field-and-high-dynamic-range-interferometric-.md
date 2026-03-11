---
layout: default
title: POLISH'ing the Sky: Wide-Field and High-Dynamic Range Interferometric Image Reconstruction with Application to Strong Lens Discovery
---

# POLISH'ing the Sky: Wide-Field and High-Dynamic Range Interferometric Image Reconstruction with Application to Strong Lens Discovery
**arXiv**：[2603.09162v1](https://arxiv.org/abs/2603.09162) · [PDF](https://arxiv.org/pdf/2603.09162.pdf)  
**作者**：Zihui Wu, Liam Connor, Samuel McCarty, Katherine L. Bouman  

**一句话要点**：提出改进的POLISH框架，以解决射电干涉成像中高动态范围和大视场的挑战

**关键词**：射电干涉成像, 深度学习, 高动态范围处理, 大视场成像, 强引力透镜, 图像重建

## 3 点简述
- 核心问题：现有深度学习方法在真实射电干涉成像中处理高动态范围、大视场及训练-测试不匹配时表现不足
- 方法要点：引入分块训练拼接策略和非线性arcsinh强度变换，提升模型鲁棒性和超分辨率能力
- 实验或效果：在T-RECS模拟套件中评估，显著改善重建质量，并应用于强引力透镜发现，潜在提升探测效率

## 摘要（原文）

> Radio interferometry enables high-resolution imaging of astronomical radio sources by synthesizing a large effective aperture from an array of antennas and solving a deconvolution problem to reconstruct the image. Deep learning has emerged as a promising solution to the imaging problem, reducing computational costs and enabling super-resolution. However, existing DL-based methods often fall short of the requirements for real-world deployment due to limitations in handling high dynamic range, large field of view, and mismatches between training and test conditions. In this work, we build upon and extend the POLISH framework, a recent DL model for radio interferometric imaging. We introduce key improvements to enable robust reconstruction and super-resolution under real-world conditions: (1) a patch-wise training and stitching strategy for scaling to wide-field imaging and (2) a nonlinear arcsinh-based intensity transformation to manage high dynamic range. We conduct comprehensive evaluations using the T-RECS simulation suite with realistic sky models and point spead functions (PSF), and demonstrate that our approach significantly improves reconstruction quality and robustness. We test the model on realistic simulated strong gravitational lenses and show that lens systems with Einstein radii near the PSF scale can be recovered after deconvolution with our POLISH model, potentially yielding 10$\times$ more galaxy-galaxy lensing systems from the Deep Synoptic Array (DSA) survey than with image-plane CLEAN. Our results highlight the potential of DL models as practical, scalable tools for next-generation radio astronomy.

