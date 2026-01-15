---
layout: default
title: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection
---

# Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection
**arXiv**：[2601.09684v1](https://arxiv.org/abs/2601.09684) · [PDF](https://arxiv.org/pdf/2601.09684.pdf)  
**作者**：Ziyu Yang, Guibin Chen, Yuxin Yang, Aoxiong Zeng, Xiangquan Yang  

**一句话要点**：提出Ortho-LoRA以解决多任务LoRA中的梯度冲突问题

**关键词**：多任务学习, 低秩适应, 梯度投影, 正交分解, 参数高效微调, 大语言模型

## 3 点简述
- 多任务LoRA因梯度冲突导致负迁移，性能低于单任务微调
- Ortho-LoRA通过正交梯度投影在LoRA子空间内动态消除任务间干扰
- 在GLUE基准上恢复95%性能差距，计算开销可忽略

## 摘要（原文）

> Multi-Task Learning (MTL) combined with Low-Rank Adaptation (LoRA) has emerged as a promising direction for parameter-efficient deployment of Large Language Models (LLMs). By sharing a single adapter across multiple tasks, one can significantly reduce storage overhead. However, this approach suffers from negative transfer, where conflicting gradient updates from distinct tasks degrade the performance of individual tasks compared to single-task fine-tuning. This problem is exacerbated in LoRA due to the low-rank constraint, which limits the optimization landscape's capacity to accommodate diverse task requirements. In this paper, we propose Ortho-LoRA, a gradient projection method specifically tailored for the bipartite structure of LoRA. Ortho-LoRA dynamically projects conflicting task gradients onto the orthogonal complement of each other within the intrinsic LoRA subspace. Extensive experiments on the GLUE benchmark demonstrate that Ortho-LoRA effectively mitigates task interference, outperforming standard joint training and recovering 95\% of the performance gap between multi-task and single-task baselines with negligible computational overhead.

