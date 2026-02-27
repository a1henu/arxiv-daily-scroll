---
layout: default
title: Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction
---

# Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction
**arXiv**：[2602.23315v1](https://arxiv.org/abs/2602.23315) · [PDF](https://arxiv.org/pdf/2602.23315.pdf)  
**作者**：Sha Hu  

**一句话要点**：提出基于不变变换和重采样的推理方法，以减少认知不确定性并提升AI模型推理准确性。

**关键词**：认知不确定性, 不变变换, 重采样推理, AI模型优化, 推理准确性

## 3 点简述
- 核心问题：AI模型推理中存在认知不确定性，导致即使优化后仍可能产生错误。
- 方法要点：通过输入的不变变换生成多个样本，利用推理错误的独立性进行重采样和聚合输出。
- 实验或效果：该方法有潜力提高推理准确性，并平衡模型大小与性能。

## 摘要（原文）

> An artificial intelligence (AI) model can be viewed as a function that maps inputs to outputs in high-dimensional spaces. Once designed and well trained, the AI model is applied for inference. However, even optimized AI models can produce inference errors due to aleatoric and epistemic uncertainties. Interestingly, we observed that when inferring multiple samples based on invariant transformations of an input, inference errors can show partial independences due to epistemic uncertainty. Leveraging this insight, we propose a "resampling" based inferencing that applies to a trained AI model with multiple transformed versions of an input, and aggregates inference outputs to a more accurate result. This approach has the potential to improve inference accuracy and offers a strategy for balancing model size and performance.

