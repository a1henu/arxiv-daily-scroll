---
layout: default
title: Loop Closure using AnyLoc Visual Place Recognition in DPV-SLAM
---

# Loop Closure using AnyLoc Visual Place Recognition in DPV-SLAM
**arXiv**：[2601.02723v1](https://arxiv.org/abs/2601.02723) · [PDF](https://arxiv.org/pdf/2601.02723.pdf)  
**作者**：Wenzheng Zhang, Kazuki Adachi, Yoshitaka Hara, Sousuke Nakamura  

**一句话要点**：提出集成AnyLoc视觉地点识别以提升DPV-SLAM闭环性能的方法

**关键词**：视觉SLAM, 闭环检测, 视觉地点识别, 深度学习特征, 自适应阈值

## 3 点简述
- 核心问题：传统BoVW闭环检测依赖手工特征，在多变视角和光照下鲁棒性不足。
- 方法要点：用基于深度特征的AnyLoc替代BoVW，并引入自适应相似度阈值调整机制。
- 实验或效果：在室内外数据集上验证，闭环准确性和鲁棒性显著优于原DPV-SLAM。

## 摘要（原文）

> Loop closure is crucial for maintaining the accuracy and consistency of visual SLAM. We propose a method to improve loop closure performance in DPV-SLAM. Our approach integrates AnyLoc, a learning-based visual place recognition technique, as a replacement for the classical Bag of Visual Words (BoVW) loop detection method. In contrast to BoVW, which relies on handcrafted features, AnyLoc utilizes deep feature representations, enabling more robust image retrieval across diverse viewpoints and lighting conditions. Furthermore, we propose an adaptive mechanism that dynamically adjusts similarity threshold based on environmental conditions, removing the need for manual tuning. Experiments on both indoor and outdoor datasets demonstrate that our method significantly outperforms the original DPV-SLAM in terms of loop closure accuracy and robustness. The proposed method offers a practical and scalable solution for enhancing loop closure performance in modern SLAM systems.

