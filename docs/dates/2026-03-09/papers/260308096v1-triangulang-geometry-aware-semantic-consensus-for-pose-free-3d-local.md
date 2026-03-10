---
layout: default
title: TrianguLang: Geometry-Aware Semantic Consensus for Pose-Free 3D Localization
---

# TrianguLang: Geometry-Aware Semantic Consensus for Pose-Free 3D Localization
**arXiv**：[2603.08096v1](https://arxiv.org/abs/2603.08096) · [PDF](https://arxiv.org/pdf/2603.08096.pdf)  
**作者**：Bryce Grant, Aryeh Rothenberg, Atri Banerjee, Peng Wang  

**一句话要点**：提出TrianguLang框架，通过几何感知语义共识实现无姿态估计的3D定位，以解决文本引导定位中精度与效率的权衡问题。

**关键词**：3D定位, 文本引导分割, 几何感知注意力, 前馈推理, 无姿态估计, 跨视图对应

## 3 点简述
- 核心问题：现有方法在3D定位中面临每场景优化的精度与几何一致性，与前馈推理效率之间的权衡，且依赖相机标定。
- 方法要点：引入几何感知语义注意力（GASA），利用预测几何门控跨视图特征对应，抑制语义合理但几何不一致的匹配，无需真实姿态。
- 实验或效果：在ScanNet++等五个基准测试中实现最先进的前馈文本引导分割与定位，处理速度约18 FPS，减少用户交互至单文本查询。

## 摘要（原文）

> Localizing objects and parts from natural language in 3D space is essential for robotics, AR, and embodied AI, yet existing methods face a trade-off between the accuracy and geometric consistency of per-scene optimization and the efficiency of feed-forward inference. We present TrianguLang, a feed-forward framework for 3D localization that requires no camera calibration at inference. Unlike prior methods that treat views independently, we introduce Geometry-Aware Semantic Attention (GASA), which utilizes predicted geometry to gate cross-view feature correspondence, suppressing semantically plausible but geometrically inconsistent matches without requiring ground-truth poses. Validated on five benchmarks including ScanNet++ and uCO3D, TrianguLang achieves state-of-the-art feed-forward text-guided segmentation and localization, reducing user effort from $O(N)$ clicks to a single text query. The model processes each frame at 1008x1008 resolution in $\sim$57ms ($\sim$18 FPS) without optimization, enabling practical deployment for interactive robotics and AR applications. Code and checkpoints are available at https://cwru-aism.github.io/triangulang/.

