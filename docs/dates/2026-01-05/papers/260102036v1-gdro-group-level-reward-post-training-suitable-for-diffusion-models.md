---
layout: default
title: GDRO: Group-level Reward Post-training Suitable for Diffusion Models
---

# GDRO: Group-level Reward Post-training Suitable for Diffusion Models
**arXiv**：[2601.02036v1](https://arxiv.org/abs/2601.02036) · [PDF](https://arxiv.org/pdf/2601.02036.pdf)  
**作者**：Yiyang Wang, Xi Chen, Xiaogang Xu, Yu Liu, Hengshuang Zhao  

**一句话要点**：提出GDRO以解决扩散模型在群体级奖励对齐中的效率、随机性和奖励黑客问题。

**关键词**：扩散模型, 奖励对齐, 离线训练, 群体级奖励, 奖励黑客, 后训练优化

## 3 点简述
- 核心问题：在线强化学习在扩散模型中效率低、依赖随机采样器且易受奖励黑客影响。
- 方法要点：设计GDRO，支持全离线训练，无需ODE-to-SDE近似，结合理论分析确保稳定性。
- 实验或效果：在OCR和GenEval任务中，GDRO有效提升奖励分数，并缓解奖励黑客，展示高效与鲁棒性。

## 摘要（原文）

> Recent advancements adopt online reinforcement learning (RL) from LLMs to text-to-image rectified flow diffusion models for reward alignment. The use of group-level rewards successfully aligns the model with the targeted reward. However, it faces challenges including low efficiency, dependency on stochastic samplers, and reward hacking. The problem is that rectified flow models are fundamentally different from LLMs: 1) For efficiency, online image sampling takes much more time and dominates the time of training. 2) For stochasticity, rectified flow is deterministic once the initial noise is fixed. Aiming at these problems and inspired by the effects of group-level rewards from LLMs, we design Group-level Direct Reward Optimization (GDRO). GDRO is a new post-training paradigm for group-level reward alignment that combines the characteristics of rectified flow models. Through rigorous theoretical analysis, we point out that GDRO supports full offline training that saves the large time cost for image rollout sampling. Also, it is diffusion-sampler-independent, which eliminates the need for the ODE-to-SDE approximation to obtain stochasticity. We also empirically study the reward hacking trap that may mislead the evaluation, and involve this factor in the evaluation using a corrected score that not only considers the original evaluation reward but also the trend of reward hacking. Extensive experiments demonstrate that GDRO effectively and efficiently improves the reward score of the diffusion model through group-wise offline optimization across the OCR and GenEval tasks, while demonstrating strong stability and robustness in mitigating reward hacking.

