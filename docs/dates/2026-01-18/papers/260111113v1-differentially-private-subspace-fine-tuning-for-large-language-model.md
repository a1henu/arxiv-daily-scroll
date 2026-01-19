---
layout: default
title: Differentially Private Subspace Fine-Tuning for Large Language Models
---

# Differentially Private Subspace Fine-Tuning for Large Language Models
**arXiv**：[2601.11113v1](https://arxiv.org/abs/2601.11113) · [PDF](https://arxiv.org/pdf/2601.11113.pdf)  
**作者**：Lele Zheng, Xiang Wang, Tao Zhang, Yang Cao, Ke Cheng, Yulong Shen  

**一句话要点**：提出DP-SFT方法，通过子空间微调降低噪声幅度，以解决大语言模型差分隐私微调中的性能下降问题。

**关键词**：差分隐私, 大语言模型微调, 子空间优化, 梯度扰动, 隐私保护机器学习

## 3 点简述
- 核心问题：差分隐私微调中高维参数空间注入噪声导致大扰动，降低模型性能并破坏训练稳定性。
- 方法要点：分两阶段识别任务特定低维子空间，仅在该子空间注入噪声，减少对无关参数的干扰。
- 实验或效果：在多个数据集上验证，DP-SFT在严格差分隐私约束下提升准确性、稳定性和收敛速度。

## 摘要（原文）

> Fine-tuning large language models on downstream tasks is crucial for realizing their cross-domain potential but often relies on sensitive data, raising privacy concerns. Differential privacy (DP) offers rigorous privacy guarantees and has been widely adopted in fine-tuning; however, naively injecting noise across the high-dimensional parameter space creates perturbations with large norms, degrading performance and destabilizing training. To address this issue, we propose DP-SFT, a two-stage subspace fine-tuning method that substantially reduces noise magnitude while preserving formal DP guarantees. Our intuition is that, during fine-tuning, significant parameter updates lie within a low-dimensional, task-specific subspace, while other directions change minimally. Hence, we only inject DP noise into this subspace to protect privacy without perturbing irrelevant parameters. In phase one, we identify the subspace by analyzing principal gradient directions to capture task-specific update signals. In phase two, we project full gradients onto this subspace, add DP noise, and map the perturbed gradients back to the original parameter space for model updates, markedly lowering noise impact. Experiments on multiple datasets demonstrate that DP-SFT enhances accuracy and stability under rigorous DP constraints, accelerates convergence, and achieves substantial gains over DP fine-tuning baselines.

