---
layout: default
title: Data assimilation and discrepancy modeling with shallow recurrent decoders
---

# Data assimilation and discrepancy modeling with shallow recurrent decoders
**arXiv**：[2512.01170v1](https://arxiv.org/abs/2512.01170) · [PDF](https://arxiv.org/pdf/2512.01170.pdf)  
**作者**：Yuxuan Bao, J. Nathan Kutz  

**一句话要点**：提出DA-SHRED框架以解决复杂物理系统数据同化与模型缺失动态问题

**关键词**：数据同化, 浅层循环解码器, SIM2REAL差距, 潜在空间学习, 缺失动态识别

## 3 点简述
- 核心问题：模拟模型与传感器数据存在SIM2REAL差距，导致全状态重建不准确
- 方法要点：利用浅层循环解码器学习模拟模型的潜在空间，结合传感器数据更新潜在变量
- 实验或效果：在复杂系统中成功缩小SIM2REAL差距并恢复缺失动态，实现鲁棒数据同化

## 摘要（原文）

> The requirements of modern sensing are rapidly evolving, driven by increasing demands for data efficiency, real-time processing, and deployment under limited sensing coverage. Complex physical systems are often characterized through the integration of a limited number of point sensors in combination with scientific computations which approximate the dominant, full-state dynamics. Simulation models, however, inevitably neglect small-scale or hidden processes, are sensitive to perturbations, or oversimplify parameter correlations, leading to reconstructions that often diverge from the reality measured by sensors. This creates a critical need for data assimilation, the process of integrating observational data with predictive simulation models to produce coherent and accurate estimates of the full state of complex physical systems. We propose a machine learning framework for Data Assimilation with a SHallow REcurrent Decoder (DA-SHRED) which bridges the simulation-to-real (SIM2REAL) gap between computational modeling and experimental sensor data. For real-world physics systems modeling high-dimensional spatiotemporal fields, where the full state cannot be directly observed and must be inferred from sparse sensor measurements, we leverage the latent space learned from a reduced simulation model via SHRED, and update these latent variables using real sensor data to accurately reconstruct the full system state. Furthermore, our algorithm incorporates a sparse identification of nonlinear dynamics based regression model in the latent space to identify functionals corresponding to missing dynamics in the simulation model. We demonstrate that DA-SHRED successfully closes the SIM2REAL gap and additionally recovers missing dynamics in highly complex systems, demonstrating that the combination of efficient temporal encoding and physics-informed correction enables robust data assimilation.

