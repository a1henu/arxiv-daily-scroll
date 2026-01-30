---
layout: default
title: Hebbian Learning with Global Direction
---

# Hebbian Learning with Global Direction
**arXiv**：[2601.21367v1](https://arxiv.org/abs/2601.21367) · [PDF](https://arxiv.org/pdf/2601.21367.pdf)  
**作者**：Wenjia Hua, Kejie Zhao, Luziwei Leng, Ran Cheng, Yuxin Ma, Qinghai Guo  

**一句话要点**：提出全局引导赫布学习框架以解决赫布学习可扩展性问题

**关键词**：赫布学习, 全局引导, 生物可塑性, 模型无关框架, 可扩展性

## 3 点简述
- 赫布学习因依赖局部信息而可扩展性受限
- 框架整合局部赫布更新与全局方向信号
- 在ImageNet等复杂任务上显著缩小与反向传播的差距

## 摘要（原文）

> Backpropagation algorithm has driven the remarkable success of deep neural networks, but its lack of biological plausibility and high computational costs have motivated the ongoing search for alternative training methods. Hebbian learning has attracted considerable interest as a biologically plausible alternative to backpropagation. Nevertheless, its exclusive reliance on local information, without consideration of global task objectives, fundamentally limits its scalability. Inspired by the biological synergy between neuromodulators and local plasticity, we introduce a novel model-agnostic Global-guided Hebbian Learning (GHL) framework, which seamlessly integrates local and global information to scale up across diverse networks and tasks. In specific, the local component employs Oja's rule with competitive learning to ensure stable and effective local updates. Meanwhile, the global component introduces a sign-based signal that guides the direction of local Hebbian plasticity updates. Extensive experiments demonstrate that our method consistently outperforms existing Hebbian approaches. Notably, on large-scale network and complex datasets like ImageNet, our framework achieves the competitive results and significantly narrows the gap with standard backpropagation.

