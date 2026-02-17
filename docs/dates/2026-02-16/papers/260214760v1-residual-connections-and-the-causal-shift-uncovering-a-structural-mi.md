---
layout: default
title: Residual Connections and the Causal Shift: Uncovering a Structural Misalignment in Transformers
---

# Residual Connections and the Causal Shift: Uncovering a Structural Misalignment in Transformers
**arXiv**：[2602.14760v1](https://arxiv.org/abs/2602.14760) · [PDF](https://arxiv.org/pdf/2602.14760.pdf)  
**作者**：Jonathan Lys, Vincent Gripon, Bastien Pasdeloup, Lukas Mauch, Fabien Cardinaux, Ghouthi Boukli Hacene  

**一句话要点**：提出残差路径缓解策略以解决Transformer中因果偏移导致的表示错位问题

**关键词**：Transformer架构, 残差连接, 因果偏移, 表示对齐, 轻量级缓解, 自回归模型

## 3 点简述
- 核心问题：自回归Transformer中残差连接与因果掩码导致输入输出表示错位，影响预测准确性
- 方法要点：通过解码轨迹和相似性度量定位错位，提出基于残差衰减的轻量级缓解策略
- 实验或效果：在多个基准测试中验证策略能缓解表示错位并提升性能，提供高效架构增强

## 摘要（原文）

> Large Language Models (LLMs) are trained with next-token prediction, implemented in autoregressive Transformers via causal masking for parallelism. This creates a subtle misalignment: residual connections tie activations to the current token, while supervision targets the next token, potentially propagating mismatched information if the current token is not the most informative for prediction. In this work, we empirically localize this input-output alignment shift in pretrained LLMs, using decoding trajectories over tied embedding spaces and similarity-based metrics. Our experiments reveal that the hidden token representations switch from input alignment to output alignment deep within the network. Motivated by this observation, we propose a lightweight residual-path mitigation based on residual attenuation, implemented either as a fixed-layer intervention or as a learnable gating mechanism. Experiments on multiple benchmarks show that these strategies alleviate the representation misalignment and yield improvements, providing an efficient and general architectural enhancement for autoregressive Transformers.

