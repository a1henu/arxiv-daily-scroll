---
layout: default
title: Is Gradient Ascent Really Necessary? Memorize to Forget for Machine Unlearning
---

# Is Gradient Ascent Really Necessary? Memorize to Forget for Machine Unlearning
**arXiv**：[2602.06441v1](https://arxiv.org/abs/2602.06441) · [PDF](https://arxiv.org/pdf/2602.06441.pdf)  
**作者**：Zhuo Huang, Qizhou Wang, Ziming Hong, Shanshan Ye, Bo Han, Tongliang Liu  

**一句话要点**：提出模型外推法替代梯度上升，以稳定机器遗忘过程

**关键词**：机器遗忘, 梯度上升, 模型外推, 记忆模型, 预测一致性

## 3 点简述
- 核心问题：梯度上升在机器遗忘中易导致灾难性崩溃，影响模型性能
- 方法要点：通过训练记忆模型并外推至参考模型，避免直接使用梯度上升
- 实验或效果：该方法简单高效，能稳定训练并提升遗忘性能

## 摘要（原文）

> For ethical and safe AI, machine unlearning rises as a critical topic aiming to protect sensitive, private, and copyrighted knowledge from misuse. To achieve this goal, it is common to conduct gradient ascent (GA) to reverse the training on undesired data. However, such a reversal is prone to catastrophic collapse, which leads to serious performance degradation in general tasks. As a solution, we propose model extrapolation as an alternative to GA, which reaches the counterpart direction in the hypothesis space from one model given another reference model. Therefore, we leverage the original model as the reference, further train it to memorize undesired data while keeping prediction consistency on the rest retained data, to obtain a memorization model. Counterfactual as it might sound, a forget model can be obtained via extrapolation from the memorization model to the reference model. Hence, we avoid directly acquiring the forget model using GA, but proceed with gradient descent for the memorization model, which successfully stabilizes the machine unlearning process. Our model extrapolation is simple and efficient to implement, and it can also effectively converge throughout training to achieve improved unlearning performance.

