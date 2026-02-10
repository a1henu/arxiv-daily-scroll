---
layout: default
title: Negative-Aware Diffusion Process for Temporal Knowledge Graph Extrapolation
---

# Negative-Aware Diffusion Process for Temporal Knowledge Graph Extrapolation
**arXiv**：[2602.08815v1](https://arxiv.org/abs/2602.08815) · [PDF](https://arxiv.org/pdf/2602.08815.pdf)  
**作者**：Yanglei Gan, Peng He, Yuxiang Cai, Run Lin, Guanyu Zhou, Qiao Liu  

**一句话要点**：提出负感知扩散模型NADEx，以解决时序知识图谱外推中忽略负上下文和去噪嵌入校准不足的问题。

**关键词**：时序知识图谱推理, 扩散模型, 负感知学习, Transformer去噪器, 余弦对齐正则化

## 3 点简述
- 核心问题：现有扩散模型在时序知识图谱推理中仅依赖正证据，且训练目标以交叉熵排序为主，缺乏对去噪嵌入的校准监督。
- 方法要点：NADEx编码时序关系上下文，通过Transformer去噪器重构查询对象，并引入基于负原型的余弦对齐正则化器以优化决策边界。
- 实验或效果：在四个公开时序知识图谱基准测试中，NADEx实现了最先进的性能表现。

## 摘要（原文）

> Temporal Knowledge Graph (TKG) reasoning seeks to predict future missing facts from historical evidence. While diffusion models (DM) have recently gained attention for their ability to capture complex predictive distributions, two gaps remain: (i) the generative path is conditioned only on positive evidence, overlooking informative negative context, and (ii) training objectives are dominated by cross-entropy ranking, which improves candidate ordering but provides little supervision over the calibration of the denoised embedding. To bridge this gap, we introduce Negative-Aware Diffusion model for TKG Extrapolation (NADEx). Specifically, NADEx encodes subject-centric histories of entities, relations and temporal intervals into sequential embeddings. NADEx perturbs the query object in the forward process and reconstructs it in reverse with a Transformer denoiser conditioned on the temporal-relational context. We further derive a cosine-alignment regularizer derived from batch-wise negative prototypes, which tightens the decision boundary against implausible candidates. Comprehensive experiments on four public TKG benchmarks demonstrate that NADEx delivers state-of-the-art performance.

