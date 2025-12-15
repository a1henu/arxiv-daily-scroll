---
layout: default
title: Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization
---

# Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization
**arXiv**：[2512.11391v1](https://arxiv.org/abs/2512.11391) · [PDF](https://arxiv.org/pdf/2512.11391.pdf)  
**作者**：Yifan Niu, Han Xiao, Dongyi Liu, Nuo Chen, Jia Li  

**一句话要点**：提出零空间约束策略优化以缓解大语言模型安全对齐中的能力遗忘问题

**关键词**：大语言模型, 安全对齐, 强化学习, 零空间投影, 策略优化, 对齐税

## 3 点简述
- 核心问题：强化学习安全对齐导致大语言模型遗忘通用能力，即对齐税
- 方法要点：将安全策略梯度几何投影到通用任务的零空间，以保留核心能力
- 实验或效果：在数学、代码等任务上实现最优安全性能，且数据效率高

## 摘要（原文）

> As Large Language Models (LLMs) are increasingly deployed in real-world applications, it is important to ensure their behaviors align with human values, societal norms, and ethical principles. However, safety alignment under Reinforcement Learning (RL) often suffers from forgetting learned general abilities, which is also known as the alignment tax. To address this issue, we introduce Null-Space constrained Policy Optimization (NSPO), a novel RL framework for LLM safety alignment while preserving their core abilities. The safety policy gradients are geometrically projected into the null space of general tasks, thereby mitigating the safety alignment tax. In addition, we theoretically prove that NSPO preserves the model's original core capabilities, while still guaranteeing a descent direction for effective safety alignment. Extensive experiments demonstrate that NSPO outperforms existing methods by a large margin, achieving state-of-the-art safety performance without sacrificing accuracy on general tasks, including math, code, and instruction-following tasks. Notably, NSPO is data-efficient and only requires 40% of public human-annotated safety data from PKU-SafeRLHF to achieve promising safety performance, without a large amount of mixed general tasks data in existing alignment methods.

