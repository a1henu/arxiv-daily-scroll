---
layout: default
title: Action-Guided Attention for Video Action Anticipation
---

# Action-Guided Attention for Video Action Anticipation
**arXiv**：[2603.01743v1](https://arxiv.org/abs/2603.01743) · [PDF](https://arxiv.org/pdf/2603.01743.pdf)  
**作者**：Tsung-Ming Tai, Sofia Casarin, Andrea Pilzer, Werner Nutt, Oswald Lanz  

**一句话要点**：提出动作引导注意力机制，以解决视频动作预测中语义建模不足和过拟合问题。

**关键词**：视频动作预测, 注意力机制, 序列建模, 泛化能力, 可解释性分析

## 3 点简述
- 核心问题：现有基于Transformer的方法依赖像素级注意力，缺乏高级语义建模，易过拟合于过去帧的显式视觉线索，限制意图捕捉和泛化能力。
- 方法要点：引入动作引导注意力，利用预测的动作序列作为查询和键来引导序列建模，通过门控函数结合过去相关时刻与当前帧嵌入。
- 实验或效果：在EPIC-Kitchens-100基准上验证了良好泛化性，并提供后训练分析以增强模型透明度和可解释性。

## 摘要（原文）

> Anticipating future actions in videos is challenging, as the observed frames provide only evidence of past activities, requiring the inference of latent intentions to predict upcoming actions. Existing transformer-based approaches, which rely on dot-product attention over pixel representations, often lack the high-level semantics necessary to model video sequences for effective action anticipation. As a result, these methods tend to overfit to explicit visual cues present in the past frames, limiting their ability to capture underlying intentions and degrading generalization to unseen samples. To address this, we propose Action-Guided Attention (AGA), an attention mechanism that explicitly leverages predicted action sequences as queries and keys to guide sequence modeling. Our approach fosters the attention module to emphasize relevant moments from the past based on the upcoming activity and combine this information with the current frame embedding via a dedicated gating function. The design of AGA enables post-training analysis of the knowledge discovered from the training set. Experiments on the widely adopted EPIC-Kitchens-100 benchmark demonstrate that AGA generalizes well from validation to unseen test sets. Post-training analysis can further examine the action dependencies captured by the model and the counterfactual evidence it has internalized, offering transparent and interpretable insights into its anticipative predictions.

