---
layout: default
title: Using reinforcement learning to probe the role of feedback in skill acquisition
---

# Using reinforcement learning to probe the role of feedback in skill acquisition
**arXiv**：[2512.08463v1](https://arxiv.org/abs/2512.08463) · [PDF](https://arxiv.org/pdf/2512.08463.pdf)  
**作者**：Antonio Terpin, Raffaello D'Andrea  

**一句话要点**：通过强化学习探究反馈在技能获取中的作用，使用旋转圆柱体实验验证反馈对学习与执行的影响差异。

**关键词**：强化学习, 技能获取, 反馈机制, 物理系统实验, 拖曳力控制

## 3 点简述
- 研究技能获取中反馈的作用，以物理系统替代人类实验，聚焦于拖曳力控制任务。
- 采用强化学习代理与旋转圆柱体交互，利用高维流反馈快速发现高性能策略。
- 实验显示学习需要反馈，但执行无需反馈，且学习效果受目标（最小化或最大化拖曳力）影响显著。

## 摘要（原文）

> Many high-performance human activities are executed with little or no external feedback: think of a figure skater landing a triple jump, a pitcher throwing a curveball for a strike, or a barista pouring latte art. To study the process of skill acquisition under fully controlled conditions, we bypass human subjects. Instead, we directly interface a generalist reinforcement learning agent with a spinning cylinder in a tabletop circulating water channel to maximize or minimize drag. This setup has several desirable properties. First, it is a physical system, with the rich interactions and complex dynamics that only the physical world has: the flow is highly chaotic and extremely difficult, if not impossible, to model or simulate accurately. Second, the objective -- drag minimization or maximization -- is easy to state and can be captured directly in the reward, yet good strategies are not obvious beforehand. Third, decades-old experimental studies provide recipes for simple, high-performance open-loop policies. Finally, the setup is inexpensive and far easier to reproduce than human studies. In our experiments we find that high-dimensional flow feedback lets the agent discover high-performance drag-control strategies with only minutes of real-world interaction. When we later replay the same action sequences without any feedback, we obtain almost identical performance. This shows that feedback, and in particular flow feedback, is not needed to execute the learned policy. Surprisingly, without flow feedback during training the agent fails to discover any well-performing policy in drag maximization, but still succeeds in drag minimization, albeit more slowly and less reliably. Our studies show that learning a high-performance skill can require richer information than executing it, and learning conditions can be kind or wicked depending solely on the goal, not on dynamics or policy complexity.

