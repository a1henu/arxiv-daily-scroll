---
layout: default
title: A Differentiable Adversarial Framework for Task-Aware Data Subsampling
---

# A Differentiable Adversarial Framework for Task-Aware Data Subsampling
**arXiv**：[2601.02081v1](https://arxiv.org/abs/2601.02081) · [PDF](https://arxiv.org/pdf/2601.02081.pdf)  
**作者**：Jiacheng Lyu, Bihua Bao  

**一句话要点**：提出对抗性软选择子采样框架，以解决大规模数据集训练中的任务感知数据缩减问题。

**关键词**：数据子采样, 对抗学习, 任务感知学习, 信息瓶颈, Gumbel-Softmax, 大规模数据训练

## 3 点简述
- 传统数据子采样为静态预处理，可能丢弃关键信息，导致下游预测性能下降。
- ASSS框架通过选择器网络与任务网络的对抗游戏，学习连续样本重要性权重，实现端到端优化。
- 在四个大规模真实数据集上，ASSS优于启发式基线，有时甚至超越全数据集训练，展示智能去噪效果。

## 摘要（原文）

> The proliferation of large-scale datasets poses a major computational challenge to model training. The traditional data subsampling method works as a static, task independent preprocessing step which usually discards information that is critical to downstream prediction. In this paper, we introduces the antagonistic soft selection subsampling (ASSS) framework as is a novel paradigm that reconstructs data reduction into a differentiable end-to-end learning problem. ASSS uses the adversarial game between selector network and task network, and selector network learning assigns continuous importance weights to samples. This direct optimization implemented by Gumbel-Softmax relaxation allows the selector to identify and retain samples with the maximum amount of information for a specific task target under the guidance of the loss function that balances the fidelity and sparsity of the prediction. Theoretical analysis links this framework with the information bottleneck principle. Comprehensive experiments on four large-scale real world datasets show that ASSS has always been better than heuristic subsampling baselines such as clustering and nearest neighbor thinning in maintaining model performance. It is worth noting that ASSS can not only match, but also sometimes exceed the training performance of the entire dataset, showcasing the effect of intelligent denoising. This work establishes task aware data subsampling as a learnable component, providing a principled solution for effective large-scale data learning.

