---
layout: default
title: HINT: Hierarchical Interaction Modeling for Autoregressive Multi-Human Motion Generation
---

# HINT: Hierarchical Interaction Modeling for Autoregressive Multi-Human Motion Generation
**arXiv**：[2601.20383v1](https://arxiv.org/abs/2601.20383) · [PDF](https://arxiv.org/pdf/2601.20383.pdf)  
**作者**：Mengge Liu, Yan Di, Gu Wang, Yun Qu, Dekai Zhu, Yanyan Li, Xiangyang Ji  

**一句话要点**：提出HINT框架，通过分层交互建模实现自回归多人体运动生成

**关键词**：多人体运动生成, 自回归建模, 分层交互, 扩散模型, 滑动窗口策略

## 3 点简述
- 核心问题：现有离线方法难以处理长文本、变长序列和变人数量的多人体交互运动生成
- 方法要点：在扩散模型中引入解耦运动表示和滑动窗口策略，分层建模局部交互与全局一致性
- 实验或效果：在InterHuman基准上FID达3.100，优于离线模型和自回归基线

## 摘要（原文）

> Text-driven multi-human motion generation with complex interactions remains a challenging problem. Despite progress in performance, existing offline methods that generate fixed-length motions with a fixed number of agents, are inherently limited in handling long or variable text, and varying agent counts. These limitations naturally encourage autoregressive formulations, which predict future motions step by step conditioned on all past trajectories and current text guidance. In this work, we introduce HINT, the first autoregressive framework for multi-human motion generation with Hierarchical INTeraction modeling in diffusion. First, HINT leverages a disentangled motion representation within a canonicalized latent space, decoupling local motion semantics from inter-person interactions. This design facilitates direct adaptation to varying numbers of human participants without requiring additional refinement. Second, HINT adopts a sliding-window strategy for efficient online generation, and aggregates local within-window and global cross-window conditions to capture past human history, inter-person dependencies, and align with text guidance. This strategy not only enables fine-grained interaction modeling within each window but also preserves long-horizon coherence across all the long sequence. Extensive experiments on public benchmarks demonstrate that HINT matches the performance of strong offline models and surpasses autoregressive baselines. Notably, on InterHuman, HINT achieves an FID of 3.100, significantly improving over the previous state-of-the-art score of 5.154.

