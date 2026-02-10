---
layout: default
title: StretchTime: Adaptive Time Series Forecasting via Symplectic Attention
---

# StretchTime: Adaptive Time Series Forecasting via Symplectic Attention
**arXiv**：[2602.08983v1](https://arxiv.org/abs/2602.08983) · [PDF](https://arxiv.org/pdf/2602.08983.pdf)  
**作者**：Yubin Kim, Viresh Pati, Jevon Twitty, Vinh Pham, Shihao Yang, Jiecheng Lu  

**一句话要点**：提出StretchTime架构，通过辛位置嵌入解决时间序列预测中的非仿射时间扭曲问题。

**关键词**：时间序列预测, Transformer架构, 辛位置嵌入, 自适应时间扭曲, 非平稳动态, 多变量预测

## 3 点简述
- 核心问题：Transformer在时间序列预测中依赖均匀位置编码，无法处理现实世界中的非仿射时间扭曲动态。
- 方法要点：引入基于哈密顿力学的辛位置嵌入，扩展旋转群至辛群，通过自适应扭曲模块实现端到端时间坐标调整。
- 实验或效果：在标准基准测试中实现最先进性能，对非平稳时间动态数据集表现出优越鲁棒性。

## 摘要（原文）

> Transformer architectures have established strong baselines in time series forecasting, yet they typically rely on positional encodings that assume uniform, index-based temporal progression. However, real-world systems, from shifting financial cycles to elastic biological rhythms, frequently exhibit "time-warped" dynamics where the effective flow of time decouples from the sampling index. In this work, we first formalize this misalignment and prove that rotary position embedding (RoPE) is mathematically incapable of representing non-affine temporal warping. To address this, we propose Symplectic Positional Embeddings (SyPE), a learnable encoding framework derived from Hamiltonian mechanics. SyPE strictly generalizes RoPE by extending the rotation group $\mathrm{SO}(2)$ to the symplectic group $\mathrm{Sp}(2,\mathbb{R})$, modulated by a novel input-dependent adaptive warp module. By allowing the attention mechanism to adaptively dilate or contract temporal coordinates end-to-end, our approach captures locally varying periodicities without requiring pre-defined warping functions. We implement this mechanism in StretchTime, a multivariate forecasting architecture that achieves state-of-the-art performance on standard benchmarks, demonstrating superior robustness on datasets exhibiting non-stationary temporal dynamics.

