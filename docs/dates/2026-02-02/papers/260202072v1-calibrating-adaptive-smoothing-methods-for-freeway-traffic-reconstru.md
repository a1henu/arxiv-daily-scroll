---
layout: default
title: Calibrating Adaptive Smoothing Methods for Freeway Traffic Reconstruction
---

# Calibrating Adaptive Smoothing Methods for Freeway Traffic Reconstruction
**arXiv**：[2602.02072v1](https://arxiv.org/abs/2602.02072) · [PDF](https://arxiv.org/pdf/2602.02072.pdf)  
**作者**：Junyi Ji, Derek Gloudemans, Gergely Zachár, Matthew Nice, William Barbour, Daniel B. Work  

**一句话要点**：提出自适应平滑方法的端到端校准框架，用于高速公路交通状态重建。

**关键词**：交通状态重建, 自适应平滑方法, 参数校准, 核优化, PyTorch实现, 高速公路交通

## 3 点简述
- 核心问题：自适应平滑方法在交通重建中缺乏基于真实数据的参数校准。
- 方法要点：将校准建模为参数化核优化问题，使用PyTorch实现集成深度学习。
- 实验或效果：利用稀疏雷达网络数据评估速度分布和误差，提供基准指标。

## 摘要（原文）

> The adaptive smoothing method (ASM) is a widely used approach for traffic state reconstruction. This article presents a Python implementation of ASM, featuring end-to-end calibration using real-world ground truth data. The calibration is formulated as a parameterized kernel optimization problem. The model is calibrated using data from a full-state observation testbed, with input from a sparse radar sensor network. The implementation is developed in PyTorch, enabling integration with various deep learning methods. We evaluate the results in terms of speed distribution, spatio-temporal error distribution, and spatial error to provide benchmark metrics for the traffic reconstruction problem. We further demonstrate the usability of the calibrated method across multiple freeways. Finally, we discuss the challenges of reproducibility in general traffic model calibration and the limitations of ASM. This article is reproducible and can serve as a benchmark for various freeway operation tasks.

