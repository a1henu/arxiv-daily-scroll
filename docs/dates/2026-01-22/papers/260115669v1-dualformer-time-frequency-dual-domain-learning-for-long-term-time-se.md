---
layout: default
title: Dualformer: Time-Frequency Dual Domain Learning for Long-term Time Series Forecasting
---

# Dualformer: Time-Frequency Dual Domain Learning for Long-term Time Series Forecasting
**arXiv**：[2601.15669v1](https://arxiv.org/abs/2601.15669) · [PDF](https://arxiv.org/pdf/2601.15669.pdf)  
**作者**：Jingjing Bai, Yoshinobu Kawahara  

**一句话要点**：提出Dualformer以解决Transformer在长时序预测中高频信息衰减问题

**关键词**：长时序预测, Transformer模型, 频域学习, 双域框架, 自适应权重

## 3 点简述
- 核心问题：Transformer在长时序预测中因层间频率传播无差异导致高频信息衰减，限制模型性能。
- 方法要点：设计双分支架构，结合时域和频域建模，通过分层频率采样和周期性感知权重机制自适应整合特征。
- 实验或效果：在八个基准数据集上验证了Dualformer的鲁棒性和优越性能，尤其在异构或弱周期性数据上表现突出。

## 摘要（原文）

> Transformer-based models, despite their promise for long-term time series forecasting (LTSF), suffer from an inherent low-pass filtering effect that limits their effectiveness. This issue arises due to undifferentiated propagation of frequency components across layers, causing a progressive attenuation of high-frequency information crucial for capturing fine-grained temporal variations. To address this limitation, we propose Dualformer, a principled dual-domain framework that rethinks frequency modeling from a layer-wise perspective. Dualformer introduces three key components: (1) a dual-branch architecture that concurrently models complementary temporal patterns in both time and frequency domains; (2) a hierarchical frequency sampling module that allocates distinct frequency bands to different layers, preserving high-frequency details in lower layers while modeling low-frequency trends in deeper layers; and (3) a periodicity-aware weighting mechanism that dynamically balances contributions from the dual branches based on the harmonic energy ratio of inputs, supported theoretically by a derived lower bound. This design enables structured frequency modeling and adaptive integration of time-frequency features, effectively preserving high-frequency information and enhancing generalization. Extensive experiments conducted on eight widely used benchmarks demonstrate Dualformer's robustness and superior performance, particularly on heterogeneous or weakly periodic data. Our code is publicly available at https://github.com/Akira-221/Dualformer.

