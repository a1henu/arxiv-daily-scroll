---
layout: default
title: Diverse Video Generation with Determinantal Point Process-Guided Policy Optimization
---

# Diverse Video Generation with Determinantal Point Process-Guided Policy Optimization
**arXiv**：[2511.20647v1](https://arxiv.org/abs/2511.20647) · [PDF](https://arxiv.org/pdf/2511.20647.pdf)  
**作者**：Tahira Kazimi, Connor Dunlop, Pinar Yanardag  

**一句话要点**：提出DPP-GRPO框架以解决文本到视频生成中的低多样性问题

**关键词**：文本到视频生成, 多样性优化, 策略优化, 行列式点过程, 组相对策略优化

## 3 点简述
- 核心问题：文本到视频扩散模型在单一提示下生成视频多样性不足
- 方法要点：结合行列式点过程和组相对策略优化，将多样性作为显式奖励信号
- 实验或效果：在WAN和CogVideoX上实现多样性提升，并在VBench等基准测试中验证

## 摘要（原文）

> While recent text-to-video (T2V) diffusion models have achieved impressive quality and prompt alignment, they often produce low-diversity outputs when sampling multiple videos from a single text prompt. We tackle this challenge by formulating it as a set-level policy optimization problem, with the goal of training a policy that can cover the diverse range of plausible outcomes for a given prompt. To address this, we introduce DPP-GRPO, a novel framework for diverse video generation that combines Determinantal Point Processes (DPPs) and Group Relative Policy Optimization (GRPO) theories to enforce explicit reward on diverse generations. Our objective turns diversity into an explicit signal by imposing diminishing returns on redundant samples (via DPP) while supplies groupwise feedback over candidate sets (via GRPO). Our framework is plug-and-play and model-agnostic, and encourages diverse generations across visual appearance, camera motions, and scene structure without sacrificing prompt fidelity or perceptual quality. We implement our method on WAN and CogVideoX, and show that our method consistently improves video diversity on state-of-the-art benchmarks such as VBench, VideoScore, and human preference studies. Moreover, we release our code and a new benchmark dataset of 30,000 diverse prompts to support future research.

