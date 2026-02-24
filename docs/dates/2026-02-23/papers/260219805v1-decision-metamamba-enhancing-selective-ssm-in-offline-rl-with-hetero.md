---
layout: default
title: Decision MetaMamba: Enhancing Selective SSM in Offline RL with Heterogeneous Sequence Mixing
---

# Decision MetaMamba: Enhancing Selective SSM in Offline RL with Heterogeneous Sequence Mixing
**arXiv**：[2602.19805v1](https://arxiv.org/abs/2602.19805) · [PDF](https://arxiv.org/pdf/2602.19805.pdf)  
**作者**：Wall Kim, Chaeyoung Song, Hanul Kim  

**一句话要点**：提出Decision MetaMamba以解决离线强化学习中Mamba模型选择性机制导致关键步骤信息丢失的问题。

**关键词**：离线强化学习, Mamba模型, 序列混合, 选择性机制, 参数效率

## 3 点简述
- 核心问题：Mamba模型在离线强化学习中，其选择性机制可能因忽略序列中的关键步骤而损害性能。
- 方法要点：用基于密集层的序列混合器替换Mamba的token混合器，并修改位置结构以保留局部信息，实现异构序列混合。
- 实验或效果：在多种强化学习任务中达到最先进性能，且参数紧凑，具有实际应用潜力。

## 摘要（原文）

> Mamba-based models have drawn much attention in offline RL. However, their selective mechanism often detrimental when key steps in RL sequences are omitted. To address these issues, we propose a simple yet effective structure, called Decision MetaMamba (DMM), which replaces Mamba's token mixer with a dense layer-based sequence mixer and modifies positional structure to preserve local information. By performing sequence mixing that considers all channels simultaneously before Mamba, DMM prevents information loss due to selective scanning and residual gating. Extensive experiments demonstrate that our DMM delivers the state-of-the-art performance across diverse RL tasks. Furthermore, DMM achieves these results with a compact parameter footprint, demonstrating strong potential for real-world applications.

