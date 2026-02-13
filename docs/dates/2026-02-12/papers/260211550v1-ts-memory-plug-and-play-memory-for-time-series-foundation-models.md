---
layout: default
title: TS-Memory: Plug-and-Play Memory for Time Series Foundation Models
---

# TS-Memory: Plug-and-Play Memory for Time Series Foundation Models
**arXiv**：[2602.11550v1](https://arxiv.org/abs/2602.11550) · [PDF](https://arxiv.org/pdf/2602.11550.pdf)  
**作者**：Sisuo Lyu, Siru Zhong, Tiegang Chen, Weilin Ruan, Qingxiang Liu, Taiqiang Lv, Qingsong Wen, Raymond Chi-Wing Wong, Yuxuan Liang  

**一句话要点**：提出TS-Memory轻量记忆适配器，以解决时间序列基础模型在分布偏移下适应下游任务的挑战。

**关键词**：时间序列基础模型, 参数化记忆蒸馏, 轻量适配器, 零样本预测, 分布偏移适应, 检索效率优化

## 3 点简述
- 核心问题：时间序列基础模型零样本预测强，但分布偏移下适应下游任务面临灾难性遗忘或高延迟检索的权衡。
- 方法要点：通过参数化记忆蒸馏，构建离线kNN教师合成置信感知分位数目标，蒸馏到轻量适配器，实现无检索部署。
- 实验或效果：在多种模型和基准上，点预测和概率预测均优于代表性适应方法，效率接近冻结主干。

## 摘要（原文）

> Time Series Foundation Models (TSFMs) achieve strong zero-shot forecasting through large-scale pre-training, but adapting them to downstream domains under distribution shift remains challenging. Existing solutions face a trade-off: Parametric Adaptation can cause catastrophic forgetting and requires costly multi-domain maintenance, while Non-Parametric Retrieval improves forecasts but incurs high inference latency due to datastore search. We propose Parametric Memory Distillation and implement it as TS-Memory, a lightweight memory adapter that augments frozen TSFMs. TS-Memory is trained in two stages. First, we construct an offline, leakage-safe kNN teacher that synthesizes confidence-aware quantile targets from retrieved futures. Second, we distill this retrieval-induced distributional correction into a lightweight memory adapter via confidence-gated supervision. During inference, TS-Memory fuses memory and backbone predictions with constant-time overhead, enabling retrieval-free deployment. Experiments across diverse TSFMs and benchmarks demonstrate consistent improvements in both point and probabilistic forecasting over representative adaptation methods, with efficiency comparable to the frozen backbone.

