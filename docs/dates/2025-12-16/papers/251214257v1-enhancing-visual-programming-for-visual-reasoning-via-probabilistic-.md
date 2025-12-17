---
layout: default
title: Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs
---

# Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs
**arXiv**：[2512.14257v1](https://arxiv.org/abs/2512.14257) · [PDF](https://arxiv.org/pdf/2512.14257.pdf)  
**作者**：Wentao Wan, Kaiyu Wu, Qingyang Ma, Nan Kang, Yunjie Chen, Liang Lin, Keze Wang  

**一句话要点**：提出EVPG方法，通过概率图增强视觉编程以优化视觉推理任务

**关键词**：视觉编程, 概率图模型, 端到端学习, 视觉推理, 梯度优化

## 3 点简述
- 核心问题：视觉编程中预训练模型优化困难，因缺乏子任务标签且框架不可微分
- 方法要点：构建有向概率图，将不可微执行过程转为可微概率推断，实现端到端梯度优化
- 实验或效果：在GQA、NLVRv2和Open Images任务上验证有效性，性能显著提升

## 摘要（原文）

> Recently, Visual Programming (VP) based on large language models (LLMs) has rapidly developed and demonstrated significant potential in complex Visual Reasoning (VR) tasks. Previous works to enhance VP have primarily focused on improving the quality of LLM-generated visual programs. However, they have neglected to optimize the VP-invoked pre-trained models, which serve as modules for the visual sub-tasks decomposed from the targeted tasks by VP. The difficulty is that there are only final labels of targeted VR tasks rather than labels of sub-tasks. Besides, the non-differentiable nature of VP impedes the direct use of efficient gradient-based optimization methods to leverage final labels for end-to-end learning of the entire VP framework. To overcome these issues, we propose EVPG, a method to Enhance Visual Programming for visual reasoning via Probabilistic Graphs. Specifically, we creatively build a directed probabilistic graph according to the variable dependency relationships during the VP executing process, which reconstructs the non-differentiable VP executing process into a differentiable exact probability inference process on this directed probabilistic graph. As a result, this enables the VP framework to utilize the final labels for efficient, gradient-based optimization in end-to-end supervised learning on targeted VR tasks. Extensive and comprehensive experiments demonstrate the effectiveness and advantages of our EVPG, showing significant performance improvements for VP on three classical complex VR tasks: GQA, NLVRv2, and Open Images.

