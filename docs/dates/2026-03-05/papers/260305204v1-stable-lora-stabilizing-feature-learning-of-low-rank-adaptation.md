---
layout: default
title: Stable-LoRA: Stabilizing Feature Learning of Low-Rank Adaptation
---

# Stable-LoRA: Stabilizing Feature Learning of Low-Rank Adaptation
**arXiv**：[2603.05204v1](https://arxiv.org/abs/2603.05204) · [PDF](https://arxiv.org/pdf/2603.05204.pdf)  
**作者**：Yize Wu, Ke Gao, Ling Li, Yanjun Wu  

**一句话要点**：提出Stable-LoRA以解决LoRA特征学习不稳定的问题

**关键词**：低秩适应, 特征学习稳定性, 权重收缩优化, 参数高效微调, 大语言模型

## 3 点简述
- LoRA在适当超参数和初始化下可自稳定，但非零初始化A会破坏稳定性
- Stable-LoRA通过早期训练步骤动态收缩A来增强特征学习稳定性
- 实验表明Stable-LoRA在多种模型和任务中优于基线，无额外内存开销

## 摘要（原文）

> Low-Rank Adaptation (LoRA) is a widely adopted parameter-efficient method for fine-tuning Large Langauge Models. It updates the weight matrix as $W=W_0+sBA$, where $W_0$ is the original frozen weight, $s$ is a scaling factor and $A$,$B$ are trainable low-rank matrices. Despite its robust empirical effectiveness, the theoretical foundations of LoRA remain insufficiently understood, particularly with respect to feature learning stability. In this paper, we first establish that, LoRA can, in principle, naturally achieve and sustain stable feature learning (i.e., be self-stabilized) under appropriate hyper-parameters and initializations of $A$ and $B$. However, we also uncover a fundamental limitation that the necessary non-zero initialization of $A$ compromises self-stability, leading to suboptimal performances. To address this challenge, we propose Stable-LoRA, a weight-shrinkage optimization strategy that dynamically enhances stability of LoRA feature learning. By progressively shrinking $A$ during the earliest training steps, Stable-LoRA is both theoretically and empirically validated to effectively eliminate instability of LoRA feature learning while preserving the benefits of the non-zero start. Experiments show that Stable-LoRA consistently outperforms other baselines across diverse models and tasks, with no additional memory usage and only negligible computation overheads. The code is available at https://github.com/Yize-Wu/Stable-LoRA.

