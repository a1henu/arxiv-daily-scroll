---
layout: default
title: Difficulty-Estimated Policy Optimization
---

# Difficulty-Estimated Policy Optimization
**arXiv**：[2602.06375v1](https://arxiv.org/abs/2602.06375) · [PDF](https://arxiv.org/pdf/2602.06375.pdf)  
**作者**：Yu Zhao, Fan Jiang, Tianle Liu, Bo Zeng, Yu Liu, Longyue Wang, Weihua Luo  

**一句话要点**：提出难度估计策略优化以解决推理对齐中的梯度衰减与计算效率问题

**关键词**：推理对齐, 策略优化, 难度估计, 计算效率, 梯度衰减

## 3 点简述
- 核心问题：GRPO在问题过于简单或复杂时梯度信号衰减，影响收敛稳定性。
- 方法要点：集成在线难度估计器，动态评估并过滤训练数据，优先高学习潜力样本。
- 实验或效果：实证显示，DEPO在保持模型性能的同时，将rollout成本降低高达2倍。

## 摘要（原文）

> Recent advancements in Large Reasoning Models (LRMs), exemplified by DeepSeek-R1, have underscored the potential of scaling inference-time compute through Group Relative Policy Optimization (GRPO). However, GRPO frequently suffers from gradient signal attenuation when encountering problems that are either too trivial or overly complex. In these scenarios, the disappearance of inter-group advantages makes the gradient signal susceptible to noise, thereby jeopardizing convergence stability. While variants like DAPO attempt to rectify gradient vanishing, they do not alleviate the substantial computational overhead incurred by exhaustive rollouts on low-utility samples. In this paper, we propose Difficulty-Estimated Policy Optimization (DEPO), a novel framework designed to optimize the efficiency and robustness of reasoning alignment. DEPO integrates an online Difficulty Estimator that dynamically assesses and filters training data before the rollout phase. This mechanism ensures that computational resources are prioritized for samples with high learning potential. Empirical results demonstrate that DEPO achieves up to a 2x reduction in rollout costs without compromising model performance. Our approach significantly lowers the computational barrier for training high-performance reasoning models, offering a more sustainable path for reasoning scaling. Code and data will be released upon acceptance.

