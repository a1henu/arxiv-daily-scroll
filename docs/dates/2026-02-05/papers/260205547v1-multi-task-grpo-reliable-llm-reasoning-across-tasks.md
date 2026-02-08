---
layout: default
title: Multi-Task GRPO: Reliable LLM Reasoning Across Tasks
---

# Multi-Task GRPO: Reliable LLM Reasoning Across Tasks
**arXiv**：[2602.05547v1](https://arxiv.org/abs/2602.05547) · [PDF](https://arxiv.org/pdf/2602.05547.pdf)  
**作者**：Shyam Sundhar Ramesh, Xiaotong Ji, Matthieu Zimmer, Sangwoong Yoon, Zhiyong Wang, Haitham Bou Ammar, Aurelien Lucchi, Ilija Bogunovic  

**一句话要点**：提出MT-GRPO算法以解决多任务推理中性能不平衡与梯度失真问题

**关键词**：多任务学习, 强化学习后训练, 任务权重调整, 梯度采样, 语言模型推理, 性能平衡

## 3 点简述
- 核心问题：标准GRPO在多任务适应中导致任务优化不平衡和梯度贡献失真
- 方法要点：动态调整任务权重优化最差任务性能，引入比率保持采样器确保梯度反映权重
- 实验效果：在3任务和9任务设置中，MT-GRPO显著提升最差任务准确率并减少训练步骤

## 摘要（原文）

> RL-based post-training with GRPO is widely used to improve large language models on individual reasoning tasks. However, real-world deployment requires reliable performance across diverse tasks. A straightforward multi-task adaptation of GRPO often leads to imbalanced outcomes, with some tasks dominating optimization while others stagnate. Moreover, tasks can vary widely in how frequently prompts yield zero advantages (and thus zero gradients), which further distorts their effective contribution to the optimization signal. To address these issues, we propose a novel Multi-Task GRPO (MT-GRPO) algorithm that (i) dynamically adapts task weights to explicitly optimize worst-task performance and promote balanced progress across tasks, and (ii) introduces a ratio-preserving sampler to ensure task-wise policy gradients reflect the adapted weights. Experiments on both 3-task and 9-task settings show that MT-GRPO consistently outperforms baselines in worst-task accuracy. In particular, MT-GRPO achieves 16-28% and 6% absolute improvement on worst-task performance over standard GRPO and DAPO, respectively, while maintaining competitive average accuracy. Moreover, MT-GRPO requires 50% fewer training steps to reach 50% worst-task accuracy in the 3-task setting, demonstrating substantially improved efficiency in achieving reliable performance across tasks.

