---
layout: default
title: Robust Scene Coordinate Regression via Geometrically-Consistent Global Descriptors
---

# Robust Scene Coordinate Regression via Geometrically-Consistent Global Descriptors
**arXiv**：[2512.17226v1](https://arxiv.org/abs/2512.17226) · [PDF](https://arxiv.org/pdf/2512.17226.pdf)  
**作者**：Son Tung Nguyen, Tobias Fischer, Alejandro Fontan, Michael Milford  

**一句话要点**：提出几何一致全局描述符聚合模块，以提升视觉定位的鲁棒性

**关键词**：视觉定位, 全局描述符, 几何一致性, 对比学习, 鲁棒性, 无监督训练

## 3 点简述
- 现有方法仅依赖几何线索生成全局描述符，导致在噪声几何约束下判别力不足和鲁棒性降低
- 通过聚合模块学习同时符合几何结构和视觉相似性的全局描述符，纠正基于重叠分数的错误关联
- 在挑战性基准测试中实现显著定位性能提升，并保持计算和内存效率

## 摘要（原文）

> Recent learning-based visual localization methods use global descriptors to disambiguate visually similar places, but existing approaches often derive these descriptors from geometric cues alone (e.g., covisibility graphs), limiting their discriminative power and reducing robustness in the presence of noisy geometric constraints. We propose an aggregator module that learns global descriptors consistent with both geometrical structure and visual similarity, ensuring that images are close in descriptor space only when they are visually similar and spatially connected. This corrects erroneous associations caused by unreliable overlap scores. Using a batch-mining strategy based solely on the overlap scores and a modified contrastive loss, our method trains without manual place labels and generalizes across diverse environments. Experiments on challenging benchmarks show substantial localization gains in large-scale environments while preserving computational and memory efficiency. Code is available at \href{https://github.com/sontung/robust\_scr}{github.com/sontung/robust\_scr}.

