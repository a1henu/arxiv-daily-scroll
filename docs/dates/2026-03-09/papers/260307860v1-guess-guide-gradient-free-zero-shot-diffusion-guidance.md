---
layout: default
title: Guess & Guide: Gradient-Free Zero-Shot Diffusion Guidance
---

# Guess & Guide: Gradient-Free Zero-Shot Diffusion Guidance
**arXiv**：[2603.07860v1](https://arxiv.org/abs/2603.07860) · [PDF](https://arxiv.org/pdf/2603.07860.pdf)  
**作者**：Abduragim Shtanchaev, Albina Ilina, Yazid Janati, Arip Asadulaev, Martin Takác, Eric Moulines  

**一句话要点**：提出无梯度零样本扩散引导方法，以解决贝叶斯逆问题中计算负担大的问题。

**关键词**：扩散模型, 贝叶斯逆问题, 零样本生成, 无梯度优化, 计算效率

## 3 点简述
- 核心问题：现有方法依赖需计算向量-雅可比积的代理似然，导致去噪步骤计算负担重。
- 方法要点：引入轻量级似然代理，无需通过去噪网络计算梯度，消除反向传播开销。
- 实验或效果：推理成本显著下降，在多项任务中取得最优结果，实现帕累托最优。

## 摘要（原文）

> Pretrained diffusion models serve as effective priors for Bayesian inverse problems. These priors enable zero-shot generation by sampling from the conditional distribution, which avoids the need for task-specific retraining. However, a major limitation of existing methods is their reliance on surrogate likelihoods that require vector-Jacobian products at each denoising step, creating a substantial computational burden. To address this, we introduce a lightweight likelihood surrogate that eliminates the need to calculate gradients through the denoiser network. This enables us to handle diverse inverse problems without backpropagation overhead. Experiments confirm that using our method, the inference cost drops dramatically. At the same time, our approach delivers the highest results in multiple tasks. Broadly speaking, we propose the fastest and Pareto optimal method for Bayesian inverse problems.

