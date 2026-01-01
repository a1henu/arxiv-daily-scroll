---
layout: default
title: Projection-based Adversarial Attack using Physics-in-the-Loop Optimization for Monocular Depth Estimation
---

# Projection-based Adversarial Attack using Physics-in-the-Loop Optimization for Monocular Depth Estimation
**arXiv**：[2512.24792v1](https://arxiv.org/abs/2512.24792) · [PDF](https://arxiv.org/pdf/2512.24792.pdf)  
**作者**：Takeru Kusakabe, Yudai Hirose, Mashiho Mukaida, Satoshi Ono  

**一句话要点**：提出基于投影的对抗攻击方法，利用物理在环优化验证单目深度估计模型的脆弱性。

**关键词**：对抗攻击, 单目深度估计, 物理在环优化, 投影扰动, 深度神经网络脆弱性, 进化策略

## 3 点简述
- 核心问题：深度神经网络在单目深度估计中易受对抗攻击，威胁模型可靠性。
- 方法要点：通过投影扰动光到目标物体，结合物理在环优化和分布式协方差矩阵自适应进化策略。
- 实验或效果：成功生成导致深度误估计的对抗样本，使物体部分从场景中消失。

## 摘要（原文）

> Deep neural networks (DNNs) remain vulnerable to adversarial attacks that cause misclassification when specific perturbations are added to input images. This vulnerability also threatens the reliability of DNN-based monocular depth estimation (MDE) models, making robustness enhancement a critical need in practical applications. To validate the vulnerability of DNN-based MDE models, this study proposes a projection-based adversarial attack method that projects perturbation light onto a target object. The proposed method employs physics-in-the-loop (PITL) optimization -- evaluating candidate solutions in actual environments to account for device specifications and disturbances -- and utilizes a distributed covariance matrix adaptation evolution strategy. Experiments confirmed that the proposed method successfully created adversarial examples that lead to depth misestimations, resulting in parts of objects disappearing from the target scene.

