---
layout: default
title: Towards Robust Protective Perturbation against DeepFake Face Swapping
---

# Towards Robust Protective Perturbation against DeepFake Face Swapping
**arXiv**：[2512.07228v1](https://arxiv.org/abs/2512.07228) · [PDF](https://arxiv.org/pdf/2512.07228.pdf)  
**作者**：Hengyang Yao, Lin Li, Ke Sun, Jianing Qiu, Huiping Chen  

**一句话要点**：提出EOLT框架以增强DeepFake人脸交换的防护扰动鲁棒性

**关键词**：DeepFake防护, 扰动鲁棒性, 变换分布学习, 强化学习, 人脸交换防御

## 3 点简述
- 核心问题：现有防护扰动易被压缩或调整大小等基本变换破坏，鲁棒性不足。
- 方法要点：引入EOLT，通过策略网络学习变换分布，自适应生成实例特定扰动。
- 实验或效果：在30种变换上平均鲁棒性提升26%，挑战类别增益达30%。

## 摘要（原文）

> DeepFake face swapping enables highly realistic identity forgeries, posing serious privacy and security risks. A common defence embeds invisible perturbations into images, but these are fragile and often destroyed by basic transformations such as compression or resizing. In this paper, we first conduct a systematic analysis of 30 transformations across six categories and show that protection robustness is highly sensitive to the choice of training transformations, making the standard Expectation over Transformation (EOT) with uniform sampling fundamentally suboptimal. Motivated by this, we propose Expectation Over Learned distribution of Transformation (EOLT), the framework to treat transformation distribution as a learnable component rather than a fixed design choice. Specifically, EOLT employs a policy network that learns to automatically prioritize critical transformations and adaptively generate instance-specific perturbations via reinforcement learning, enabling explicit modeling of defensive bottlenecks while maintaining broad transferability. Extensive experiments demonstrate that our method achieves substantial improvements over state-of-the-art approaches, with 26% higher average robustness and up to 30% gains on challenging transformation categories.

