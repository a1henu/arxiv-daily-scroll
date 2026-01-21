---
layout: default
title: EEG-Titans: Long-Horizon Seizure Forecasting via Dual-Branch Attention and Neural Memory
---

# EEG-Titans: Long-Horizon Seizure Forecasting via Dual-Branch Attention and Neural Memory
**arXiv**：[2601.13748v1](https://arxiv.org/abs/2601.13748) · [PDF](https://arxiv.org/pdf/2601.13748.pdf)  
**作者**：Tien-Dat Pham, Xuan-The Tran  

**一句话要点**：提出EEG-Titans，通过双分支注意力和神经记忆机制解决长时程癫痫发作预测中局部与全局信息权衡问题。

**关键词**：癫痫发作预测, 脑电图分析, 长时程建模, 注意力机制, 神经记忆, 双分支架构

## 3 点简述
- 核心问题：癫痫发作预测中，发作前动态可能跨越长时间，而临床相关信号可能细微且短暂，导致模型在捕获局部时空模式和保持长程上下文信息间存在权衡。
- 方法要点：采用双分支架构，结合滑动窗口注意力捕获短期异常，以及循环记忆通路总结缓慢渐进趋势，增强长上下文建模能力。
- 实验或效果：在CHB-MIT头皮EEG数据集上，按时间顺序保留协议评估，EEG-Titans在18名受试者中达到99.46%的平均段级灵敏度，并通过分层上下文策略在高噪声受试者中显著降低误报率。

## 摘要（原文）

> Accurate epileptic seizure prediction from electroencephalography (EEG) remains challenging because pre-ictal dynamics may span long time horizons while clinically relevant signatures can be subtle and transient. Many deep learning models face a persistent trade-off between capturing local spatiotemporal patterns and maintaining informative long-range context when operating on ultralong sequences. We propose EEG-Titans, a dualbranch architecture that incorporates a modern neural memory mechanism for long-context modeling. The model combines sliding-window attention to capture short-term anomalies with a recurrent memory pathway that summarizes slower, progressive trends over time. On the CHB-MIT scalp EEG dataset, evaluated under a chronological holdout protocol, EEG-Titans achieves 99.46% average segment-level sensitivity across 18 subjects. We further analyze safety-first operating points on artifact-prone recordings and show that a hierarchical context strategy extending the receptive field for high-noise subjects can markedly reduce false alarms (down to 0.00 FPR/h in an extreme outlier) without sacrificing sensitivity. These results indicate that memory-augmented long-context modeling can provide robust seizure forecasting under clinically constrained evaluation

