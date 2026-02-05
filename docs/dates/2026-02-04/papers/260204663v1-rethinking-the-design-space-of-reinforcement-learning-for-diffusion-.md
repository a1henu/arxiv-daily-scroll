---
layout: default
title: Rethinking the Design Space of Reinforcement Learning for Diffusion Models: On the Importance of Likelihood Estimation Beyond Loss Design
---

# Rethinking the Design Space of Reinforcement Learning for Diffusion Models: On the Importance of Likelihood Estimation Beyond Loss Design
**arXiv**：[2602.04663v1](https://arxiv.org/abs/2602.04663) · [PDF](https://arxiv.org/pdf/2602.04663.pdf)  
**作者**：Jaemoo Choi, Yuchen Zhu, Wei Guo, Petr Molodyk, Bo Yuan, Jinbin Bai, Yi Xin, Molei Tao, Yongxin Chen  

**一句话要点**：提出基于ELBO的似然估计方法，提升扩散模型强化学习效率与稳定性

**关键词**：扩散模型, 强化学习, 似然估计, 策略梯度, 文本到图像生成, ELBO

## 3 点简述
- 核心问题：扩散模型似然难解，阻碍策略梯度方法直接应用，现有方法缺乏系统分析
- 方法要点：系统分析RL设计空间，强调ELBO似然估计是关键因素，优于损失函数设计
- 实验或效果：在SD 3.5 Medium上验证，GenEval分数提升至0.95，效率优于SOTA方法

## 摘要（原文）

> Reinforcement learning has been widely applied to diffusion and flow models for visual tasks such as text-to-image generation. However, these tasks remain challenging because diffusion models have intractable likelihoods, which creates a barrier for directly applying popular policy-gradient type methods. Existing approaches primarily focus on crafting new objectives built on already heavily engineered LLM objectives, using ad hoc estimators for likelihood, without a thorough investigation into how such estimation affects overall algorithmic performance. In this work, we provide a systematic analysis of the RL design space by disentangling three factors: i) policy-gradient objectives, ii) likelihood estimators, and iii) rollout sampling schemes. We show that adopting an evidence lower bound (ELBO) based model likelihood estimator, computed only from the final generated sample, is the dominant factor enabling effective, efficient, and stable RL optimization, outweighing the impact of the specific policy-gradient loss functional. We validate our findings across multiple reward benchmarks using SD 3.5 Medium, and observe consistent trends across all tasks. Our method improves the GenEval score from 0.24 to 0.95 in 90 GPU hours, which is $4.6\times$ more efficient than FlowGRPO and $2\times$ more efficient than the SOTA method DiffusionNFT without reward hacking.

