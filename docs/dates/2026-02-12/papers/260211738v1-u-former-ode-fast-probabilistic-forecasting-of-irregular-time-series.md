---
layout: default
title: U-Former ODE: Fast Probabilistic Forecasting of Irregular Time Series
---

# U-Former ODE: Fast Probabilistic Forecasting of Irregular Time Series
**arXiv**：[2602.11738v1](https://arxiv.org/abs/2602.11738) · [PDF](https://arxiv.org/pdf/2602.11738.pdf)  
**作者**：Ilya Kuleshov, Alexander Marusov, Alexey Zaytsev  

**一句话要点**：提出UFO架构以解决不规则时间序列概率预测中的计算效率与全局建模难题

**关键词**：不规则时间序列, 概率预测, 神经控制微分方程, U-Net, Transformer, 并行计算

## 3 点简述
- 核心问题：不规则时间序列概率预测在医疗和金融领域至关重要，但现有Neural CDE方法计算慢且缺乏全局上下文。
- 方法要点：结合U-Net并行多尺度特征提取、Transformer全局建模和Neural CDE连续时间动力学，构建全因果并行模型。
- 实验或效果：在五个基准测试中优于十个先进基线，推理速度比传统Neural CDE快达15倍，对长序列和多变量序列表现稳定。

## 摘要（原文）

> Probabilistic forecasting of irregularly sampled time series is crucial in domains such as healthcare and finance, yet it remains a formidable challenge. Existing Neural Controlled Differential Equation (Neural CDE) approaches, while effective at modelling continuous dynamics, suffer from slow, inherently sequential computation, which restricts scalability and limits access to global context. We introduce UFO (U-Former ODE), a novel architecture that seamlessly integrates the parallelizable, multiscale feature extraction of U-Nets, the powerful global modelling of Transformers, and the continuous-time dynamics of Neural CDEs. By constructing a fully causal, parallelizable model, UFO achieves a global receptive field while retaining strong sensitivity to local temporal dynamics. Extensive experiments on five standard benchmarks -- covering both regularly and irregularly sampled time series -- demonstrate that UFO consistently outperforms ten state-of-the-art neural baselines in predictive accuracy. Moreover, UFO delivers up to 15$\times$ faster inference compared to conventional Neural CDEs, with consistently strong performance on long and highly multivariate sequences.

