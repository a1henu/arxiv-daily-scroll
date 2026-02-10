---
layout: default
title: Thegra: Graph-based SLAM for Thermal Imagery
---

# Thegra: Graph-based SLAM for Thermal Imagery
**arXiv**：[2602.08531v1](https://arxiv.org/abs/2602.08531) · [PDF](https://arxiv.org/pdf/2602.08531.pdf)  
**作者**：Anastasiia Kornilova, Ivan Moskalenko, Arabella Gromova, Gonzalo Ferrer, Alexander Menshchikov  

**一句话要点**：提出基于图的稀疏单目SLAM系统，用于热成像在视觉退化环境中的定位与建图。

**关键词**：热成像SLAM, 图优化, 跨域特征学习, 稀疏特征匹配, 置信度加权因子图

## 3 点简述
- 热成像在低光照、烟雾等环境中实用，但图像纹理低、对比度差，特征提取困难。
- 采用SuperPoint检测器和LightGlue匹配器，通过预处理和置信度加权因子图适应热数据。
- 在公开热数据集上验证，无需特定训练或微调，实现可靠性能，代码将开源。

## 摘要（原文）

> Thermal imaging provides a practical sensing modality for visual SLAM in visually degraded environments such as low illumination, smoke, or adverse weather. However, thermal imagery often exhibits low texture, low contrast, and high noise, complicating feature-based SLAM. In this work, we propose a sparse monocular graph-based SLAM system for thermal imagery that leverages general-purpose learned features -- the SuperPoint detector and LightGlue matcher, trained on large-scale visible-spectrum data to improve cross-domain generalization. To adapt these components to thermal data, we introduce a preprocessing pipeline to enhance input suitability and modify core SLAM modules to handle sparse and outlier-prone feature matches. We further incorporate keypoint confidence scores from SuperPoint into a confidence-weighted factor graph to improve estimation robustness. Evaluations on public thermal datasets demonstrate that the proposed system achieves reliable performance without requiring dataset-specific training or fine-tuning a desired feature detector, given the scarcity of quality thermal data. Code will be made available upon publication.

