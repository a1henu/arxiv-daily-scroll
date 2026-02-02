---
layout: default
title: Securing Time in Energy IoT: A Clock-Dynamics-Aware Spatio-Temporal Graph Attention Network for Clock Drift Attacks and Y2K38 Failures
---

# Securing Time in Energy IoT: A Clock-Dynamics-Aware Spatio-Temporal Graph Attention Network for Clock Drift Attacks and Y2K38 Failures
**arXiv**：[2601.23147v1](https://arxiv.org/abs/2601.23147) · [PDF](https://arxiv.org/pdf/2601.23147.pdf)  
**作者**：Saeid Jamshidi, Omar Abdul Wahab, Rolando Herrero, Foutse Khomh  

**一句话要点**：提出STGAT框架以解决能源物联网中时钟漂移攻击和Y2K38故障的时间安全问题

**关键词**：时空图注意力网络, 时钟漂移攻击, Y2K38故障, 能源物联网安全, 时间异常检测, 图神经网络

## 3 点简述
- 核心问题：能源物联网设备易受时钟漂移、时间同步操纵和Y2K38溢出等时间不一致性威胁，传统模型无法有效检测。
- 方法要点：结合漂移感知时间嵌入、时间自注意力和图注意力，建模时间扭曲和设备间一致性，使用曲率正则化分离正常与异常。
- 实验或效果：在受控时序扰动数据上，STGAT达到95.7%准确率，优于基线模型，并减少26%检测延迟。

## 摘要（原文）

> The integrity of time in distributed Internet of Things (IoT) devices is crucial for reliable operation in energy cyber-physical systems, such as smart grids and microgrids. However, IoT systems are vulnerable to clock drift, time-synchronization manipulation, and timestamp discontinuities, such as the Year 2038 (Y2K38) Unix overflow, all of which disrupt temporal ordering. Conventional anomaly-detection models, which assume reliable timestamps, fail to capture temporal inconsistencies. This paper introduces STGAT (Spatio-Temporal Graph Attention Network), a framework that models both temporal distortion and inter-device consistency in energy IoT systems. STGAT combines drift-aware temporal embeddings and temporal self-attention to capture corrupted time evolution at individual devices, and uses graph attention to model spatial propagation of timing errors. A curvature-regularized latent representation geometrically separates normal clock evolution from anomalies caused by drift, synchronization offsets, and overflow events. Experimental results on energy IoT telemetry with controlled timing perturbations show that STGAT achieves 95.7% accuracy, outperforming recurrent, transformer, and graph-based baselines with significant improvements (d > 1.8, p < 0.001). Additionally, STGAT reduces detection delay by 26%, achieving a 2.3-time-step delay while maintaining stable performance under overflow, drift, and physical inconsistencies.

