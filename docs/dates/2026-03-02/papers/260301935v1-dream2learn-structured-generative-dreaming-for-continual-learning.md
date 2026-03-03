---
layout: default
title: Dream2Learn: Structured Generative Dreaming for Continual Learning
---

# Dream2Learn: Structured Generative Dreaming for Continual Learning
**arXiv**：[2603.01935v1](https://arxiv.org/abs/2603.01935) · [PDF](https://arxiv.org/pdf/2603.01935.pdf)  
**作者**：Salvatore Calcagno, Matteo Pennisi, Federica Proietto Salanitri, Amelia Sorrenti, Simone Palazzo, Concetto Spampinato, Giovanni Bellitto  

**一句话要点**：提出Dream2Learn框架，通过结构化生成梦境实现持续学习中的知识重组与正向迁移。

**关键词**：持续学习, 生成梦境, 扩散模型, 知识重组, 正向迁移

## 3 点简述
- 核心问题：持续学习中平衡可塑性与稳定性，缓解灾难性遗忘。
- 方法要点：利用冻结扩散模型和软提示优化，生成语义新颖的梦境类样本，用于自训练以重组表示空间。
- 实验或效果：在Mini-ImageNet等数据集上优于基于排练的基线，实现正向迁移，提升适应性。

## 摘要（原文）

> Continual learning requires balancing plasticity and stability while mitigating catastrophic forgetting. Inspired by human dreaming as a mechanism for internal simulation and knowledge restructuring, we introduce Dream2Learn (D2L), a framework in which a model autonomously generates structured synthetic experiences from its own internal representations and uses them for self-improvement. Rather than reconstructing past data as in generative replay, D2L enables a classifier to create novel, semantically distinct dreamed classes that are coherent with its learned knowledge yet do not correspond to previously observed data. These dreamed samples are produced by conditioning a frozen diffusion model through soft prompt optimization driven by the classifier itself. The generated data are not used to replace memory, but to expand and reorganize the representation space, effectively allowing the network to self-train on internally synthesized concepts. By integrating dreamed classes into continual training, D2L proactively structures latent features to support forward knowledge transfer and adaptation to future tasks. This prospective self-training mechanism mirrors the role of sleep in consolidating and reorganizing memory, turning internal simulations into a tool for improved generalization. Experiments on Mini-ImageNet, FG-ImageNet, and ImageNet-R demonstrate that D2L consistently outperforms strong rehearsal-based baselines and achieves positive forward transfer, confirming its ability to enhance adaptability through internally generated training signals.

