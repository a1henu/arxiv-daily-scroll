---
layout: default
title: Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter
---

# Learning to Nudge: A Scalable Barrier Function Framework for Safe Robot Interaction in Dense Clutter
**arXiv**：[2601.02686v1](https://arxiv.org/abs/2601.02686) · [PDF](https://arxiv.org/pdf/2601.02686.pdf)  
**作者**：Haixin Jin, Nikhil Uday Shinde, Soofiyan Atar, Hongzhan Yu, Dylan Hirsch, Sicun Gao, Michael C. Yip, Sylvia Herbert  

**一句话要点**：提出密集接触屏障函数以解决机器人密集杂乱环境中的安全交互问题

**关键词**：机器人安全, 屏障函数, 密集杂乱环境, 可组合学习, 安全交互

## 3 点简述
- 核心问题：传统安全框架避免接触，限制机器人在密集杂乱环境中的操作能力
- 方法要点：学习可组合的以对象为中心的屏障函数，隐式捕获物理交互安全约束
- 实验或效果：模拟实验验证了在密集杂乱环境中实现无碰撞导航和安全接触交互

## 摘要（原文）

> Robots operating in everyday environments must navigate and manipulate within densely cluttered spaces, where physical contact with surrounding objects is unavoidable. Traditional safety frameworks treat contact as unsafe, restricting robots to collision avoidance and limiting their ability to function in dense, everyday settings. As the number of objects grows, model-based approaches for safe manipulation become computationally intractable; meanwhile, learned methods typically tie safety to the task at hand, making them hard to transfer to new tasks without retraining. In this work we introduce Dense Contact Barrier Functions(DCBF). Our approach bypasses the computational complexity of explicitly modeling multi-object dynamics by instead learning a composable, object-centric function that implicitly captures the safety constraints arising from physical interactions. Trained offline on interactions with a few objects, the learned DCBFcomposes across arbitrary object sets at runtime, producing a single global safety filter that scales linearly and transfers across tasks without retraining. We validate our approach through simulated experiments in dense clutter, demonstrating its ability to enable collision-free navigation and safe, contact-rich interaction in suitable settings.

