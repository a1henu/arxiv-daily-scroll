---
layout: default
title: Causally Robust Reward Learning from Reason-Augmented Preference Feedback
---

# Causally Robust Reward Learning from Reason-Augmented Preference Feedback
**arXiv**：[2603.04861v1](https://arxiv.org/abs/2603.04861) · [PDF](https://arxiv.org/pdf/2603.04861.pdf)  
**作者**：Minjune Hwang, Yigit Korkmaz, Daniel Seita, Erdem Bıyık  

**一句话要点**：提出ReCouPLe框架，利用自然语言理由增强偏好反馈以解决奖励学习中的因果混淆问题。

**关键词**：奖励学习, 因果混淆, 自然语言理由, 偏好反馈, 泛化能力, 嵌入空间

## 3 点简述
- 核心问题：基于偏好的奖励学习易受因果混淆影响，奖励模型可能依赖虚假特征，导致泛化能力差。
- 方法要点：引入自然语言理由作为嵌入空间的指导轴，训练模型基于与理由对齐的特征评分轨迹，去除非相关上下文。
- 实验或效果：在分布偏移下奖励准确率提升达1.5倍，新任务中下游策略性能提升达2倍，无需额外数据或语言模型微调。

## 摘要（原文）

> Preference-based reward learning is widely used for shaping agent behavior to match a user's preference, yet its sparse binary feedback makes it especially vulnerable to causal confusion. The learned reward often latches onto spurious features that merely co-occur with preferred trajectories during training, collapsing when those correlations disappear or reverse at test time. We introduce ReCouPLe, a lightweight framework that uses natural language rationales to provide the missing causal signal. Each rationale is treated as a guiding projection axis in an embedding space, training the model to score trajectories based on features aligned with that axis while de-emphasizing context that is unrelated to the stated reason. Because the same rationales (e.g., "avoids collisions", "completes the task faster") can appear across multiple tasks, ReCouPLe naturally reuses the same causal direction whenever tasks share semantics, and transfers preference knowledge to novel tasks without extra data or language-model fine-tuning. Our learned reward model can ground preferences on the articulated reason, aligning better with user intent and generalizing beyond spurious features. ReCouPLe outperforms baselines by up to 1.5x in reward accuracy under distribution shifts, and 2x in downstream policy performance in novel tasks. We have released our code at https://github.com/mj-hwang/ReCouPLe

