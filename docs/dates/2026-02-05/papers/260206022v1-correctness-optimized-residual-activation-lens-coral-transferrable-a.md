---
layout: default
title: Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering
---

# Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering
**arXiv**：[2602.06022v1](https://arxiv.org/abs/2602.06022) · [PDF](https://arxiv.org/pdf/2602.06022.pdf)  
**作者**：Miranda Muqing Miao, Young-Min Cho, Lyle Ungar  

**一句话要点**：提出CORAL方法，通过正则化推理时引导优化正确性，提升大语言模型的准确性和校准性。

**关键词**：推理时引导, 模型校准, 激活探针, 正则化优化, 迁移学习

## 3 点简述
- 大语言模型在指令微调和偏好对齐后存在校准偏差，训练优化成本高。
- CORAL使用权重衰减MLP探针从模型内部激活提取分布式正确性信号，进行正则化推理时引导。
- 在三个7B参数模型上平均提升准确率10%和预期校准误差50%，并迁移至四个基准测试集。

## 摘要（原文）

> Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive. Inference-time steering offers a lightweight alternative, yet most existing methods optimize proxies for correctness rather than correctness itself. We introduce CORAL (Correctness-Optimized Residual Activation Lens), a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes. We evaluate CORAL across three 7B-parameter models and find that it consistently improves accuracy by 10\% and expected calibration error (ECE) by 50\% on average. We additionally demonstrate that these gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14\% accuracy improvements and 49\% ECE improvements. Our results support the hypothesis that distributed information in model internals can be extracted using regularized probes when individual neurons are insufficient. CORAL thus provides a compute-efficient, transferable, and calibration-aware approach to improve MCQA performance during inference.

