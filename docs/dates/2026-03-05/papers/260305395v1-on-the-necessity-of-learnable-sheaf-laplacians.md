---
layout: default
title: On the Necessity of Learnable Sheaf Laplacians
---

# On the Necessity of Learnable Sheaf Laplacians
**arXiv**：[2603.05395v1](https://arxiv.org/abs/2603.05395) · [PDF](https://arxiv.org/pdf/2603.05395.pdf)  
**作者**：Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga, Pietro Liò  

**一句话要点**：提出身份层束网络基线，质疑异质图学习中可学习层束拉普拉斯的必要性

**关键词**：层束神经网络, 异质图学习, 过平滑问题, 身份层束网络, 消融实验, 拉普拉斯算子

## 3 点简述
- 核心问题：层束神经网络通过可学习限制映射缓解异质图过平滑，但复杂性是否必要？
- 方法要点：引入身份层束网络基线，固定限制映射为恒等映射，进行消融实验比较。
- 实验或效果：在五个异质图基准上，身份基线性能与多种层束神经网络变体相当，过平滑未显著增加。

## 摘要（原文）

> Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

