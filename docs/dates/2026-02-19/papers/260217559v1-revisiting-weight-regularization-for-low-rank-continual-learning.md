---
layout: default
title: Revisiting Weight Regularization for Low-Rank Continual Learning
---

# Revisiting Weight Regularization for Low-Rank Continual Learning
**arXiv**：[2602.17559v1](https://arxiv.org/abs/2602.17559) · [PDF](https://arxiv.org/pdf/2602.17559.pdf)  
**作者**：Yaoyue Zheng, Yin Zhang, Joost van de Weijer, Gido M van de Ven, Shaoyi Du, Xuetao Zhang, Zhiqiang Tian  

**一句话要点**：提出EWC-LoRA方法，通过权重正则化缓解低秩持续学习中的任务干扰

**关键词**：持续学习, 权重正则化, 低秩适配器, 参数高效学习, 任务干扰缓解

## 3 点简述
- 核心问题：参数高效持续学习中权重正则化技术未充分探索，任务干扰影响性能
- 方法要点：使用弹性权重巩固正则化共享低秩更新，保持存储和推理成本恒定
- 实验或效果：在多个基准测试中优于现有低秩方法，实现稳定性与可塑性平衡

## 摘要（原文）

> Continual Learning (CL) with large-scale pre-trained models (PTMs) has recently gained wide attention, shifting the focus from training from scratch to continually adapting PTMs. This has given rise to a promising paradigm: parameter-efficient continual learning (PECL), where task interference is typically mitigated by assigning a task-specific module during training, such as low-rank adapters. However, weight regularization techniques, such as Elastic Weight Consolidation (EWC)-a key strategy in CL-remain underexplored in this new paradigm. In this paper, we revisit weight regularization in low-rank CL as a new perspective for mitigating task interference in PECL. Unlike existing low-rank CL methods, we mitigate task interference by regularizing a shared low-rank update through EWC, thereby keeping the storage requirement and inference costs constant regardless of the number of tasks. Our proposed method EWC-LoRA leverages a low-rank representation to estimate parameter importance over the full-dimensional space. This design offers a practical, computational- and memory-efficient solution for CL with PTMs, and provides insights that may inform the broader application of regularization techniques within PECL. Extensive experiments on various benchmarks demonstrate the effectiveness of EWC-LoRA, achieving a stability-plasticity trade-off superior to existing low-rank CL approaches. These results indicate that, even under low-rank parameterizations, weight regularization remains an effective mechanism for mitigating task interference. Code is available at: https://github.com/yaoyz96/low-rank-cl.

