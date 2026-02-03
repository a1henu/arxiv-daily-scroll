---
layout: default
title: The Multiple Ticket Hypothesis: Random Sparse Subnetworks Suffice for RLVR
---

# The Multiple Ticket Hypothesis: Random Sparse Subnetworks Suffice for RLVR
**arXiv**：[2602.01599v1](https://arxiv.org/abs/2602.01599) · [PDF](https://arxiv.org/pdf/2602.01599.pdf)  
**作者**：Israel Adewuyi, Solomon Okibe, Vladmir Ivanov  

**一句话要点**：提出多票假设，证明在RLVR中随机稀疏子网络可替代全参数微调

**关键词**：稀疏子网络, 强化学习可验证奖励, 参数冗余, 多票假设, 随机掩码训练

## 3 点简述
- 核心问题：探索预训练模型中参数冗余在强化学习可验证奖励（RLVR）中的利用方式
- 方法要点：仅训练随机选择的1%参数，验证稀疏子网络性能
- 实验或效果：在3个模型和2个任务域中，随机稀疏训练匹配或超越全参数微调，不同掩码重叠度极低

## 摘要（原文）

> The Lottery Ticket Hypothesis demonstrated that sparse subnetworks can match full-model performance, suggesting parameter redundancy. Meanwhile, in Reinforcement Learning with Verifiable Rewards (RLVR), recent work has shown that updates concentrate on a sparse subset of parameters, which further lends evidence to this underlying redundancy. We study the simplest possible way to exploit this redundancy: training only a randomly selected subset of parameters at extreme sparsities. Empirically, we find that training just 1\% of parameters matches or exceeds full-parameter RLVR finetuning across 3 models and 2 task domains. Moreover, different random masks show minimal overlap ($\leq 0.005$ Jaccard similarity) and yet all succeed, suggesting pretrained models contain many viable sparse subnetworks rather than one privileged set. We term this the Multiple Ticket Hypothesis. We explain this phenomenon through the implicit per-step KL constraint in RLVR, which restricts updates to a low-dimensional subspace, enabling arbitrary sparse masks to succeed.

