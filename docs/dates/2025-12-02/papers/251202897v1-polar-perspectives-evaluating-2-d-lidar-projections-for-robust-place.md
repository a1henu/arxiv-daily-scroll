---
layout: default
title: Polar Perspectives: Evaluating 2-D LiDAR Projections for Robust Place Recognition with Visual Foundation Models
---

# Polar Perspectives: Evaluating 2-D LiDAR Projections for Robust Place Recognition with Visual Foundation Models
**arXiv**：[2512.02897v1](https://arxiv.org/abs/2512.02897) · [PDF](https://arxiv.org/pdf/2512.02897.pdf)  
**作者**：Pierpaolo Serio, Giulio Pisaneschi, Andrea Dan Ryals, Vincenzo Infantino, Lorenzo Gentilini, Valentina Donzella, Lorenzo Pollini  

**一句话要点**：评估2D LiDAR投影对视觉基础模型在稳健地点识别中的影响

**关键词**：LiDAR投影, 地点识别, 视觉基础模型, 模块化检索, 环境鲁棒性, 实时自主性

## 3 点简述
- 核心问题：不同LiDAR到图像投影如何影响基于视觉基础模型的度量地点识别性能
- 方法要点：采用模块化检索管道，控制骨干网络、聚合和评估协议，隔离投影本身的影响
- 实验或效果：通过多数据集实验，识别投影特性对判别力、环境鲁棒性和实时自主性的关键作用

## 摘要（原文）

> This work presents a systematic investigation into how alternative LiDAR-to-image projections affect metric place recognition when coupled with a state-of-the-art vision foundation model. We introduce a modular retrieval pipeline that controls for backbone, aggregation, and evaluation protocol, thereby isolating the influence of the 2-D projection itself. Using consistent geometric and structural channels across multiple datasets and deployment scenarios, we identify the projection characteristics that most strongly determine discriminative power, robustness to environmental variation, and suitability for real-time autonomy. Experiments with different datasets, including integration into an operational place recognition policy, validate the practical relevance of these findings and demonstrate that carefully designed projections can serve as an effective surrogate for end-to-end 3-D learning in LiDAR place recognition.

