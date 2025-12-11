---
layout: default
title: Efficient Continual Learning in Neural Machine Translation: A Low-Rank Adaptation Approach
---

# Efficient Continual Learning in Neural Machine Translation: A Low-Rank Adaptation Approach
**arXiv**：[2512.09910v1](https://arxiv.org/abs/2512.09910) · [PDF](https://arxiv.org/pdf/2512.09910.pdf)  
**作者**：Salvador Carrión, Francisco Casacuberta  

**一句话要点**：提出基于低秩适配的持续学习方法，以解决神经机器翻译中的灾难性遗忘和高计算成本问题。

**关键词**：神经机器翻译, 持续学习, 低秩适配, 灾难性遗忘, 参数高效学习, 交互式调整

## 3 点简述
- 核心问题：神经机器翻译持续学习面临灾难性遗忘和重训练计算成本高的双重挑战。
- 方法要点：采用低秩适配框架，结合交互式模块组合和基于梯度的正则化策略，实现参数高效调整。
- 实验或效果：实验表明方法在性能媲美全参数技术的同时，有效保留旧知识并支持新任务学习。

## 摘要（原文）

> Continual learning in Neural Machine Translation (NMT) faces the dual challenges of catastrophic forgetting and the high computational cost of retraining. This study establishes Low-Rank Adaptation (LoRA) as a parameter-efficient framework to address these challenges in dedicated NMT architectures. We first demonstrate that LoRA-based fine-tuning adapts NMT models to new languages and domains with performance on par with full-parameter techniques, while utilizing only a fraction of the parameter space. Second, we propose an interactive adaptation method using a calibrated linear combination of LoRA modules. This approach functions as a gate-free mixture of experts, enabling real-time, user-controllable adjustments to domain and style without retraining. Finally, to mitigate catastrophic forgetting, we introduce a novel gradient-based regularization strategy specifically designed for low-rank decomposition matrices. Unlike methods that regularize the full parameter set, our approach weights the penalty on the low-rank updates using historical gradient information. Experimental results indicate that this strategy efficiently preserves prior domain knowledge while facilitating the acquisition of new tasks, offering a scalable paradigm for interactive and continual NMT.

