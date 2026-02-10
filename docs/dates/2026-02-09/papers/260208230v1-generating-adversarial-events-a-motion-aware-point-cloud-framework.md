---
layout: default
title: Generating Adversarial Events: A Motion-Aware Point Cloud Framework
---

# Generating Adversarial Events: A Motion-Aware Point Cloud Framework
**arXiv**：[2602.08230v1](https://arxiv.org/abs/2602.08230) · [PDF](https://arxiv.org/pdf/2602.08230.pdf)  
**作者**：Hongwei Ren, Youxin Jiang, Qifei Gu, Xiangqian Wu  

**一句话要点**：提出MA-ADV框架，利用点云表示生成对抗事件以攻击事件相机系统。

**关键词**：事件相机, 对抗攻击, 点云表示, 扩散模型, 时空关系, 安全挑战

## 3 点简述
- 核心问题：事件相机系统因事件表示不可微，对抗攻击研究稀缺，威胁安全关键应用。
- 方法要点：基于点云表示，结合扩散平滑扰动，利用时空关系，通过Adam优化和搜索最小化扰动成本。
- 实验或效果：实现100%攻击成功率，扰动成本最小，增强对抗防御的鲁棒性，凸显事件感知系统安全挑战。

## 摘要（原文）

> Event cameras have been widely adopted in safety-critical domains such as autonomous driving, robotics, and human-computer interaction. A pressing challenge arises from the vulnerability of deep neural networks to adversarial examples, which poses a significant threat to the reliability of event-based systems. Nevertheless, research into adversarial attacks on events is scarce. This is primarily due to the non-differentiable nature of mainstream event representations, which hinders the extension of gradient-based attack methods. In this paper, we propose MA-ADV, a novel \textbf{M}otion-\textbf{A}ware \textbf{Adv}ersarial framework. To the best of our knowledge, this is the first work to generate adversarial events by leveraging point cloud representations. MA-ADV accounts for high-frequency noise in events and employs a diffusion-based approach to smooth perturbations, while fully leveraging the spatial and temporal relationships among events. Finally, MA-ADV identifies the minimal-cost perturbation through a combination of sample-wise Adam optimization, iterative refinement, and binary search. Extensive experimental results validate that MA-ADV ensures a 100\% attack success rate with minimal perturbation cost, and also demonstrate enhanced robustness against defenses, underscoring the critical security challenges facing future event-based perception systems.

