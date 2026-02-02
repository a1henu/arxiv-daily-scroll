---
layout: default
title: Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments
---

# Test-Time Mixture of World Models for Embodied Agents in Dynamic Environments
**arXiv**：[2601.22647v1](https://arxiv.org/abs/2601.22647) · [PDF](https://arxiv.org/pdf/2601.22647.pdf)  
**作者**：Jinwoo Jang, Minjong Yoo, Sihyung Yoon, Honguk Woo  

**一句话要点**：提出测试时世界模型混合框架以增强具身智能体在动态环境中的适应性

**关键词**：具身智能体, 动态环境适应, 混合专家, 世界模型, 测试时学习, 原型路由

## 3 点简述
- 核心问题：基于语言模型的具身智能体在动态环境中适应性有限，需构建灵活世界模型以支持推理与决策。
- 方法要点：扩展混合专家范式，在测试时更新路由函数，通过多粒度原型路由、测试时精炼和蒸馏混合增强实现持续适应。
- 实验或效果：在VirtualHome、ALFWorld和RLBench基准上评估，展示零样本适应和少样本扩展场景下的强性能。

## 摘要（原文）

> Language model (LM)-based embodied agents are increasingly deployed in real-world settings. Yet, their adaptability remains limited in dynamic environments, where constructing accurate and flexible world models is crucial for effective reasoning and decision-making. To address this challenge, we extend the Mixture-of-Experts (MoE) paradigm to embodied agents. While conventional MoE architectures modularize knowledge into expert components with pre-trained routing, they remain rigid once deployed, making them less effective for adapting to unseen domains in dynamic environments. We therefore propose Test-time Mixture of World Models (TMoW), a framework that enhances adaptability to unseen and evolving domains. TMoW updates its routing function over world models at test time, unlike conventional MoE where the function remains fixed, enabling agents to recombine existing models and integrate new ones for continual adaptation. It achieves this through (i) multi-granular prototype-based routing, which adapts mixtures across object- to scene-level similarities, (ii) test-time refinement that aligns unseen domain features with prototypes during inference, and (iii) distilled mixture-based augmentation, which efficiently constructs new models from few-shot data and existing prototypes. We evaluate TMoW on VirtualHome, ALFWorld, and RLBench benchmarks, demonstrating strong performance in both zero-shot adaptation and few-shot expansion scenarios, and showing that it enables embodied agents to operate effectively in dynamic environments.

