---
layout: default
title: DeepHalo: A Neural Choice Model with Controllable Context Effects
---

# DeepHalo: A Neural Choice Model with Controllable Context Effects
**arXiv**：[2601.04616v1](https://arxiv.org/abs/2601.04616) · [PDF](https://arxiv.org/pdf/2601.04616.pdf)  
**作者**：Shuhan Zhang, Zhi Wang, Rui Gao, Shuang Li  

**一句话要点**：提出DeepHalo神经选择模型，以可控方式建模上下文效应，用于推荐和偏好学习。

**关键词**：上下文效应建模, 神经选择模型, 可解释人工智能, 推荐系统, 偏好学习

## 3 点简述
- 核心问题：传统模型忽略上下文效应，而行为研究显示选择集组成影响偏好，现有模型在特征设置下受限或缺乏可解释性。
- 方法要点：DeepHalo结合特征，允许显式控制交互阶数，提供上下文效应的原则性解释，作为通用逼近器。
- 实验或效果：在合成和真实数据集上验证了强预测性能，并增强了对选择驱动因素的透明度。

## 摘要（原文）

> Modeling human decision-making is central to applications such as recommendation, preference learning, and human-AI alignment. While many classic models assume context-independent choice behavior, a large body of behavioral research shows that preferences are often influenced by the composition of the choice set itself -- a phenomenon known as the context effect or Halo effect. These effects can manifest as pairwise (first-order) or even higher-order interactions among the available alternatives. Recent models that attempt to capture such effects either focus on the featureless setting or, in the feature-based setting, rely on restrictive interaction structures or entangle interactions across all orders, which limits interpretability. In this work, we propose DeepHalo, a neural modeling framework that incorporates features while enabling explicit control over interaction order and principled interpretation of context effects. Our model enables systematic identification of interaction effects by order and serves as a universal approximator of context-dependent choice functions when specialized to a featureless setting. Experiments on synthetic and real-world datasets demonstrate strong predictive performance while providing greater transparency into the drivers of choice.

