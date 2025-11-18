---
layout: default
title: Hybrid-Domain Adaptative Representation Learning for Gaze Estimation
---

# Hybrid-Domain Adaptative Representation Learning for Gaze Estimation
**arXiv**：[2511.13222v1](https://arxiv.org/abs/2511.13222) · [PDF](https://arxiv.org/pdf/2511.13222.pdf)  
**作者**：Qida Tan, Hongyu Yang, Wenchao Du  

**一句话要点**：提出混合域自适应表示学习框架以提升跨域视线估计鲁棒性

**关键词**：视线估计, 域适应, 表示学习, 头部姿态融合, 跨域评估, 无监督学习

## 3 点简述
- 核心问题：跨域视线估计受表情、佩戴物等无关因素干扰，性能下降显著。
- 方法要点：通过无监督域适应对齐高低质量图像特征，并融合头部姿态几何约束。
- 实验或效果：在多个数据集上达到SOTA精度，如EyeDiap 5.02度，跨域评估表现优异。

## 摘要（原文）

> Appearance-based gaze estimation, aiming to predict accurate 3D gaze direction from a single facial image, has made promising progress in recent years. However, most methods suffer significant performance degradation in cross-domain evaluation due to interference from gaze-irrelevant factors, such as expressions, wearables, and image quality. To alleviate this problem, we present a novel Hybrid-domain Adaptative Representation Learning (shorted by HARL) framework that exploits multi-source hybrid datasets to learn robust gaze representation. More specifically, we propose to disentangle gaze-relevant representation from low-quality facial images by aligning features extracted from high-quality near-eye images in an unsupervised domain-adaptation manner, which hardly requires any computational or inference costs. Additionally, we analyze the effect of head-pose and design a simple yet efficient sparse graph fusion module to explore the geometric constraint between gaze direction and head-pose, leading to a dense and robust gaze representation. Extensive experiments on EyeDiap, MPIIFaceGaze, and Gaze360 datasets demonstrate that our approach achieves state-of-the-art accuracy of $\textbf{5.02}^{\circ}$ and $\textbf{3.36}^{\circ}$, and $\textbf{9.26}^{\circ}$ respectively, and present competitive performances through cross-dataset evaluation. The code is available at https://github.com/da60266/HARL.

