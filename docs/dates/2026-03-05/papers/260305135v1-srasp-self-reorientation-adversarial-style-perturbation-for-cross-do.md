---
layout: default
title: SRasP: Self-Reorientation Adversarial Style Perturbation for Cross-Domain Few-Shot Learning
---

# SRasP: Self-Reorientation Adversarial Style Perturbation for Cross-Domain Few-Shot Learning
**arXiv**：[2603.05135v1](https://arxiv.org/abs/2603.05135) · [PDF](https://arxiv.org/pdf/2603.05135.pdf)  
**作者**：Wenqian Li, Pengfei Fang, Hui Xue  

**一句话要点**：提出SRasP方法以解决跨域少样本学习中风格扰动梯度不稳定和收敛尖锐的问题

**关键词**：跨域少样本学习, 风格扰动, 梯度稳定, 多目标优化, 模型泛化

## 3 点简述
- 核心问题：现有风格扰动方法在跨域少样本学习中存在梯度不稳定和收敛到尖锐最小值的问题
- 方法要点：SRasP利用全局语义指导识别不连贯裁剪，重新定向并聚合裁剪与全局风格梯度，结合多目标优化函数最大化视觉差异并保持语义一致性
- 实验或效果：在多个跨域少样本学习基准测试中，SRasP相比先进方法取得一致改进，提升模型泛化能力

## 摘要（原文）

> Cross-Domain Few-Shot Learning (CD-FSL) aims to transfer knowledge from a seen source domain to unseen target domains, serving as a key benchmark for evaluating the robustness and transferability of models. Existing style-based perturbation methods mitigate domain shift but often suffer from gradient instability and convergence to sharp minima.To address these limitations, we propose a novel crop-global style perturbation network, termed Self-Reorientation Adversarial \underline{S}tyle \underline{P}erturbation (SRasP). Specifically, SRasP leverages global semantic guidance to identify incoherent crops, followed by reorienting and aggregating the style gradients of these crops with the global style gradients within one image. Furthermore, we propose a novel multi-objective optimization function to maximize visual discrepancy while enforcing semantic consistency among global, crop, and adversarial features. Applying the stabilized perturbations during training encourages convergence toward flatter and more transferable solutions, improving generalization to unseen domains. Extensive experiments are conducted on multiple CD-FSL benchmarks, demonstrating consistent improvements over state-of-the-art methods.

