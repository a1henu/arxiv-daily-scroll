---
layout: default
title: Structured Universal Adversarial Attacks on Object Detection for Video Sequences
---

# Structured Universal Adversarial Attacks on Object Detection for Video Sequences
**arXiv**：[2510.14460v1](https://arxiv.org/abs/2510.14460) · [PDF](https://arxiv.org/pdf/2510.14460.pdf)  
**作者**：Sven Jacob, Weijia Shao, Gjergji Kasneci  

**一句话要点**：提出结构化通用对抗攻击，针对视频目标检测实现最小失真扰动。

**关键词**：视频目标检测, 通用对抗攻击, 核范数正则化, 指数梯度优化, 最小失真扰动

## 3 点简述
- 视频目标检测在安全关键应用中易受通用对抗攻击威胁。
- 采用核范数正则化生成背景集中的结构化扰动，并使用自适应指数梯度优化。
- 攻击效果优于低秩投影梯度下降和Frank-Wolfe方法，保持高隐蔽性。

## 摘要（原文）

> Video-based object detection plays a vital role in safety-critical
> applications. While deep learning-based object detectors have achieved
> impressive performance, they remain vulnerable to adversarial attacks,
> particularly those involving universal perturbations. In this work, we propose
> a minimally distorted universal adversarial attack tailored for video object
> detection, which leverages nuclear norm regularization to promote structured
> perturbations concentrated in the background. To optimize this formulation
> efficiently, we employ an adaptive, optimistic exponentiated gradient method
> that enhances both scalability and convergence. Our results demonstrate that
> the proposed attack outperforms both low-rank projected gradient descent and
> Frank-Wolfe based attacks in effectiveness while maintaining high stealthiness.
> All code and data are publicly available at
> https://github.com/jsve96/AO-Exp-Attack.

