---
layout: default
title: SDFed: Bridging Local Global Discrepancy via Subspace Refinement and Divergence Control in Federated Prompt Learning
---

# SDFed: Bridging Local Global Discrepancy via Subspace Refinement and Divergence Control in Federated Prompt Learning
**arXiv**：[2602.08590v1](https://arxiv.org/abs/2602.08590) · [PDF](https://arxiv.org/pdf/2602.08590.pdf)  
**作者**：Yicheng Di, Wei Yuan, Tieke He, Zhanjie Zhang, Ao Ma, Yuan Liu, Hongzhi Yin  

**一句话要点**：提出SDFed框架，通过子空间细化和差异控制解决异构联邦提示学习中的本地-全局差异问题。

**关键词**：联邦学习, 提示学习, 异构客户端, 视觉语言模型, 本地-全局差异

## 3 点简述
- 核心问题：异构联邦提示学习中，统一提示结构无法适应客户端数据分布和资源差异，导致本地与全局知识冲突。
- 方法要点：SDFed允许变长本地提示匹配客户端特性，通过子空间细化和差异控制策略减少冲突并促进知识转移。
- 实验或效果：在多个数据集上验证，SDFed在异构联邦设置中提升了性能和鲁棒性。

## 摘要（原文）

> Vision-language pretrained models offer strong transferable representations, yet adapting them in privacy-sensitive multi-party settings is challenging due to the high communication cost of federated optimization and the limited local data on clients. Federated prompt learning mitigates this issue by keeping the VLPM backbone frozen and collaboratively training lightweight prompt parameters. However, existing approaches typically enforce a unified prompt structure and length across clients, which is inadequate under practical client heterogeneity in both data distributions and system resources, and may further introduce conflicts between globally shared and locally optimal knowledge. To address these challenges, we propose \textbf{SDFed}, a heterogeneous federated prompt learning framework that bridges Local-Global Discrepancy via Subspace Refinement and Divergence Control. SDFed maintains a fixed-length global prompt for efficient aggregation while allowing each client to learn a variable-length local prompt to better match its data characteristics and capacity. To mitigate local-global conflicts and facilitate effective knowledge transfer, SDFed introduces a subspace refinement method for local prompts and an information retention and divergence control strategy that preserves key local information while maintaining appropriate separability between global and local representations. Extensive experiments on several datasets demonstrate that SDFed consistently improves performance and robustness in heterogeneous federated settings.

