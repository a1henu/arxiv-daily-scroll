---
layout: default
title: Robust Subpixel Localization of Diagonal Markers in Large-Scale Navigation via Multi-Layer Screening and Adaptive Matching
---

# Robust Subpixel Localization of Diagonal Markers in Large-Scale Navigation via Multi-Layer Screening and Adaptive Matching
**arXiv**：[2601.08161v1](https://arxiv.org/abs/2601.08161) · [PDF](https://arxiv.org/pdf/2601.08161.pdf)  
**作者**：Jing Tao, Banglei Guan, Yang Shang, Shunkun Liang, Qifeng Yu  

**一句话要点**：提出基于多层筛选与自适应匹配的鲁棒对角标记亚像素定位方法，以解决大规模导航中复杂背景干扰和计算效率问题。

**关键词**：亚像素定位, 对角标记检测, 自适应模板匹配, 大规模导航, 计算效率优化, 鲁棒定位

## 3 点简述
- 核心问题：大规模飞行导航中复杂背景干扰导致定位失败，传统滑动窗口匹配计算效率低。
- 方法要点：采用三层框架，包括多层角点筛选和自适应模板匹配，通过粗到精候选选择减少计算成本。
- 实验或效果：实验证明方法在复杂大规模环境中有效提取和定位对角标记，适用于导航任务视场测量。

## 摘要（原文）

> This paper proposes a robust, high-precision positioning methodology to address localization failures arising from complex background interference in large-scale flight navigation and the computational inefficiency inherent in conventional sliding window matching techniques. The proposed methodology employs a three-tiered framework incorporating multi-layer corner screening and adaptive template matching. Firstly, dimensionality is reduced through illumination equalization and structural information extraction. A coarse-to-fine candidate selection strategy minimizes sliding window computational costs, enabling rapid estimation of the marker's position. Finally, adaptive templates are generated for candidate points, achieving subpixel precision through improved template matching with correlation coefficient extremum fitting. Experimental results demonstrate the method's effectiveness in extracting and localizing diagonal markers in complex, large-scale environments, making it ideal for field-of-view measurement in navigation tasks.

