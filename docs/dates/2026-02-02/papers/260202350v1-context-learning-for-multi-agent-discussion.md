---
layout: default
title: Context Learning for Multi-Agent Discussion
---

# Context Learning for Multi-Agent Discussion
**arXiv**：[2602.02350v1](https://arxiv.org/abs/2602.02350) · [PDF](https://arxiv.org/pdf/2602.02350.pdf)  
**作者**：Xingyuan Hua, Sheng Yue, Xinyi Li, Yizhe Zhao, Jinrui Zhang, Ju Ren  

**一句话要点**：提出多智能体上下文学习方法以解决讨论不一致问题

**关键词**：多智能体讨论, 上下文学习, 大语言模型, 自适应机制, 信息组织

## 3 点简述
- 核心问题：多智能体讨论中因上下文错配导致解决方案不连贯
- 方法要点：训练上下文生成器动态组织信息，通过自适应机制控制一致性和输出差异
- 实验或效果：在学术推理等任务上性能提升20%–50%，具有良好可迁移性和计算效率

## 摘要（原文）

> Multi-Agent Discussion (MAD) has garnered increasing attention very recently, where multiple LLM instances collaboratively solve problems via structured discussion. However, we find that current MAD methods easily suffer from discussion inconsistency, LLMs fail to reach a coherent solution, due to the misalignment between their individual contexts.In this paper, we introduce a multi-LLM context learning method (M2CL) that learns a context generator for each agent, capable of dynamically generating context instructions per discussion round via automatic information organization and refinement. Specifically, inspired by our theoretical insights on the context instruction, M2CL train the generators to control context coherence and output discrepancies via a carefully crafted self-adaptive mechanism.It enables LLMs to avoid premature convergence on majority noise and progressively reach the correct consensus. We evaluate M2CL on challenging tasks, including academic reasoning, embodied tasks, and mobile control. The results show that the performance of M2CL significantly surpasses existing methods by 20%--50%, while enjoying favorable transferability and computational efficiency.

