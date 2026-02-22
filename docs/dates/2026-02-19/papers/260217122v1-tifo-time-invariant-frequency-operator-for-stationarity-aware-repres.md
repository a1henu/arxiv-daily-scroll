---
layout: default
title: TIFO: Time-Invariant Frequency Operator for Stationarity-Aware Representation Learning in Time Series
---

# TIFO: Time-Invariant Frequency Operator for Stationarity-Aware Representation Learning in Time Series
**arXiv**：[2602.17122v1](https://arxiv.org/abs/2602.17122) · [PDF](https://arxiv.org/pdf/2602.17122.pdf)  
**作者**：Xihao Piao, Zheng Chen, Lingwei Zhu, Yushun Dong, Yasuko Matsubara, Yasushi Sakurai  

**一句话要点**：提出时间不变频率算子以解决非平稳时间序列预测中的分布偏移问题

**关键词**：时间序列预测, 分布偏移, 频率分析, 平稳性学习, 可扩展模型

## 3 点简述
- 核心问题：非平稳时间序列预测因训练与测试数据分布不同而面临分布偏移，现有方法未能充分捕捉跨样本的时间演化结构
- 方法要点：通过时间不变频率算子学习整个数据集频谱上的平稳感知权重，强调平稳频率成分并抑制非平稳成分，以缓解分布偏移
- 实验或效果：在28个预测设置中取得18个第一和6个第二结果，在ETTm2数据集上平均MSE提升33.3%和55.3%，计算成本降低60%-70%

## 摘要（原文）

> Nonstationary time series forecasting suffers from the distribution shift issue due to the different distributions that produce the training and test data. Existing methods attempt to alleviate the dependence by, e.g., removing low-order moments from each individual sample. These solutions fail to capture the underlying time-evolving structure across samples and do not model the complex time structure. In this paper, we aim to address the distribution shift in the frequency space by considering all possible time structures. To this end, we propose a Time-Invariant Frequency Operator (TIFO), which learns stationarity-aware weights over the frequency spectrum across the entire dataset. The weight representation highlights stationary frequency components while suppressing non-stationary ones, thereby mitigating the distribution shift issue in time series. To justify our method, we show that the Fourier transform of time series data implicitly induces eigen-decomposition in the frequency space. TIFO is a plug-and-play approach that can be seamlessly integrated into various forecasting models. Experiments demonstrate our method achieves 18 top-1 and 6 top-2 results out of 28 forecasting settings. Notably, it yields 33.3% and 55.3% improvements in average MSE on the ETTm2 dataset. In addition, TIFO reduces computational costs by 60% -70% compared to baseline methods, demonstrating strong scalability across diverse forecasting models.

