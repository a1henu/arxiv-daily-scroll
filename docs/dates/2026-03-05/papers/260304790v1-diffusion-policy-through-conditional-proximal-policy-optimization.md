---
layout: default
title: Diffusion Policy through Conditional Proximal Policy Optimization
---

# Diffusion Policy through Conditional Proximal Policy Optimization
**arXiv**：[2603.04790v1](https://arxiv.org/abs/2603.04790) · [PDF](https://arxiv.org/pdf/2603.04790.pdf)  
**作者**：Ben Liu, Shunpeng Yang, Hua Chen  

**一句话要点**：提出条件近端策略优化方法，以高效训练扩散策略于在线强化学习场景。

**关键词**：扩散策略, 在线强化学习, 条件近端策略优化, 多模态行为, 熵正则化

## 3 点简述
- 核心问题：扩散策略在在线强化学习中难以计算动作对数似然，导致内存和计算效率低下。
- 方法要点：通过策略迭代与扩散过程对齐，仅需评估简单高斯概率，并自然处理熵正则化。
- 实验或效果：在IsaacLab和MuJoCo Playground基准任务中实现多模态行为与优越性能。

## 摘要（原文）

> Reinforcement learning (RL) has been extensively employed in a wide range of decision-making problems, such as games and robotics. Recently, diffusion policies have shown strong potential in modeling multi-modal behaviors, enabling more diverse and flexible action generation compared to the conventional Gaussian policy. Despite various attempts to combine RL with diffusion, a key challenge is the difficulty of computing action log-likelihood under the diffusion model. This greatly hinders the direct application of diffusion policies in on-policy reinforcement learning. Most existing methods calculate or approximate the log-likelihood through the entire denoising process in the diffusion model, which can be memory- and computationally inefficient. To overcome this challenge, we propose a novel and efficient method to train a diffusion policy in an on-policy setting that requires only evaluating a simple Gaussian probability. This is achieved by aligning the policy iteration with the diffusion process, which is a distinct paradigm compared to previous work. Moreover, our formulation can naturally handle entropy regularization, which is often difficult to incorporate into diffusion policies. Experiments demonstrate that the proposed method produces multimodal policy behaviors and achieves superior performance on a variety of benchmark tasks in both IsaacLab and MuJoCo Playground.

