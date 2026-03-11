---
layout: default
title: Reconstructing Movement from Sparse Samples: Enhanced Spatio-Temporal Matching Strategies for Low-Frequency Data
---

# Reconstructing Movement from Sparse Samples: Enhanced Spatio-Temporal Matching Strategies for Low-Frequency Data
**arXiv**：[2603.09412v1](https://arxiv.org/abs/2603.09412) · [PDF](https://arxiv.org/pdf/2603.09412.pdf)  
**作者**：Ali Yousefian, Arianna Burzacchi, Simone Vantini  

**一句话要点**：提出四种改进策略以增强低采样频率GPS轨迹与路网匹配的算法性能

**关键词**：GPS轨迹匹配, 时空匹配算法, 低采样频率, 路网重建, 行为分析, 性能优化

## 3 点简述
- 核心问题：原始时空匹配算法在密集环境和高采样间隔下存在计算效率和精度限制
- 方法要点：引入动态缓冲区、自适应观测概率、新时间评分函数和行为分析以优化匹配
- 实验或效果：基于米兰真实数据评估，新指标显示性能和路径质量显著提升

## 摘要（原文）

> This paper explores potential improvements to the Spatial-Temporal Matching algorithm for matching the GPS trajectories to road networks. While this algorithm is effective, it presents some limitations in computational efficiency and the accuracy of the results, especially in dense environments with relatively high sampling intervals. To address this, the paper proposes four modifications to the original algorithm: a dynamic buffer, an adaptive observation probability, a redesigned temporal scoring function, and a behavioral analysis to account for the historical mobility patterns. The enhancements are assessed using real-world data from the urban area of Milan, and through newly defined evaluation metrics to be applied in the absence of ground truth. The results of the experiment show significant improvements in performance efficiency and path quality across various metrics.

