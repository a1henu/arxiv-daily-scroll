---
layout: default
title: Mitigating Forgetting in Low Rank Adaptation
---

# Mitigating Forgetting in Low Rank Adaptation
**arXiv**：[2512.17720v1](https://arxiv.org/abs/2512.17720) · [PDF](https://arxiv.org/pdf/2512.17720.pdf)  
**作者**：Joanna Sliwa, Frank Schneider, Philipp Hennig, Jose Miguel Hernandez-Lobato  

**一句话要点**：提出LaLoRA以缓解低秩适配中的灾难性遗忘问题

**关键词**：低秩适配, 灾难性遗忘, 拉普拉斯近似, 权重正则化, 参数高效微调, 模型微调

## 3 点简述
- 核心问题：低秩适配（LoRA）微调大模型时易导致灾难性遗忘，丢失预训练知识。
- 方法要点：基于拉普拉斯近似，对LoRA权重施加权重空间正则化，约束高曲率方向更新以保留知识。
- 实验或效果：在Llama模型数学推理微调中展示改进的学习-遗忘权衡，可通过正则化强度直接控制。

## 摘要（原文）

> Parameter-efficient fine-tuning methods, such as Low-Rank Adaptation (LoRA), enable fast specialization of large pre-trained models to different downstream applications. However, this process often leads to catastrophic forgetting of the model's prior domain knowledge. We address this issue with LaLoRA, a weight-space regularization technique that applies a Laplace approximation to Low-Rank Adaptation. Our approach estimates the model's confidence in each parameter and constrains updates in high-curvature directions, preserving prior knowledge while enabling efficient target-domain learning. By applying the Laplace approximation only to the LoRA weights, the method remains lightweight. We evaluate LaLoRA by fine-tuning a Llama model for mathematical reasoning and demonstrate an improved learning-forgetting trade-off, which can be directly controlled via the method's regularization strength. We further explore different loss landscape curvature approximations for estimating parameter confidence, analyze the effect of the data used for the Laplace approximation, and study robustness across hyperparameters.

