---
layout: default
title: DropoutTS: Sample-Adaptive Dropout for Robust Time Series Forecasting
---

# DropoutTS: Sample-Adaptive Dropout for Robust Time Series Forecasting
**arXiv**：[2601.21726v1](https://arxiv.org/abs/2601.21726) · [PDF](https://arxiv.org/pdf/2601.21726.pdf)  
**作者**：Siru Zhong, Yiqiu Liu, Zhiqing Cui, Zezhi Shao, Fei Wang, Qingsong Wen, Yuxuan Liang  

**一句话要点**：提出DropoutTS插件，通过样本自适应Dropout提升时间序列预测的鲁棒性。

**关键词**：时间序列预测, 鲁棒性增强, 自适应Dropout, 噪声处理, 模型无关插件

## 3 点简述
- 核心问题：深度时间序列模型易受现实噪声影响，现有方法难以平衡效果与效率。
- 方法要点：利用谱稀疏性量化噪声，动态映射为自适应Dropout率，抑制虚假波动。
- 实验或效果：在多种噪声场景和基准测试中，显著提升骨干模型性能，参数开销可忽略。

## 摘要（原文）

> Deep time series models are vulnerable to noisy data ubiquitous in real-world applications. Existing robustness strategies either prune data or rely on costly prior quantification, failing to balance effectiveness and efficiency. In this paper, we introduce DropoutTS, a model-agnostic plugin that shifts the paradigm from "what" to learn to "how much" to learn. DropoutTS employs a Sample-Adaptive Dropout mechanism: leveraging spectral sparsity to efficiently quantify instance-level noise via reconstruction residuals, it dynamically calibrates model learning capacity by mapping noise to adaptive dropout rates - selectively suppressing spurious fluctuations while preserving fine-grained fidelity. Extensive experiments across diverse noise regimes and open benchmarks show DropoutTS consistently boosts superior backbones' performance, delivering advanced robustness with negligible parameter overhead and no architectural modifications. Our code is available at https://github.com/CityMind-Lab/DropoutTS.

