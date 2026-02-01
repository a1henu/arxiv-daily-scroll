---
layout: default
title: Hebbian Learning with Global Direction
---

# Hebbian Learning with Global Direction
**arXiv**：[2601.21367v1](https://arxiv.org/abs/2601.21367) · [PDF](https://arxiv.org/pdf/2601.21367.pdf)  
**作者**：Wenjia Hua, Kejie Zhao, Luziwei Leng, Ran Cheng, Yuxin Ma, Qinghai Guo  

**一句话要点**：提出全局引导赫布学习框架以解决赫布学习缺乏全局目标指导的可扩展性问题

**关键词**：赫布学习, 全局引导学习, 生物可塑性, 模型无关框架, 反向传播替代

## 3 点简述
- 赫布学习依赖局部信息，缺乏全局任务目标，限制了其在大规模网络和复杂任务中的可扩展性
- 引入模型无关的全局引导赫布学习框架，结合局部赫布更新和全局方向信号，实现局部与全局信息的融合
- 在ImageNet等大规模数据集上实验，性能优于现有赫布方法，显著缩小与反向传播的差距

## 摘要（原文）

> Backpropagation algorithm has driven the remarkable success of deep neural networks, but its lack of biological plausibility and high computational costs have motivated the ongoing search for alternative training methods. Hebbian learning has attracted considerable interest as a biologically plausible alternative to backpropagation. Nevertheless, its exclusive reliance on local information, without consideration of global task objectives, fundamentally limits its scalability. Inspired by the biological synergy between neuromodulators and local plasticity, we introduce a novel model-agnostic Global-guided Hebbian Learning (GHL) framework, which seamlessly integrates local and global information to scale up across diverse networks and tasks. In specific, the local component employs Oja's rule with competitive learning to ensure stable and effective local updates. Meanwhile, the global component introduces a sign-based signal that guides the direction of local Hebbian plasticity updates. Extensive experiments demonstrate that our method consistently outperforms existing Hebbian approaches. Notably, on large-scale network and complex datasets like ImageNet, our framework achieves the competitive results and significantly narrows the gap with standard backpropagation.

