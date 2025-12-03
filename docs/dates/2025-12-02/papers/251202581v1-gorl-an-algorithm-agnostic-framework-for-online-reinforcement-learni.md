---
layout: default
title: GoRL: An Algorithm-Agnostic Framework for Online Reinforcement Learning with Generative Policies
---

# GoRL: An Algorithm-Agnostic Framework for Online Reinforcement Learning with Generative Policies
**arXiv**：[2512.02581v1](https://arxiv.org/abs/2512.02581) · [PDF](https://arxiv.org/pdf/2512.02581.pdf)  
**作者**：Chubin Zhang, Zhenglin Wan, Feng Chen, Xingrui Yu, Ivor Tsang, Bo An  

**一句话要点**：提出GoRL框架，通过解耦优化与生成，解决在线强化学习中生成策略的稳定性问题。

**关键词**：在线强化学习, 生成策略, 稳定性优化, 连续控制, 双时间尺度更新

## 3 点简述
- 核心问题：在线强化学习中，高斯策略表达能力有限，而生成策略（如扩散模型）因似然难处理导致优化不稳定。
- 方法要点：GoRL框架优化易处理的潜在策略，使用条件生成解码器合成动作，通过双时间尺度更新实现稳定学习。
- 实验或效果：在连续控制任务中，GoRL优于高斯策略和生成策略基线，在HopperStand任务上归一化回报超870。

## 摘要（原文）

> Reinforcement learning (RL) faces a persistent tension: policies that are stable to optimize are often too simple to represent the multimodal action distributions needed for complex control. Gaussian policies provide tractable likelihoods and smooth gradients, but their unimodal form limits expressiveness. Conversely, generative policies based on diffusion or flow matching can model rich multimodal behaviors; however, in online RL, they are frequently unstable due to intractable likelihoods and noisy gradients propagating through deep sampling chains. We address this tension with a key structural principle: decoupling optimization from generation. Building on this insight, we introduce GoRL (Generative Online Reinforcement Learning), a framework that optimizes a tractable latent policy while utilizing a conditional generative decoder to synthesize actions. A two-timescale update schedule enables the latent policy to learn stably while the decoder steadily increases expressiveness, without requiring tractable action likelihoods. Across a range of continuous-control tasks, GoRL consistently outperforms both Gaussian policies and recent generative-policy baselines. Notably, on the HopperStand task, it reaches a normalized return above 870, more than 3 times that of the strongest baseline. These results demonstrate that separating optimization from generation provides a practical path to policies that are both stable and highly expressive.

