---
layout: default
title: On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering
---

# On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering
**arXiv**：[2512.10339v1](https://arxiv.org/abs/2512.10339) · [PDF](https://arxiv.org/pdf/2512.10339.pdf)  
**作者**：Ziseok Lee, Minyeong Hwang, Sanghyun Jo, Wooyeol Lee, Jihyung Ko, Young Bin Park, Jae-Mun Choi, Eunho Yang, Kyungsu Kim  

**一句话要点**：提出自适应路径校正方法以解决异构扩散模型组合中的路径崩溃问题

**关键词**：扩散模型, 推理时引导, 路径崩溃, 分子设计, 自适应校正

## 3 点简述
- 核心问题：异构扩散模型组合时，概率密度路径可能崩溃，导致中间密度不可归一化
- 方法要点：推导路径存在准则预测崩溃，并引入自适应路径校正保证有效概率路径
- 实验或效果：在合成基准和分子设计任务中消除崩溃，提升生成质量和对接指标

## 摘要（原文）

> Inference-time steering enables pretrained diffusion/flow models to be adapted to new tasks without retraining. A widely used approach is the ratio-of-densities method, which defines a time-indexed target path by reweighting probability-density trajectories from multiple models with positive, or in some cases, negative exponents. This construction, however, harbors a critical and previously unformalized failure mode: Marginal Path Collapse, where intermediate densities become non-normalizable even though endpoints remain valid. Collapse arises systematically when composing heterogeneous models trained on different noise schedules or datasets, including a common setting in molecular design where de-novo, conformer, and pocket-conditioned models must be combined for tasks such as flexible-pose scaffold decoration. We provide a novel and complete solution for the problem. First, we derive a simple path existence criterion that predicts exactly when collapse occurs from noise schedules and exponents alone. Second, we introduce Adaptive path Correction with Exponents (ACE), which extends Feynman-Kac steering to time-varying exponents and guarantees a valid probability path. On a synthetic 2D benchmark and on flexible-pose scaffold decoration, ACE eliminates collapse and enables high-guidance compositional generation, improving distributional and docking metrics over constant-exponent baselines and even specialized task-specific scaffold decoration models. Our work turns ratio-of-densities steering with heterogeneous experts from an unstable heuristic into a reliable tool for controllable generation.

