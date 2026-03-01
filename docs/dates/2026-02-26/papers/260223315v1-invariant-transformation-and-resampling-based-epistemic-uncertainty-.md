---
layout: default
title: Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction
---

# Invariant Transformation and Resampling based Epistemic-Uncertainty Reduction
**arXiv**：[2602.23315v1](https://arxiv.org/abs/2602.23315) · [PDF](https://arxiv.org/pdf/2602.23315.pdf)  
**作者**：Sha Hu  

**一句话要点**：提出基于不变变换和重采样的推理方法以减少认知不确定性

**关键词**：认知不确定性, 不变变换, 重采样推理, AI模型优化, 推理精度提升

## 3 点简述
- 核心问题：AI模型推理误差源于随机和认知不确定性，后者可通过变换输入部分独立。
- 方法要点：对输入进行不变变换生成多个样本，聚合推理输出以提高准确性。
- 实验或效果：未知，但该方法有潜力提升推理精度并平衡模型大小与性能。

## 摘要（原文）

> An artificial intelligence (AI) model can be viewed as a function that maps inputs to outputs in high-dimensional spaces. Once designed and well trained, the AI model is applied for inference. However, even optimized AI models can produce inference errors due to aleatoric and epistemic uncertainties. Interestingly, we observed that when inferring multiple samples based on invariant transformations of an input, inference errors can show partial independences due to epistemic uncertainty. Leveraging this insight, we propose a "resampling" based inferencing that applies to a trained AI model with multiple transformed versions of an input, and aggregates inference outputs to a more accurate result. This approach has the potential to improve inference accuracy and offers a strategy for balancing model size and performance.

