---
layout: default
title: Weak-Driven Learning: How Weak Agents make Strong Agents Stronger
---

# Weak-Driven Learning: How Weak Agents make Strong Agents Stronger
**arXiv**：[2602.08222v1](https://arxiv.org/abs/2602.08222) · [PDF](https://arxiv.org/pdf/2602.08222.pdf)  
**作者**：Zehao Chen, Gongxun Li, Tianxiang Ai, Yifei Li, Zixuan Huang, Wang Zhou, Fuzhen Zhuang, Xianglong Liu, Jianxin Li, Deqing Wang, Yikun Ban  

**一句话要点**：提出WMSS后训练范式，利用弱检查点突破大语言模型优化饱和瓶颈。

**关键词**：后训练优化, 大语言模型, 弱驱动学习, 熵动态分析, 补偿性学习

## 3 点简述
- 核心问题：大语言模型后训练中，高置信度导致性能提升饱和，传统方法收益递减。
- 方法要点：通过熵动态识别可恢复学习差距，利用历史弱检查点进行补偿性学习。
- 实验或效果：在数学推理和代码生成数据集上实现有效性能提升，无额外推理成本。

## 摘要（原文）

> As post-training optimization becomes central to improving large language models, we observe a persistent saturation bottleneck: once models grow highly confident, further training yields diminishing returns. While existing methods continue to reinforce target predictions, we find that informative supervision signals remain latent in models' own historical weak states. Motivated by this observation, we propose WMSS (Weak Agents Can Make Strong Agents Stronger), a post-training paradigm that leverages weak checkpoints to guide continued optimization. By identifying recoverable learning gaps via entropy dynamics and reinforcing them through compensatory learning, WMSS enables strong agents to improve beyond conventional post-training saturation. Experiments on mathematical reasoning and code generation datasets show that agents trained with our approach achieve effective performance improvements, while incurring zero additional inference cost.

