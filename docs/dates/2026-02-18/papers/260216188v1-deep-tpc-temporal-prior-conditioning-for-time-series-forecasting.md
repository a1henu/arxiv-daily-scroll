---
layout: default
title: Deep TPC: Temporal-Prior Conditioning for Time Series Forecasting
---

# Deep TPC: Temporal-Prior Conditioning for Time Series Forecasting
**arXiv**：[2602.16188v1](https://arxiv.org/abs/2602.16188) · [PDF](https://arxiv.org/pdf/2602.16188.pdf)  
**作者**：Filippos Bellos, NaveenJohn Premkumar, Yannis Avrithis, Nam H. Nguyen, Jason J. Corso  

**一句话要点**：提出Temporal-Prior Conditioning以提升时间序列预测中的时间推理能力

**关键词**：时间序列预测, 时间先验条件化, 跨注意力机制, 长期预测, LLM应用, 参数效率

## 3 点简述
- 核心问题：现有LLM-for-time series方法时间信息注入浅层，导致时间推理能力受限
- 方法要点：通过多层跨注意力机制，将时间作为首要模态条件化模型，分离时间序列信号与时间信息
- 实验或效果：在多个数据集上实现长期预测的先进性能，优于全微调和浅层条件化策略

## 摘要（原文）

> LLM-for-time series (TS) methods typically treat time shallowly, injecting positional or prompt-based cues once at the input of a largely frozen decoder, which limits temporal reasoning as this information degrades through the layers. We introduce Temporal-Prior Conditioning (TPC), which elevates time to a first-class modality that conditions the model at multiple depths. TPC attaches a small set of learnable time series tokens to the patch stream; at selected layers these tokens cross-attend to temporal embeddings derived from compact, human-readable temporal descriptors encoded by the same frozen LLM, then feed temporal context back via self-attention. This disentangles time series signal and temporal information while maintaining a low parameter budget. We show that by training only the cross-attention modules and explicitly disentangling time series signal and temporal information, TPC consistently outperforms both full fine-tuning and shallow conditioning strategies, achieving state-of-the-art performance in long-term forecasting across diverse datasets. Code available at: https://github.com/fil-mp/Deep_tpc

