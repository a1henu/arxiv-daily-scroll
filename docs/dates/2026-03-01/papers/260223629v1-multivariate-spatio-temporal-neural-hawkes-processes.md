---
layout: default
title: Multivariate Spatio-Temporal Neural Hawkes Processes
---

# Multivariate Spatio-Temporal Neural Hawkes Processes
**arXiv**：[2602.23629v1](https://arxiv.org/abs/2602.23629) · [PDF](https://arxiv.org/pdf/2602.23629.pdf)  
**作者**：Christopher Chukwuemeka, Hojun You, Mikyoung Jun  

**一句话要点**：提出多变量时空神经霍克斯过程以建模复杂时空动态事件数据

**关键词**：神经霍克斯过程, 时空点过程, 多变量事件建模, 深度学习, 强度函数分析, 恐怖主义数据分析

## 3 点简述
- 核心问题：现有神经霍克斯过程在捕捉时空交互时存在建模缺口，无法有效恢复时空强度结构
- 方法要点：通过学习的时空衰减动态将空间信息整合到潜在状态演化中，无需预定义触发核
- 实验或效果：模拟研究显示模型能恢复时空强度结构，应用于巴基斯坦恐怖主义数据验证了跨事件类型的时空交互捕捉能力

## 摘要（原文）

> We propose a Multivariate Spatio-Temporal Neural Hawkes Process for modeling complex multivariate event data with spatio-temporal dynamics. The proposed model extends continuous-time neural Hawkes processes by integrating spatial information into latent state evolution through learned temporal and spatial decay dynamics, enabling flexible modeling of excitation and inhibition without predefined triggering kernels. By analyzing fitted intensity functions of deep learning-based temporal Hawkes process models, we identify a modeling gap in how fitted intensity behavior is captured beyond likelihood-based performance, which motivates the proposed spatio-temporal approach. Simulation studies show that the proposed method successfully recovers sensible temporal and spatial intensity structure in multivariate spatio-temporal point patterns, while existing temporal neural Hawkes process approach fails to do so. An application to terrorism data from Pakistan further demonstrates the proposed model's ability to capture complex spatio-temporal interaction across multiple event types.

