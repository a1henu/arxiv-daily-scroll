---
layout: default
title: Lifelong Embodied Navigation Learning
---

# Lifelong Embodied Navigation Learning
**arXiv**：[2603.06073v1](https://arxiv.org/abs/2603.06073) · [PDF](https://arxiv.org/pdf/2603.06073.pdf)  
**作者**：Xudong Wang, Jiahua Dong, Baichen Liu, Qi Lyu, Lianqing Liu, Zhi Han  

**一句话要点**：提出Uni-Walker框架以解决具身导航代理的终身学习问题

**关键词**：终身学习, 具身导航, 灾难性遗忘, 知识解耦, LoRA扩展, 链式思维推理

## 3 点简述
- 核心问题：具身导航代理在连续学习新任务时易发生灾难性遗忘，难以保留旧知识
- 方法要点：使用DE-LoRA解耦导航知识为共享与特定组件，结合知识继承和专家协同策略
- 实验或效果：广泛实验验证Uni-Walker在构建通用导航代理方面的优越性

## 摘要（原文）

> Embodied navigation agents powered by large language models have shown strong performance on individual tasks but struggle to continually acquire new navigation skills, which suffer from catastrophic forgetting. We formalize this challenge as lifelong embodied navigation learning (LENL), where an agent is required to adapt to a sequence of navigation tasks spanning multiple scenes and diverse user instruction styles, while retaining previously learned knowledge. To tackle this problem, we propose Uni-Walker, a lifelong embodied navigation framework that decouples navigation knowledge into task-shared and task-specific components with Decoder Extension LoRA (DE-LoRA). To learn the shared knowledge, we design a knowledge inheritance strategy and an experts co-activation strategy to facilitate shared knowledge transfer and refinement across multiple navigation tasks. To learn the specific knowledge, we propose an expert subspace orthogonality constraint together and a navigation-specific chain-of-thought reasoning mechanism to capture specific knowledge and enhance instruction-style understanding. Extensive experiments demonstrate the superiority of Uni-Walker for building universal navigation agents with lifelong learning.

