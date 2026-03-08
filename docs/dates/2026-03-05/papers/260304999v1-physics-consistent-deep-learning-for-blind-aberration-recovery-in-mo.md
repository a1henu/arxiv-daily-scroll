---
layout: default
title: Physics-consistent deep learning for blind aberration recovery in mobile optics
---

# Physics-consistent deep learning for blind aberration recovery in mobile optics
**arXiv**：[2603.04999v1](https://arxiv.org/abs/2603.04999) · [PDF](https://arxiv.org/pdf/2603.04999.pdf)  
**作者**：Kartik Jhawar, Tamo Sancho Miguel Tandoc, Khoo Jun Xuan, Wang Lipo  

**一句话要点**：提出Lens2Zernike框架，通过物理一致深度学习从单张模糊图像盲恢复移动镜头光学参数

**关键词**：盲像差恢复, 物理一致深度学习, Zernike系数回归, 移动镜头光学, 非盲去卷积, 多任务学习

## 3 点简述
- 移动摄影受镜头特定光学像差限制，现有深度学习方法缺乏显式光学建模，易产生幻觉细节
- Lens2Zernike集成Zernike系数回归、可微物理约束和空间图预测，实现多任务监督
- 在ResNet-18上，完整框架比仅系数基线提升35%，优于先前深度学习方法，支持稳定非盲去卷积

## 摘要（原文）

> Mobile photography is often limited by complex, lens-specific optical aberrations. While recent deep learning methods approach this as an end-to-end deblurring task, these "black-box" models lack explicit optical modeling and can hallucinate details. Conversely, classical blind deconvolution remains highly unstable. To bridge this gap, we present Lens2Zernike, a deep learning framework that blindly recovers physical optical parameters from a single blurred image. To the best of our knowledge, no prior work has simultaneously integrated supervision across three distinct optical domains. We introduce a novel physics-consistent strategy that explicitly minimizes errors via direct Zernike coefficient regression (z), differentiable physics constraints encompassing both wavefront and point spread function derivations (p), and auxiliary multi-task spatial map predictions (m). Through an ablation study on a ResNet-18 backbone, we demonstrate that our full multi-task framework (z+p+m) yields a 35% improvement over coefficient-only baselines. Crucially, comparative analysis reveals that our approach outperforms two established deep learning methods from previous literature, achieving significantly lower regression errors. Ultimately, we demonstrate that these recovered physical parameters enable stable non-blind deconvolution, providing substantial in-domain improvement on the patented Institute for Digital Molecular Analytics and Science (IDMxS) Mobile Camera Lens Database for restoring diffraction-limited details from severely aberrated mobile captures.

