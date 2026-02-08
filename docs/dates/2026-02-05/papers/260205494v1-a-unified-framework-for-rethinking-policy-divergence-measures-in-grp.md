---
layout: default
title: A Unified Framework for Rethinking Policy Divergence Measures in GRPO
---

# A Unified Framework for Rethinking Policy Divergence Measures in GRPO
**arXiv**：[2602.05494v1](https://arxiv.org/abs/2602.05494) · [PDF](https://arxiv.org/pdf/2602.05494.pdf)  
**作者**：Qingyuan Wu, Yuhui Wang, Simon Sinong Zhan, Yanning Dai, Shilong Deng, Sarra Habchi, Qi Zhu, Matthias Gallé, Chao Huang  

**一句话要点**：提出统一裁剪框架以系统分析策略差异度量在GRPO中的作用

**关键词**：强化学习, 策略优化, KL散度, 裁剪框架, 数学推理, 训练稳定性

## 3 点简述
- 核心问题：现有RLVR方法如GRPO通过裁剪似然比约束策略差异，缺乏对多种度量的统一分析框架。
- 方法要点：引入统一框架，涵盖似然比和KL散度等策略差异度量，并识别KL3估计器作为关键约束。
- 实验或效果：在数学推理基准上，KL3估计器提升GRPO的训练稳定性和最终性能。

## 摘要（原文）

> Reinforcement Learning with Verified Reward (RLVR) has emerged as a critical paradigm for advancing the reasoning capabilities of Large Language Models (LLMs). Most existing RLVR methods, such as GRPO and its variants, ensure stable updates by constraining policy divergence through clipping likelihood ratios. This paper introduces a unified clipping framework that characterizes existing methods via a general notion of policy divergence, encompassing both likelihood ratios and Kullback-Leibler (KL) divergences and extending to alternative measures. The framework provides a principled foundation for systematically analyzing how different policy divergence measures affect exploration and performance. We further identify the KL3 estimator, a variance-reduced Monte Carlo estimator of the KL divergence, as a key policy divergence constraint. We theoretically demonstrate that the KL3-based constraint is mathematically equivalent to an asymmetric ratio-based clipping that reallocates probability mass toward high-confidence actions, promoting stronger exploration while retaining the simplicity of GRPO-style methods. Empirical results on mathematical reasoning benchmarks demonstrate that incorporating the KL3 estimator into GRPO improves both training stability and final performance, highlighting the importance of principled policy divergence constraints in policy optimization.

