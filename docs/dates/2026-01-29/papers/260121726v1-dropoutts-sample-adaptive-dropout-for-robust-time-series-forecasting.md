---
layout: default
title: DropoutTS: Sample-Adaptive Dropout for Robust Time Series Forecasting
---

# DropoutTS: Sample-Adaptive Dropout for Robust Time Series Forecasting
**arXiv**：[2601.21726v1](https://arxiv.org/abs/2601.21726) · [PDF](https://arxiv.org/pdf/2601.21726.pdf)  
**作者**：Siru Zhong, Yiqiu Liu, Zhiqing Cui, Zezhi Shao, Fei Wang, Qingsong Wen, Yuxuan Liang  

**一句话要点**：提出DropoutTS以解决时间序列预测中噪声数据的鲁棒性问题

**关键词**：时间序列预测, 鲁棒性增强, 自适应Dropout, 噪声量化, 模型无关插件, 谱稀疏性

## 3 点简述
- 核心问题：深度时间序列模型易受现实应用中普遍存在的噪声数据影响，现有方法在效果与效率间难以平衡
- 方法要点：采用样本自适应Dropout机制，通过谱稀疏性量化实例级噪声，动态映射噪声至自适应丢弃率以校准学习能力
- 实验或效果：在多种噪声环境和公开基准测试中，DropoutTS显著提升骨干模型性能，实现高级鲁棒性且参数开销可忽略

## 摘要（原文）

> Deep time series models are vulnerable to noisy data ubiquitous in real-world applications. Existing robustness strategies either prune data or rely on costly prior quantification, failing to balance effectiveness and efficiency. In this paper, we introduce DropoutTS, a model-agnostic plugin that shifts the paradigm from "what" to learn to "how much" to learn. DropoutTS employs a Sample-Adaptive Dropout mechanism: leveraging spectral sparsity to efficiently quantify instance-level noise via reconstruction residuals, it dynamically calibrates model learning capacity by mapping noise to adaptive dropout rates - selectively suppressing spurious fluctuations while preserving fine-grained fidelity. Extensive experiments across diverse noise regimes and open benchmarks show DropoutTS consistently boosts superior backbones' performance, delivering advanced robustness with negligible parameter overhead and no architectural modifications. Our code is available at https://github.com/CityMind-Lab/DropoutTS.

