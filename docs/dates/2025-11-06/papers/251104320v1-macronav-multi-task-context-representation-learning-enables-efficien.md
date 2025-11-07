---
layout: default
title: MacroNav: Multi-Task Context Representation Learning Enables Efficient Navigation in Unknown Environments
---

# MacroNav: Multi-Task Context Representation Learning Enables Efficient Navigation in Unknown Environments
**arXiv**：[2511.04320v1](https://arxiv.org/abs/2511.04320) · [PDF](https://arxiv.org/pdf/2511.04320.pdf)  
**作者**：Kuankuan Sima, Longbin Tang, Haozhe Ma, Lin Zhao  

**一句话要点**：提出MacroNav框架以解决未知环境中自主导航的效率与表示平衡问题

**关键词**：自主导航, 上下文表示学习, 多任务学习, 强化学习, 图推理, 未知环境

## 3 点简述
- 核心问题：未知环境中部分可观测下，现有方法难以平衡丰富上下文表示与导航效率。
- 方法要点：采用多任务自监督学习训练轻量上下文编码器，结合强化学习与图推理进行动作选择。
- 实验或效果：在真实世界部署中，成功率和路径长度加权成功率显著优于现有方法，计算成本低。

## 摘要（原文）

> Autonomous navigation in unknown environments requires compact yet expressive
> spatial understanding under partial observability to support high-level
> decision making. Existing approaches struggle to balance rich contextual
> representation with navigation efficiency. We present MacroNav, a
> learning-based navigation framework featuring two key components: (1) a
> lightweight context encoder trained via multi-task self-supervised learning to
> capture multi-scale, navigation-centric spatial representations; and (2) a
> reinforcement learning policy that seamlessly integrates these representations
> with graph-based reasoning for efficient action selection. Extensive
> experiments demonstrate the context encoder's efficient and robust
> environmental understanding. Real-world deployments further validate MacroNav's
> effectiveness, yielding significant gains over state-of-the-art navigation
> methods in both Success Rate (SR) and Success weighted by Path Length (SPL),
> while maintaining low computational cost. Code will be released upon
> acceptance.

