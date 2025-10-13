---
layout: default
title: Spotlight on Token Perception for Multimodal Reinforcement Learning
---

# Spotlight on Token Perception for Multimodal Reinforcement Learning
**arXiv**：[2510.09285v1](https://arxiv.org/abs/2510.09285) · [PDF](https://arxiv.org/pdf/2510.09285.pdf)  
**作者**：Siyuan Huang, Xiaoye Qu, Yafu Li, Yun Luo, Zefeng He, Daizong Liu, Yu Cheng  
**一句话要点**：提出视觉感知策略优化以增强多模态强化学习中的视觉推理能力
**关键词**：多模态强化学习, 令牌感知, 视觉依赖, 策略优化, 推理基准

## 3 点简述
- 核心问题：多模态强化学习中视觉感知在优化过程中常被忽视，影响推理准确性。
- 方法要点：引入令牌感知度量视觉依赖，通过重加权优势和聚焦关键令牌优化策略。
- 实验或效果：在八个基准测试中显著优于现有模型，适用于7B和32B规模。

## 摘要（原文）

> While Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the
> reasoning capabilities of Large Vision-Language Models (LVLMs), most existing
> methods in multimodal reasoning neglect the critical role of visual perception
> within the RLVR optimization process. In this paper, we undertake a pioneering
> exploration of multimodal RLVR through the novel perspective of token
> perception, which measures the visual dependency of each generated token. With
> a granular analysis of Chain-of-Thought (CoT) processes, we uncover two key
> insights: first, token perception in a rollout trajectory is sparsely
> distributed, where only a small fraction of tokens have high visual dependency
> for visually-grounded reasoning; second, different trajectories exhibit
> significant divergence in their overall visual dependency. Based on these
> observations, we propose Visually-Perceptive Policy Optimization (VPPO), a
> novel policy gradient algorithm that explicitly leverages token perception to
> refine the learning signal. Specifically, VPPO achieves this through a dual
> mechanism: it reweights a trajectory's advantage by its overall visual
> dependency, and focuses policy updates exclusively on perceptually pivotal
> tokens. On a comprehensive suite of eight perception and reasoning benchmarks,
> VPPO demonstrates substantial gains over leading open-source RL-tuned models,
> with its effectiveness consistently validated across 7B and 32B model scales.
> Our findings not only establish a new token-level perceptual perspective for
> analyzing multimodal RLVR but also present a novel and effective optimization
> strategy to significantly enhance the multimodal reasoning capabilities of
> LVLMs.

