---
layout: default
title: AnchorOPT: Towards Optimizing Dynamic Anchors for Adaptive Prompt Learning
---

# AnchorOPT: Towards Optimizing Dynamic Anchors for Adaptive Prompt Learning
**arXiv**：[2511.21188v1](https://arxiv.org/abs/2511.21188) · [PDF](https://arxiv.org/pdf/2511.21188.pdf)  
**作者**：Zheng Li, Yibing Song, Xin Zhang, Lei Luo, Xiang Li, Jian Yang  

**一句话要点**：提出AnchorOPT以优化动态锚点，提升自适应提示学习的灵活性。

**关键词**：提示学习, 动态锚点, CLIP模型, 自适应优化, 即插即用模块

## 3 点简述
- 现有提示学习方法使用静态锚点，缺乏跨任务和阶段自适应性。
- AnchorOPT动态学习锚点值和位置矩阵，分两阶段训练优化。
- 实验显示性能可比或优于其他方法，作为即插即用模块提升泛化。

## 摘要（原文）

> Existing prompt learning methods, which are built upon CLIP models, leverage textual tokens as anchors to guide the learnable soft tokens. This guidance improves CLIP generalizations. However, these anchors-static in both value and position-lack cross-task and stage-adaptive flexibility. To address this limitation, we propose AnchorOPT, a dynamic anchor-based prompt learning framework. Specifically, AnchorOPT introduces dynamism in two key dimensions: (i) anchor values eschew handcrafted explicit textual tokens (e.g., "shape", "color"), instead learning dynamically from task-specific data; and (ii) the positional relationship between anchor and soft tokens is no longer fixed but adaptively optimized via a learnable position matrix conditioned on the training stage and task context. Training occurs in two stages: we first learn the anchor tokens, then freeze and transfer them to the second stage for optimization of soft tokens and the position matrix. Extensive experiments demonstrate that using only a simple learnable anchor and position matrix achieves performance comparable to or exceeding some methods incorporating additional learnable modules or regularization techniques. As a plug-and-play module, AnchorOPT integrates seamlessly into existing frameworks, yielding consistent performance gains across diverse datasets. Code is publicly available at https://github.com/zhengli97/ATPrompt.

