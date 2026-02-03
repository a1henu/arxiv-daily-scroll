---
layout: default
title: Advancing General-Purpose Reasoning Models with Modular Gradient Surgery
---

# Advancing General-Purpose Reasoning Models with Modular Gradient Surgery
**arXiv**：[2602.02301v1](https://arxiv.org/abs/2602.02301) · [PDF](https://arxiv.org/pdf/2602.02301.pdf)  
**作者**：Min Cai, Yu Liang, Longzheng Wang, Yan Wang, Yueyang Zhang, Long Xia, Zhiyuan Sun, Xi Ye, Daiting Shi  

**一句话要点**：提出模块化梯度手术以解决多领域强化学习中的梯度冲突问题

**关键词**：模块化梯度手术, 多领域强化学习, 通用推理模型, 梯度冲突, Transformer优化

## 3 点简述
- 核心问题：多领域训练中，领域异质性导致行为与梯度层面的交叉干扰，限制通用推理模型性能提升。
- 方法要点：在Transformer模块层面实施梯度手术，缓解梯度冲突，提升模型在多领域中的泛化能力。
- 实验或效果：在Llama和Qwen模型上，相比标准多任务强化学习，平均提升4.3和4.5点，覆盖数学、通用聊天和指令遵循领域。

## 摘要（原文）

> Reinforcement learning (RL) has played a central role in recent advances in large reasoning models (LRMs), yielding strong gains in verifiable and open-ended reasoning. However, training a single general-purpose LRM across diverse domains remains challenging due to pronounced domain heterogeneity. Through a systematic study of two widely used strategies, Sequential RL and Mixed RL, we find that both incur substantial cross-domain interference at the behavioral and gradient levels, resulting in limited overall gains. To address these challenges, we introduce **M**odular **G**radient **S**urgery (**MGS**), which resolves gradient conflicts at the module level within the transformer. When applied to Llama and Qwen models, MGS achieves average improvements of 4.3 (16.6\%) and 4.5 (11.1\%) points, respectively, over standard multi-task RL across three representative domains (math, general chat, and instruction following). Further analysis demonstrates that MGS remains effective under prolonged training. Overall, our study clarifies the sources of interference in multi-domain RL and presents an effective solution for training general-purpose LRMs.

