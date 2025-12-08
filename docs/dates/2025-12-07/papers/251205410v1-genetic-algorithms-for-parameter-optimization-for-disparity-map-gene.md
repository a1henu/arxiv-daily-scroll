---
layout: default
title: Genetic Algorithms For Parameter Optimization for Disparity Map Generation of Radiata Pine Branch Images
---

# Genetic Algorithms For Parameter Optimization for Disparity Map Generation of Radiata Pine Branch Images
**arXiv**：[2512.05410v1](https://arxiv.org/abs/2512.05410) · [PDF](https://arxiv.org/pdf/2512.05410.pdf)  
**作者**：Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green  

**一句话要点**：提出基于遗传算法的参数优化框架，以提升无人机在辐射松树枝图像视差图生成中的精度与效率。

**关键词**：遗传算法, 立体匹配, 视差图生成, 无人机应用, 参数优化, 图像质量评估

## 3 点简述
- 传统立体匹配算法如SGBM与WLS滤波在无人机应用中需手动调参，影响距离测量精度。
- 采用遗传算法自动搜索SGBM和WLS的最优参数配置，消除人工调参需求。
- 实验显示，相比基线配置，该方法降低均方误差42.86%，提升峰值信噪比和结构相似性8.47%和28.52%。

## 摘要（原文）

> Traditional stereo matching algorithms like Semi-Global Block Matching (SGBM) with Weighted Least Squares (WLS) filtering offer speed advantages over neural networks for UAV applications, generating disparity maps in approximately 0.5 seconds per frame. However, these algorithms require meticulous parameter tuning. We propose a Genetic Algorithm (GA) based parameter optimization framework that systematically searches for optimal parameter configurations for SGBM and WLS, enabling UAVs to measure distances to tree branches with enhanced precision while maintaining processing efficiency. Our contributions include: (1) a novel GA-based parameter optimization framework that eliminates manual tuning; (2) a comprehensive evaluation methodology using multiple image quality metrics; and (3) a practical solution for resource-constrained UAV systems. Experimental results demonstrate that our GA-optimized approach reduces Mean Squared Error by 42.86% while increasing Peak Signal-to-Noise Ratio and Structural Similarity by 8.47% and 28.52%, respectively, compared with baseline configurations. Furthermore, our approach demonstrates superior generalization performance across varied imaging conditions, which is critcal for real-world forestry applications.

