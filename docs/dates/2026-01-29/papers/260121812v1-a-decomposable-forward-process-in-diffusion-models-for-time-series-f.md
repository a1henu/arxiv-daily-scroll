---
layout: default
title: A Decomposable Forward Process in Diffusion Models for Time-Series Forecasting
---

# A Decomposable Forward Process in Diffusion Models for Time-Series Forecasting
**arXiv**：[2601.21812v1](https://arxiv.org/abs/2601.21812) · [PDF](https://arxiv.org/pdf/2601.21812.pdf)  
**作者**：Francisco Caldas, Sahil Kumar, Cláudia Soares  

**一句话要点**：提出可分解前向扩散过程，用于时间序列预测，通过谱分解提升模式保持能力。

**关键词**：时间序列预测, 扩散模型, 谱分解, 前向过程, 模式保持, 噪声注入

## 3 点简述
- 核心问题：标准扩散模型在时间序列预测中难以有效保持结构化时序模式如季节性。
- 方法要点：引入模型无关的前向扩散过程，基于谱分解按能量分阶段注入噪声，保持主导频率高信噪比。
- 实验或效果：在标准基准测试中，应用傅里叶或小波变换策略一致提升预测质量，计算开销可忽略。

## 摘要（原文）

> We introduce a model-agnostic forward diffusion process for time-series forecasting that decomposes signals into spectral components, preserving structured temporal patterns such as seasonality more effectively than standard diffusion. Unlike prior work that modifies the network architecture or diffuses directly in the frequency domain, our proposed method alters only the diffusion process itself, making it compatible with existing diffusion backbones (e.g., DiffWave, TimeGrad, CSDI). By staging noise injection according to component energy, it maintains high signal-to-noise ratios for dominant frequencies throughout the diffusion trajectory, thereby improving the recoverability of long-term patterns. This strategy enables the model to maintain the signal structure for a longer period in the forward process, leading to improved forecast quality. Across standard forecasting benchmarks, we show that applying spectral decomposition strategies, such as the Fourier or Wavelet transform, consistently improves upon diffusion models using the baseline forward process, with negligible computational overhead. The code for this paper is available at https://anonymous.4open.science/r/D-FDP-4A29.

