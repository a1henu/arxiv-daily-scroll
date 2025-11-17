---
layout: default
title: One-to-N Backdoor Attack in 3D Point Cloud via Spherical Trigger
---

# One-to-N Backdoor Attack in 3D Point Cloud via Spherical Trigger
**arXiv**：[2511.11210v1](https://arxiv.org/abs/2511.11210) · [PDF](https://arxiv.org/pdf/2511.11210.pdf)  
**作者**：Dongmei Shan, Wei Lian, Chongxia Wang  

**一句话要点**：提出基于球形触发器的3D点云一对多后门攻击框架，以增强多目标威胁防护。

**关键词**：3D点云, 后门攻击, 球形触发器, 一对多攻击, 深度学习安全

## 3 点简述
- 现有3D点云后门攻击局限于一对一模式，无法应对多目标威胁。
- 利用球形空间属性设计可配置触发器，实现单触发编码多目标类别。
- 实验验证攻击成功率高达100%，且保持干净数据准确性。

## 摘要（原文）

> Backdoor attacks represent a critical threat to deep learning systems, particularly in safety-sensitive 3D domains such as autonomous driving and robotics. However, existing backdoor attacks for 3D point clouds have been limited to a rigid one-to-one paradigm. To address this, we present the first one-to-N backdoor framework for 3D vision, based on a novel, configurable spherical trigger. Our key insight is to leverage the spatial properties of spheres as a parameter space, allowing a single trigger design to encode multiple target classes. We establish a theoretical foundation for one-to-N backdoor attacks in 3D, demonstrating that poisoned models can map distinct trigger configurations to different target labels. Experimental results systematically validate this conclusion across multiple datasets and model architectures, achieving high attack success rates (up to 100\%) while maintaining accuracy on clean data. This work establishes a crucial benchmark for multi-target threats in 3D vision and provides the foundational understanding needed to secure future 3D-driven intelligent systems.

