---
layout: default
title: Training Data Selection with Gradient Orthogonality for Efficient Domain Adaptation
---

# Training Data Selection with Gradient Orthogonality for Efficient Domain Adaptation
**arXiv**：[2602.06359v1](https://arxiv.org/abs/2602.06359) · [PDF](https://arxiv.org/pdf/2602.06359.pdf)  
**作者**：Xiyang Zhang, Yuanhe Tian, Hongzhi Wang, Yan Song  

**一句话要点**：提出正交梯度选择方法，以高效数据选择解决大语言模型领域适应中的灾难性遗忘问题。

**关键词**：领域适应, 灾难性遗忘, 梯度正交性, 数据选择, 大语言模型, 强化学习

## 3 点简述
- 核心问题：大语言模型领域微调时，灾难性遗忘导致领域性能与通用能力难以兼顾。
- 方法要点：通过轻量导航模型和强化学习，动态选择梯度与通用知识锚正交的训练样本。
- 实验或效果：在医疗、法律和金融领域实验中，提升领域性能与训练效率，保持通用任务表现。

## 摘要（原文）

> Fine-tuning large language models (LLMs) for specialized domains often necessitates a trade-off between acquiring domain expertise and retaining general reasoning capabilities, a phenomenon known as catastrophic forgetting. Existing remedies face a dichotomy: gradient surgery methods offer geometric safety but incur prohibitive computational costs via online projections, while efficient data selection approaches reduce overhead but remain blind to conflict-inducing gradient directions. In this paper, we propose Orthogonal Gradient Selection (OGS), a data-centric method that harmonizes domain performance, general capability retention, and training efficiency. OGS shifts the geometric insights of gradient projection from the optimizer to the data selection stage by treating data selection as a constrained decision-making process. By leveraging a lightweight Navigator model and reinforcement learning techniques, OGS dynamically identifies training samples whose gradients are orthogonal to a general-knowledge anchor. This approach ensures naturally safe updates for target models without modifying the optimizer or incurring runtime projection costs. Experiments across medical, legal, and financial domains demonstrate that OGS achieves excellent results, significantly improving domain performance and training efficiency while maintaining or even enhancing performance on general tasks such as GSM8K.

