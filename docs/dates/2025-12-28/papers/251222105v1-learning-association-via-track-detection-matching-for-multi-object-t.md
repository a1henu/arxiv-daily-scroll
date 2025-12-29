---
layout: default
title: Learning Association via Track-Detection Matching for Multi-Object Tracking
---

# Learning Association via Track-Detection Matching for Multi-Object Tracking
**arXiv**：[2512.22105v1](https://arxiv.org/abs/2512.22105) · [PDF](https://arxiv.org/pdf/2512.22105.pdf)  
**作者**：Momir Adžemović  

**一句话要点**：提出Track-Detection Link Prediction方法，通过轨迹-检测链接预测实现多目标跟踪，提升关联性能。

**关键词**：多目标跟踪, 轨迹-检测关联, 链接预测, 几何特征, 数据驱动学习, 计算效率

## 3 点简述
- 多目标跟踪需跨帧关联检测以维持身份，现有方法依赖手工启发式或计算复杂端到端学习。
- TDLP基于轨迹-检测链接预测进行逐帧关联，学习数据驱动关联，保持模块化和计算效率。
- 实验表明TDLP在多个基准上超越先进方法，链接预测优于度量学习，尤其处理异构特征。

## 摘要（原文）

> Multi-object tracking aims to maintain object identities over time by associating detections across video frames. Two dominant paradigms exist in literature: tracking-by-detection methods, which are computationally efficient but rely on handcrafted association heuristics, and end-to-end approaches, which learn association from data at the cost of higher computational complexity. We propose Track-Detection Link Prediction (TDLP), a tracking-by-detection method that performs per-frame association via link prediction between tracks and detections, i.e., by predicting the correct continuation of each track at every frame. TDLP is architecturally designed primarily for geometric features such as bounding boxes, while optionally incorporating additional cues, including pose and appearance. Unlike heuristic-based methods, TDLP learns association directly from data without handcrafted rules, while remaining modular and computationally efficient compared to end-to-end trackers. Extensive experiments on multiple benchmarks demonstrate that TDLP consistently surpasses state-of-the-art performance across both tracking-by-detection and end-to-end methods. Finally, we provide a detailed analysis comparing link prediction with metric learning-based association and show that link prediction is more effective, particularly when handling heterogeneous features such as detection bounding boxes. Our code is available at \href{https://github.com/Robotmurlock/TDLP}{https://github.com/Robotmurlock/TDLP}.

