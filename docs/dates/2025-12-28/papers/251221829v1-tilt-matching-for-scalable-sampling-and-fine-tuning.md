---
layout: default
title: Tilt Matching for Scalable Sampling and Fine-Tuning
---

# Tilt Matching for Scalable Sampling and Fine-Tuning
**arXiv**：[2512.21829v1](https://arxiv.org/abs/2512.21829) · [PDF](https://arxiv.org/pdf/2512.21829.pdf)  
**作者**：Peter Potaptchik, Cheuk-Kit Lee, Michael S. Albergo  

**一句话要点**：提出Tilt Matching算法，用于可扩展采样和生成模型微调。

**关键词**：随机插值, 流匹配, 生成模型微调, 可扩展采样, 随机最优控制

## 3 点简述
- 核心问题：解决从非归一化密度采样和生成模型微调的可扩展性问题。
- 方法要点：基于随机插值，通过动力学方程关联流匹配速度与奖励倾斜分布，隐式求解随机最优控制问题。
- 实验或效果：在Lennard-Jones势下采样达到先进水平，在Stable Diffusion微调中具有竞争力，无需奖励乘子。

## 摘要（原文）

> We propose a simple, scalable algorithm for using stochastic interpolants to sample from unnormalized densities and for fine-tuning generative models. The approach, Tilt Matching, arises from a dynamical equation relating the flow matching velocity to one targeting the same distribution tilted by a reward, implicitly solving a stochastic optimal control problem. The new velocity inherits the regularity of stochastic interpolant transports while also being the minimizer of an objective with strictly lower variance than flow matching itself. The update to the velocity field can be interpreted as the sum of all joint cumulants of the stochastic interpolant and copies of the reward, and to first order is their covariance. The algorithms do not require any access to gradients of the reward or backpropagating through trajectories of the flow or diffusion. We empirically verify that the approach is efficient and highly scalable, providing state-of-the-art results on sampling under Lennard-Jones potentials and is competitive on fine-tuning Stable Diffusion, without requiring reward multipliers. It can also be straightforwardly applied to tilting few-step flow map models.

