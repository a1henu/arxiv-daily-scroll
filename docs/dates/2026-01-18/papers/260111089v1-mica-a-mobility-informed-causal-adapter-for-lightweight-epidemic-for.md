---
layout: default
title: MiCA: A Mobility-Informed Causal Adapter for Lightweight Epidemic Forecasting
---

# MiCA: A Mobility-Informed Causal Adapter for Lightweight Epidemic Forecasting
**arXiv**：[2601.11089v1](https://arxiv.org/abs/2601.11089) · [PDF](https://arxiv.org/pdf/2601.11089.pdf)  
**作者**：Suhan Guo, Jiahong Deng, Furao Shen  

**一句话要点**：提出MiCA适配器，通过因果发现整合移动性信息，提升轻量级流行病预测的准确性。

**关键词**：流行病预测, 移动性建模, 因果发现, 轻量级模型, 时空预测

## 3 点简述
- 核心问题：移动性数据噪声大、间接且与疾病记录整合困难，限制预测模型效果。
- 方法要点：使用因果发现推断移动性关系，通过门控残差混合集成到时间预测模型中。
- 实验或效果：在四个真实流行病数据集上，平均相对误差降低7.5%，性能与SOTA模型竞争。

## 摘要（原文）

> Accurate forecasting of infectious disease dynamics is critical for public health planning and intervention. Human mobility plays a central role in shaping the spatial spread of epidemics, but mobility data are noisy, indirect, and difficult to integrate reliably with disease records. Meanwhile, epidemic case time series are typically short and reported at coarse temporal resolution. These conditions limit the effectiveness of parameter-heavy mobility-aware forecasters that rely on clean and abundant data. In this work, we propose the Mobility-Informed Causal Adapter (MiCA), a lightweight and architecture-agnostic module for epidemic forecasting. MiCA infers mobility relations through causal discovery and integrates them into temporal forecasting models via gated residual mixing. This design allows lightweight forecasters to selectively exploit mobility-derived spatial structure while remaining robust under noisy and data-limited conditions, without introducing heavy relational components such as graph neural networks or full attention. Extensive experiments on four real-world epidemic datasets, including COVID-19 incidence, COVID-19 mortality, influenza, and dengue, show that MiCA consistently improves lightweight temporal backbones, achieving an average relative error reduction of 7.5\% across forecasting horizons. Moreover, MiCA attains performance competitive with SOTA spatio-temporal models while remaining lightweight.

