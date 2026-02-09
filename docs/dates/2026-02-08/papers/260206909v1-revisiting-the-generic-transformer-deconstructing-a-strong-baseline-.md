---
layout: default
title: Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models
---

# Revisiting the Generic Transformer: Deconstructing a Strong Baseline for Time Series Foundation Models
**arXiv**：[2602.06909v1](https://arxiv.org/abs/2602.06909) · [PDF](https://arxiv.org/pdf/2602.06909.pdf)  
**作者**：Yunshi Wen, Wesley M. Gifford, Chandra Reddy, Lam M. Nguyen, Jayant Kalagnanam, Anak Agung Julius  

**一句话要点**：提出标准补丁Transformer作为时间序列基础模型的强基线，实现零样本预测SOTA性能。

**关键词**：时间序列基础模型, 补丁Transformer, 零样本预测, 消融研究, 模型缩放, 开源基准

## 3 点简述
- 核心问题：时间序列基础模型研究中，异构训练设置难以区分架构创新与数据工程的影响。
- 方法要点：采用通用补丁Transformer架构，通过简单训练协议进行综合消融研究，隔离性能关键因素。
- 实验或效果：模型展示出色可扩展性，提供多维度模型缩放实证结果，并开源模型以建立透明基准。

## 摘要（原文）

> The recent surge in Time Series Foundation Models has rapidly advanced the field, yet the heterogeneous training setups across studies make it difficult to attribute improvements to architectural innovations versus data engineering. In this work, we investigate the potential of a standard patch Transformer, demonstrating that this generic architecture achieves state-of-the-art zero-shot forecasting performance using a straightforward training protocol. We conduct a comprehensive ablation study that covers model scaling, data composition, and training techniques to isolate the essential ingredients for high performance. Our findings identify the key drivers of performance, while confirming that the generic architecture itself demonstrates excellent scalability. By strictly controlling these variables, we provide comprehensive empirical results on model scaling across multiple dimensions. We release our open-source model and detailed findings to establish a transparent, reproducible baseline for future research.

