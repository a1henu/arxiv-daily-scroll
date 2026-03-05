---
layout: default
title: TAP: A Token-Adaptive Predictor Framework for Training-Free Diffusion Acceleration
---

# TAP: A Token-Adaptive Predictor Framework for Training-Free Diffusion Acceleration
**arXiv**：[2603.03792v1](https://arxiv.org/abs/2603.03792) · [PDF](https://arxiv.org/pdf/2603.03792.pdf)  
**作者**：Haowei Zhu, Tingxuan Huang, Xing Wang, Tianyu Zhao, Jiexi Wang, Weifeng Chen, Xurui Peng, Fangmin Chen, Junhai Yong, Bin Wang  

**一句话要点**：提出TAP框架以解决扩散模型推理慢的问题，通过自适应选择预测器加速生成过程。

**关键词**：扩散模型加速, 训练免费框架, 自适应预测器, 推理优化, 生成任务

## 3 点简述
- 扩散模型推理慢，需多次全模型去噪步骤。
- TAP使用低开销探针为每个token自适应选择预测器，无需额外训练。
- 实验显示TAP在多种架构中显著提升速度，感知质量损失小。

## 摘要（原文）

> Diffusion models achieve strong generative performance but remain slow at inference due to the need for repeated full-model denoising passes. We present Token-Adaptive Predictor (TAP), a training-free, probe-driven framework that adaptively selects a predictor for each token at every sampling step. TAP uses a single full evaluation of the model's first layer as a low-cost probe to compute proxy losses for a compact family of candidate predictors (instantiated primarily with Taylor expansions of varying order and horizon), then assigns each token the predictor with the smallest proxy error. This per-token "probe-then-select" strategy exploits heterogeneous temporal dynamics, requires no additional training, and is compatible with various predictor designs. TAP incurs negligible overhead while enabling large speedups with little or no perceptual quality loss. Extensive experiments across multiple diffusion architectures and generation tasks show that TAP substantially improves the accuracy-efficiency frontier compared to fixed global predictors and caching-only baselines.

