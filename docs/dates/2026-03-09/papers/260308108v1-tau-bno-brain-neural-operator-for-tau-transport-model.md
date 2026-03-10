---
layout: default
title: Tau-BNO: Brain Neural Operator for Tau Transport Model
---

# Tau-BNO: Brain Neural Operator for Tau Transport Model
**arXiv**：[2603.08108v1](https://arxiv.org/abs/2603.08108) · [PDF](https://arxiv.org/pdf/2603.08108.pdf)  
**作者**：Nuutti Barron, Heng Rao, Urmi Saha, Yu Gu, Zhenghao Liu, Ge Yu, Defu Yang, Ashish Raj, Minghan Chen  

**一句话要点**：提出Tau-BNO脑神经算子框架，以快速近似网络传输模型，解决tau蛋白传播建模中的计算瓶颈。

**关键词**：脑神经算子, tau蛋白传播, 网络传输模型, 深度学习代理, 计算加速, 生物物理建模

## 3 点简述
- 核心问题：网络传输模型因偏微分方程系统复杂，计算负担重，难以进行参数推断和机制发现。
- 方法要点：结合函数算子和查询算子，通过谱核近似各向异性传输，捕获微观反应动力学和网络传输。
- 实验或效果：预测精度高（R²≈0.98），模拟时间从小时缩短至秒，性能优于Transformer和Mamba等模型。

## 摘要（原文）

> Mechanistic modeling provides a biophysically grounded framework for studying the spread of pathological tau protein in tauopathies like Alzheimer's disease. Existing approaches typically model tau propagation as a diffusive process on the brain's structural connectome, reproducing macroscopic patterns but neglecting microscale cellular transport and reaction mechanisms. The Network Transport Model (NTM) was introduced to fill this gap, explaining how region-level progression of tau emerges from microscale biophysical processes. However, the NTM faces a common challenge for complex models defined by large systems of partial differential equations: the inability to perform parameter inference and mechanistic discovery due to high computational burden and slow model simulations. To overcome this barrier, we propose Tau-BNO, a Brain Neural Operator surrogate framework for rapidly approximating NTM dynamics that captures both intra-regional reaction kinetics and inter-regional network transport. Tau-BNO combines a function operator that encodes kinetic parameters with a query operator that preserves initial state information, while approximating anisotropic transport through a spectral kernel that retains directionality. Empirical evaluations demonstrate high predictive accuracy ($R^2\approx$ 0.98) across diverse biophysical regimes and an 89\% performance improvement over state-of-the-art sequence models like Transformers and Mamba, which lack inherent structural priors. By reducing simulation time from hours to seconds, we show that the surrogate model is capable of producing new insights and generating new hypotheses. This framework is readily extensible to a broader class of connectome-based biophysical models, showcasing the transformative value of deep learning surrogates to accelerate analysis of large-scale, computationally intensive dynamical systems.

