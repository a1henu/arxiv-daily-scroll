---
layout: default
title: Probability-Entropy Calibration: An Elastic Indicator for Adaptive Fine-tuning
---

# Probability-Entropy Calibration: An Elastic Indicator for Adaptive Fine-tuning
**arXiv**：[2602.01745v1](https://arxiv.org/abs/2602.01745) · [PDF](https://arxiv.org/pdf/2602.01745.pdf)  
**作者**：Wenhao Yu, Shaohang Wei, Jiahong Liu, Yifan Li, Minda Hu, Aiwei Liu, Hao Zhang, Irwin King  

**一句话要点**：提出概率-熵校准信号以优化监督微调中的令牌级重加权

**关键词**：监督微调, 令牌重加权, 概率-熵校准, 数学推理, 代码生成

## 3 点简述
- 核心问题：现有令牌重加权指标单一，忽略概率或熵导致误判关键学习令牌
- 方法要点：引入相对秩指示器，结合概率与熵校准，生成令牌级相对尺度重加权
- 实验或效果：在数学推理基准上一致改进，提升分布外推理和代码生成性能

## 摘要（原文）

> Token-level reweighting is a simple yet effective mechanism for controlling supervised fine-tuning, but common indicators are largely one-dimensional: the ground-truth probability reflects downstream alignment, while token entropy reflects intrinsic uncertainty induced by the pre-training prior. Ignoring entropy can misidentify noisy or easily replaceable tokens as learning-critical, while ignoring probability fails to reflect target-specific alignment. RankTuner introduces a probability--entropy calibration signal, the Relative Rank Indicator, which compares the rank of the ground-truth token with its expected rank under the prediction distribution. The inverse indicator is used as a token-wise Relative Scale to reweight the fine-tuning objective, focusing updates on truly under-learned tokens without over-penalizing intrinsically uncertain positions. Experiments on multiple backbones show consistent improvements on mathematical reasoning benchmarks, transfer gains on out-of-distribution reasoning, and pre code generation performance over probability-only or entropy-only reweighting baselines.

