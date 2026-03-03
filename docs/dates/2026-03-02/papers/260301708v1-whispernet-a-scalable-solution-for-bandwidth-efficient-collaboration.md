---
layout: default
title: WhisperNet: A Scalable Solution for Bandwidth-Efficient Collaboration
---

# WhisperNet: A Scalable Solution for Bandwidth-Efficient Collaboration
**arXiv**：[2603.01708v1](https://arxiv.org/abs/2603.01708) · [PDF](https://arxiv.org/pdf/2603.01708.pdf)  
**作者**：Gong Chen, Chaokun Zhang, Xinyan Zhao  

**一句话要点**：提出WhisperNet以解决自动驾驶中带宽受限的协作感知问题

**关键词**：协作感知, 带宽效率, 自动驾驶, 特征选择, 全局协调, 接收者中心

## 3 点简述
- 核心问题：现有协作感知方法在带宽限制下，固定压缩或空间选择牺牲全局上下文，影响场景理解。
- 方法要点：采用接收者中心范式，通过轻量显著性元数据和全局请求计划动态分配特征，结合协作特征路由确保一致性。
- 实验或效果：在OPV2V数据集上AP@0.7提升2.4%，通信成本仅0.5%，作为即插即用组件在5%带宽下增强基线并保持鲁棒性。

## 摘要（原文）

> Collaborative perception is vital for autonomous driving yet remains constrained by tight communication budgets. Earlier work reduced bandwidth by compressing full feature maps with fixed-rate encoders, which adapts poorly to a changing environment, and it further evolved into spatial selection methods that improve efficiency by focusing on salient regions, but this object-centric approach often sacrifices global context, weakening holistic scene understanding. To overcome these limitations, we introduce \textit{WhisperNet}, a bandwidth-aware framework that proposes a novel, receiver-centric paradigm for global coordination across agents. Senders generate lightweight saliency metadata, while the receiver formulates a global request plan that dynamically budgets feature contributions across agents and features, retrieving only the most informative features. A collaborative feature routing module then aligns related messages before fusion to ensure structural consistency. Extensive experiments show that WhisperNet achieves state-of-the-art performance, improving AP@0.7 on OPV2V by 2.4\% with only 0.5\% of the communication cost. As a plug-and-play component, it boosts strong baselines with merely 5\% of full bandwidth while maintaining robustness under localization noise. These results demonstrate that globally-coordinated allocation across \textit{what} and \textit{where} to share is the key to achieving efficient collaborative perception.

