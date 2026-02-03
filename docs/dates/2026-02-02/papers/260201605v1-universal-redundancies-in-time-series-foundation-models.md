---
layout: default
title: Universal Redundancies in Time Series Foundation Models
---

# Universal Redundancies in Time Series Foundation Models
**arXiv**：[2602.01605v1](https://arxiv.org/abs/2602.01605) · [PDF](https://arxiv.org/pdf/2602.01605.pdf)  
**作者**：Anthony Bao, Venkata Hasith Vattikuti, Jeffrey Lai, William Gilpin  

**一句话要点**：揭示时间序列基础模型中的通用冗余，并提出基于稳定秩的头部剪枝方法以解释退化现象。

**关键词**：时间序列基础模型, Transformer冗余, 机制可解释性, 注意力头剪枝, 稳定秩理论, 退化现象分析

## 3 点简述
- 发现基于Transformer的时间序列基础模型在中间层存在冗余组件，模型对整层剪枝具有鲁棒性。
- 提出机制可解释性工具，包括组件剪枝和残差流直接对数归因，用于分析模型行为。
- 基于稳定秩理论框架，识别导致模式重复和季节性偏差等退化现象的具体注意力头。

## 摘要（原文）

> Time Series Foundation Models (TSFMs) leverage extensive pretraining to accurately predict unseen time series during inference, without the need for task-specific fine-tuning. Through large-scale evaluations on standard benchmarks, we find that leading transformer-based TSFMs exhibit redundant components in their intermediate layers. We introduce a set of tools for mechanistic interpretability of TSFMs, including ablations of specific components and direct logit attribution on the residual stream. Our findings are consistent across several leading TSFMs with diverse architectures, and across a diverse set of real-world and synthetic time-series datasets. We discover that all models in our study are robust to ablations of entire layers. Furthermore, we develop a theoretical framework framing transformers as kernel regressors, motivating a purely intrinsic strategy for ablating heads based on the stable rank of the per-head projection matrices. Using this approach, we uncover the specific heads responsible for degenerate phenomena widely observed in TSFMs, such as parroting of motifs from the context and seasonality bias. Our study sheds light on the universal properties of this emerging class of architectures for continuous-time sequence modeling.

