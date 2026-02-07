---
layout: default
title: LeakBoost: Perceptual-Loss-Based Membership Inference Attack
---

# LeakBoost: Perceptual-Loss-Based Membership Inference Attack
**arXiv**：[2602.05748v1](https://arxiv.org/abs/2602.05748) · [PDF](https://arxiv.org/pdf/2602.05748.pdf)  
**作者**：Amit Kravchik Taub, Fred M. Grabovski, Guy Amit, Yisroel Mirsky  

**一句话要点**：提出LeakBoost框架，基于感知损失主动探测模型内部表示以增强成员推理攻击效果。

**关键词**：成员推理攻击, 感知损失, 隐私风险评估, 白盒设置, 动态探测, 图像分类

## 3 点简述
- 核心问题：现有成员推理攻击依赖静态指标，未充分利用模型动态行为，隐私风险评估不足。
- 方法要点：通过优化感知损失合成探测图像，放大成员与非成员在表示空间的差异，无需修改现有检测器。
- 实验或效果：在多个数据集和架构上显著提升AUC和低误报率下的真阳性率，改进集中于基于梯度的检测器。

## 摘要（原文）

> Membership inference attacks (MIAs) aim to determine whether a sample was part of a model's training set, posing serious privacy risks for modern machine-learning systems. Existing MIAs primarily rely on static indicators, such as loss or confidence, and do not fully leverage the dynamic behavior of models when actively probed. We propose LeakBoost, a perceptual-loss-based interrogation framework that actively probes a model's internal representations to expose hidden membership signals. Given a candidate input, LeakBoost synthesizes an interrogation image by optimizing a perceptual (activation-space) objective, amplifying representational differences between members and non-members. This image is then analyzed by an off-the-shelf membership detector, without modifying the detector itself. When combined with existing membership inference methods, LeakBoost achieves substantial improvements at low false-positive rates across multiple image classification datasets and diverse neural network architectures. In particular, it raises AUC from near-chance levels (0.53-0.62) to 0.81-0.88, and increases TPR at 1 percent FPR by over an order of magnitude compared to strong baseline attacks. A detailed sensitivity analysis reveals that deeper layers and short, low-learning-rate optimization produce the strongest leakage, and that improvements concentrate in gradient-based detectors. LeakBoost thus offers a modular and computationally efficient way to assess privacy risks in white-box settings, advancing the study of dynamic membership inference.

