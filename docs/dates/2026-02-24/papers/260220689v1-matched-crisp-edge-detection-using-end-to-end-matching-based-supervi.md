---
layout: default
title: MatchED: Crisp Edge Detection Using End-to-End, Matching-based Supervision
---

# MatchED: Crisp Edge Detection Using End-to-End, Matching-based Supervision
**arXiv**：[2602.20689v1](https://arxiv.org/abs/2602.20689) · [PDF](https://arxiv.org/pdf/2602.20689.pdf)  
**作者**：Bedrettin Cetinkaya, Sinan Kalkan, Emre Akbas  

**一句话要点**：提出MatchED模块以解决边缘检测中非端到端后处理导致的模糊边缘问题

**关键词**：边缘检测, 端到端学习, 匹配监督, 轻量级模块, 后处理优化

## 3 点简述
- 核心问题：现有方法依赖非可微后处理（如NMS）生成单像素宽边缘，阻碍端到端优化
- 方法要点：引入轻量级匹配监督模块，基于空间距离和置信度进行预测与真值边缘的一对一匹配
- 实验或效果：在四个数据集上显著提升边缘清晰度指标，首次达到或超越标准后处理的性能

## 摘要（原文）

> Generating crisp, i.e., one-pixel-wide, edge maps remains one of the fundamental challenges in edge detection, affecting both traditional and learning-based methods. To obtain crisp edges, most existing approaches rely on two hand-crafted post-processing algorithms, Non-Maximum Suppression (NMS) and skeleton-based thinning, which are non-differentiable and hinder end-to-end optimization. Moreover, all existing crisp edge detection methods still depend on such post-processing to achieve satisfactory results. To address this limitation, we propose \MethodLPP, a lightweight, only $\sim$21K additional parameters, and plug-and-play matching-based supervision module that can be appended to any edge detection model for joint end-to-end learning of crisp edges. At each training iteration, \MethodLPP performs one-to-one matching between predicted and ground-truth edges based on spatial distance and confidence, ensuring consistency between training and testing protocols. Extensive experiments on four popular datasets demonstrate that integrating \MethodLPP substantially improves the performance of existing edge detection models. In particular, \MethodLPP increases the Average Crispness (AC) metric by up to 2--4$\times$ compared to baseline models. Under the crispness-emphasized evaluation (CEval), \MethodLPP further boosts baseline performance by up to 20--35\% in ODS and achieves similar gains in OIS and AP, achieving SOTA performance that matches or surpasses standard post-processing for the first time. Code is available at https://cvpr26-matched.github.io.

