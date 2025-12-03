---
layout: default
title: Joint Distillation for Fast Likelihood Evaluation and Sampling in Flow-based Models
---

# Joint Distillation for Fast Likelihood Evaluation and Sampling in Flow-based Models
**arXiv**：[2512.02636v1](https://arxiv.org/abs/2512.02636) · [PDF](https://arxiv.org/pdf/2512.02636.pdf)  
**作者**：Xinyue Ai, Yutong He, Albert Gu, Ruslan Salakhutdinov, J Zico Kolter, Nicholas Matthew Boffi, Max Simchowitz  

**一句话要点**：提出F2D2框架，通过联合蒸馏同时加速流模型中的采样和似然评估

**关键词**：流模型, 似然评估, 联合蒸馏, 连续归一化流, 少步采样, 自引导方法

## 3 点简述
- 核心问题：流模型和扩散模型需数百至数千次评估计算似然，现有蒸馏方法牺牲似然可计算性或仍依赖昂贵积分
- 方法要点：基于连续归一化流中采样和似然ODE共享速度场，用单一模型联合蒸馏轨迹和累积散度，模块化且兼容现有少步采样模型
- 实验或效果：F2D2将采样和似然评估所需评估次数减少两个数量级，保持高样本质量，并应用于轻量自引导方法提升性能

## 摘要（原文）

> Log-likelihood evaluation enables important capabilities in generative models, including model comparison, certain fine-tuning objectives, and many downstream applications. Yet paradoxically, some of today's best generative models -- diffusion and flow-based models -- still require hundreds to thousands of neural function evaluations (NFEs) to compute a single likelihood. While recent distillation methods have successfully accelerated sampling to just a few steps, they achieve this at the cost of likelihood tractability: existing approaches either abandon likelihood computation entirely or still require expensive integration over full trajectories. We present fast flow joint distillation (F2D2), a framework that simultaneously reduces the number of NFEs required for both sampling and likelihood evaluation by two orders of magnitude. Our key insight is that in continuous normalizing flows, the coupled ODEs for sampling and likelihood are computed from a shared underlying velocity field, allowing us to jointly distill both the sampling trajectory and cumulative divergence using a single model. F2D2 is modular, compatible with existing flow-based few-step sampling models, and requires only an additional divergence prediction head. Experiments demonstrate F2D2's capability of achieving accurate log-likelihood with few-step evaluations while maintaining high sample quality, solving a long-standing computational bottleneck in flow-based generative models. As an application of our approach, we propose a lightweight self-guidance method that enables a 2-step MeanFlow model to outperform a 1024 step teacher model with only a single additional backward NFE.

