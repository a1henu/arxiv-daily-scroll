---
layout: default
title: Pragmatic Heterogeneous Collaborative Perception via Generative Communication Mechanism
---

# Pragmatic Heterogeneous Collaborative Perception via Generative Communication Mechanism
**arXiv**：[2510.19618v1](https://arxiv.org/abs/2510.19618) · [PDF](https://arxiv.org/pdf/2510.19618.pdf)  
**作者**：Junfei Zhou, Penglin Dai, Quanmin Wei, Bingyi Liu, Xiao Wu, Jianping Wang  

**一句话要点**：提出生成通信机制以解决异构多智能体协作感知中的领域差距问题

**关键词**：异构多智能体协作, 生成通信机制, 特征生成, 空间信息对齐, 轻量级集成, 条件扩散模型

## 3 点简述
- 核心问题：异构智能体因传感器和模型差异导致协作时出现领域差距，现有方法破坏语义一致性且扩展成本高
- 方法要点：使用生成通信机制，通过特征生成和空间信息对齐，无需修改原网络，实现轻量级新智能体集成
- 实验或效果：在多个数据集上优于现有方法，新智能体集成时计算成本和参数数量减少81%

## 摘要（原文）

> Multi-agent collaboration enhances the perception capabilities of individual
> agents through information sharing. However, in real-world applications,
> differences in sensors and models across heterogeneous agents inevitably lead
> to domain gaps during collaboration. Existing approaches based on adaptation
> and reconstruction fail to support pragmatic heterogeneous collaboration due to
> two key limitations: (1) Intrusive retraining of the encoder or core modules
> disrupts the established semantic consistency among agents; and (2)
> accommodating new agents incurs high computational costs, limiting scalability.
> To address these challenges, we present a novel Generative Communication
> mechanism (GenComm) that facilitates seamless perception across heterogeneous
> multi-agent systems through feature generation, without altering the original
> network, and employs lightweight numerical alignment of spatial information to
> efficiently integrate new agents at minimal cost. Specifically, a tailored
> Deformable Message Extractor is designed to extract spatial message for each
> collaborator, which is then transmitted in place of intermediate features. The
> Spatial-Aware Feature Generator, utilizing a conditional diffusion model,
> generates features aligned with the ego agent's semantic space while preserving
> the spatial information of the collaborators. These generated features are
> further refined by a Channel Enhancer before fusion. Experiments conducted on
> the OPV2V-H, DAIR-V2X and V2X-Real datasets demonstrate that GenComm
> outperforms existing state-of-the-art methods, achieving an 81\% reduction in
> both computational cost and parameter count when incorporating new agents. Our
> code is available at https://github.com/jeffreychou777/GenComm.

