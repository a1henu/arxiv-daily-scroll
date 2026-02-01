---
layout: default
title: Multi-Modal Time Series Prediction via Mixture of Modulated Experts
---

# Multi-Modal Time Series Prediction via Mixture of Modulated Experts
**arXiv**：[2601.21547v1](https://arxiv.org/abs/2601.21547) · [PDF](https://arxiv.org/pdf/2601.21547.pdf)  
**作者**：Lige Zhang, Ali Maatouk, Jialin Chen, Leandros Tassiulas, Rex Ying  

**一句话要点**：提出专家调制方法，通过文本信号控制专家行为，提升多模态时间序列预测性能。

**关键词**：多模态时间序列预测, 专家调制, 混合专家模型, 跨模态控制, 文本信号融合

## 3 点简述
- 现有方法依赖标记级融合，在数据稀缺和序列特性差异大时跨模态对齐困难。
- 引入专家调制，基于文本信号调节路由和专家计算，实现直接高效的跨模态控制。
- 理论分析和实验验证表明，该方法在多模态时间序列预测中显著改进性能。

## 摘要（原文）

> Real-world time series exhibit complex and evolving dynamics, making accurate forecasting extremely challenging. Recent multi-modal forecasting methods leverage textual information such as news reports to improve prediction, but most rely on token-level fusion that mixes temporal patches with language tokens in a shared embedding space. However, such fusion can be ill-suited when high-quality time-text pairs are scarce and when time series exhibit substantial variation in scale and characteristics, thus complicating cross-modal alignment. In parallel, Mixture-of-Experts (MoE) architectures have proven effective for both time series modeling and multi-modal learning, yet many existing MoE-based modality integration methods still depend on token-level fusion. To address this, we propose Expert Modulation, a new paradigm for multi-modal time series prediction that conditions both routing and expert computation on textual signals, enabling direct and efficient cross-modal control over expert behavior. Through comprehensive theoretical analysis and experiments, our proposed method demonstrates substantial improvements in multi-modal time series prediction. The current code is available at https://github.com/BruceZhangReve/MoME

