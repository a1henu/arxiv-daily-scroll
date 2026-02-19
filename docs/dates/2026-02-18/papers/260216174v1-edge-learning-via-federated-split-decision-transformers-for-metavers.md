---
layout: default
title: Edge Learning via Federated Split Decision Transformers for Metaverse Resource Allocation
---

# Edge Learning via Federated Split Decision Transformers for Metaverse Resource Allocation
**arXiv**：[2602.16174v1](https://arxiv.org/abs/2602.16174) · [PDF](https://arxiv.org/pdf/2602.16174.pdf)  
**作者**：Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci  

**一句话要点**：提出联邦分割决策变换器以解决移动边缘计算中异构环境下的元界资源分配问题。

**关键词**：联邦学习, 离线强化学习, 变换器模型, 移动边缘计算, 元界资源分配

## 3 点简述
- 核心问题：移动边缘计算中，传统联邦学习在异构多无线接入技术环境下性能下降，且传输全模型参数负担重。
- 方法要点：采用离线强化学习框架，将变换器模型分割为本地代理特定组件和云端共享全局层，实现本地适应与协同训练。
- 实验或效果：在异构环境中提升体验质量达10%，并将近98%的模型参数卸载到云端，减轻边缘服务器计算负担。

## 摘要（原文）

> Mobile edge computing (MEC) based wireless metaverse services offer an untethered, immersive experience to users, where the superior quality of experience (QoE) needs to be achieved under stringent latency constraints and visual quality demands. To achieve this, MEC-based intelligent resource allocation for virtual reality users needs to be supported by coordination across MEC servers to harness distributed data. Federated learning (FL) is a promising solution, and can be combined with reinforcement learning (RL) to develop generalized policies across MEC-servers. However, conventional FL incurs transmitting the full model parameters across the MEC-servers and the cloud, and suffer performance degradation due to naive global aggregation, especially in heterogeneous multi-radio access technology environments. To address these challenges, this paper proposes Federated Split Decision Transformer (FSDT), an offline RL framework where the transformer model is partitioned between MEC servers and the cloud. Agent-specific components (e.g., MEC-based embedding and prediction layers) enable local adaptability, while shared global layers in the cloud facilitate cooperative training across MEC servers. Experimental results demonstrate that FSDT enhances QoE for up to 10% in heterogeneous environments compared to baselines, while offloadingnearly 98% of the transformer model parameters to the cloud, thereby reducing the computational burden on MEC servers.

