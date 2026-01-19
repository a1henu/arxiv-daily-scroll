---
layout: default
title: FEATHer: Fourier-Efficient Adaptive Temporal Hierarchy Forecaster for Time-Series Forecasting
---

# FEATHer: Fourier-Efficient Adaptive Temporal Hierarchy Forecaster for Time-Series Forecasting
**arXiv**：[2601.11350v1](https://arxiv.org/abs/2601.11350) · [PDF](https://arxiv.org/pdf/2601.11350.pdf)  
**作者**：Jaehoon Lee, Seungwoo Lee, Younghwi Kim, Dohee Kim, Sunghyun Sim  

**一句话要点**：提出FEATHer模型，用于在边缘设备上实现高效准确的长时序预测。

**关键词**：时序预测, 边缘计算, 轻量模型, 频率分解, 工业应用

## 3 点简述
- 核心问题：时序预测需在边缘设备（如PLC）上运行，受限于低延迟和内存，参数需极少。
- 方法要点：采用超轻量多尺度频率分解、共享密集时序核、频率感知门控和稀疏周期核，无循环或注意力机制。
- 实验或效果：在八个基准测试中排名最佳，平均排名2.05，参数少至400个，优于基线模型。

## 摘要（原文）

> Time-series forecasting is fundamental in industrial domains like manufacturing and smart factories. As systems evolve toward automation, models must operate on edge devices (e.g., PLCs, microcontrollers) with strict constraints on latency and memory, limiting parameters to a few thousand. Conventional deep architectures are often impractical here. We propose the Fourier-Efficient Adaptive Temporal Hierarchy Forecaster (FEATHer) for accurate long-term forecasting under severe limits. FEATHer introduces: (i) ultra-lightweight multiscale decomposition into frequency pathways; (ii) a shared Dense Temporal Kernel using projection-depthwise convolution-projection without recurrence or attention; (iii) frequency-aware branch gating that adaptively fuses representations based on spectral characteristics; and (iv) a Sparse Period Kernel reconstructing outputs via period-wise downsampling to capture seasonality. FEATHer maintains a compact architecture (as few as 400 parameters) while outperforming baselines. Across eight benchmarks, it achieves the best ranking, recording 60 first-place results with an average rank of 2.05. These results demonstrate that reliable long-range forecasting is achievable on constrained edge hardware, offering a practical direction for industrial real-time inference.

