---
layout: default
title: DDT: A Dual-Masking Dual-Expert Transformer for Energy Time-Series Forecasting
---

# DDT: A Dual-Masking Dual-Expert Transformer for Energy Time-Series Forecasting
**arXiv**：[2601.07250v1](https://arxiv.org/abs/2601.07250) · [PDF](https://arxiv.org/pdf/2601.07250.pdf)  
**作者**：Mingnan Zhu, Qixuan Zhang, Yixuan Cheng, Fangzhou Gu, Shiming Lin  

**一句话要点**：提出DDT双掩码双专家Transformer，以解决能源时间序列预测中的复杂依赖与数据异质性问题。

**关键词**：时间序列预测, Transformer模型, 能源数据分析, 多源数据融合, 深度学习框架

## 3 点简述
- 核心问题：能源时间序列预测面临复杂时间依赖和多源数据异质性挑战，影响电网稳定与可再生能源整合。
- 方法要点：设计双掩码机制结合因果与动态掩码，并采用双专家系统解耦时间动态与跨变量相关性建模。
- 实验或效果：在7个能源基准数据集上实验，DDT在所有预测范围均优于现有方法，建立了新基准。

## 摘要（原文）

> Accurate energy time-series forecasting is crucial for ensuring grid stability and promoting the integration of renewable energy, yet it faces significant challenges from complex temporal dependencies and the heterogeneity of multi-source data. To address these issues, we propose DDT, a novel and robust deep learning framework for high-precision time-series forecasting. At its core, DDT introduces two key innovations. First, we design a dual-masking mechanism that synergistically combines a strict causal mask with a data-driven dynamic mask. This novel design ensures theoretical causal consistency while adaptively focusing on the most salient historical information, overcoming the rigidity of traditional masking techniques. Second, our architecture features a dual-expert system that decouples the modeling of temporal dynamics and cross-variable correlations into parallel, specialized pathways, which are then intelligently integrated through a dynamic gated fusion module. We conducted extensive experiments on 7 challenging energy benchmark datasets, including ETTh, Electricity, and Solar. The results demonstrate that DDT consistently outperforms strong state-of-the-art baselines across all prediction horizons, establishing a new benchmark for the task.

