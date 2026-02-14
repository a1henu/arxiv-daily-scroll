---
layout: default
title: From Path Signatures to Sequential Modeling: Incremental Signature Contributions for Offline RL
---

# From Path Signatures to Sequential Modeling: Incremental Signature Contributions for Offline RL
**arXiv**：[2602.11805v1](https://arxiv.org/abs/2602.11805) · [PDF](https://arxiv.org/pdf/2602.11805.pdf)  
**作者**：Ziyi Zhao, Qingchuan Li, Yuxuan Xu  

**一句话要点**：提出增量签名贡献方法，将路径签名分解为时序序列，以增强离线强化学习中的步态反应性。

**关键词**：路径签名, 离线强化学习, 时序建模, Transformer架构, 控制任务

## 3 点简述
- 路径签名作为轨迹的通用表示，但标准形式将时间结构压缩为全局对象，限制了在决策问题中的步态反应性。
- 提出增量签名贡献方法，将截断路径签名分解为张量代数空间中的时序序列，保留代数结构并显式化时间演化。
- 基于此表示构建ISCT模型，在HalfCheetah等环境中评估，显示对时间敏感控制任务的有效性。

## 摘要（原文）

> Path signatures embed trajectories into tensor algebra and constitute a universal, non-parametric representation of paths; however, in the standard form, they collapse temporal structure into a single global object, which limits their suitability for decision-making problems that require step-wise reactivity. We propose the Incremental Signature Contribution (ISC) method, which decomposes truncated path signatures into a temporally ordered sequence of elements in the tensor-algebra space, corresponding to incremental contributions induced by last path increments. This reconstruction preserves the algebraic structure and expressivity of signatures, while making their internal temporal evolution explicit, enabling processing signature-based representations via sequential modeling approaches. In contrast to full signatures, ISC is inherently sensitive to instantaneous trajectory updates, which is critical for sensitive and stability-requiring control dynamics. Building on this representation, we introduce ISC-Transformer (ISCT), an offline reinforcement learning model that integrates ISC into a standard Transformer architecture without further architectural modification. We evaluate ISCT on HalfCheetah, Walker2d, Hopper, and Maze2d, including settings with delayed rewards and downgraded datasets. The results demonstrate that ISC method provides a theoretically grounded and practically effective alternative to path processing for temporally sensitive control tasks.

