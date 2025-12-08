---
layout: default
title: ParaUni: Enhance Generation in Unified Multimodal Model with Reinforcement-driven Hierarchical Parallel Information Interaction
---

# ParaUni: Enhance Generation in Unified Multimodal Model with Reinforcement-driven Hierarchical Parallel Information Interaction
**arXiv**：[2512.05422v1](https://arxiv.org/abs/2512.05422) · [PDF](https://arxiv.org/pdf/2512.05422.pdf)  
**作者**：Jiangtong Tan, Lin Liu, Jie Huanng, Xiaopeng Zhang, Qi Tian, Feng Zhao  

**一句话要点**：提出ParaUni以增强统一多模态模型中的生成能力，通过并行信息交互和强化学习层级调整。

**关键词**：统一多模态模型, 视觉生成, 并行特征提取, 强化学习, 层级信息交互, 扩散模型

## 3 点简述
- 现有方法难以平衡视觉语言模型与扩散模型间的充分交互与灵活实现。
- ParaUni并行提取视觉语言模型各层特征，通过层集成模块融合细节与语义信息。
- 实验表明ParaUni利用多层互补特征显著提升生成质量，并在强化学习阶段展现多奖励优化潜力。

## 摘要（原文）

> Unified multimodal models significantly improve visual generation by combining vision-language models (VLMs) with diffusion models. However, existing methods struggle to fully balance sufficient interaction and flexible implementation due to vast representation difference. Considering abundant and hierarchical information in VLM's layers from low-level details to high-level semantics, we propose \textbf{ParaUni}. It extracts features from variants VLM's layers in a \textbf{Para}llel way for comprehensive information interaction and retains a flexible separation architecture to enhance generation in \textbf{Uni}fied multimodal model. Concretely, visual features from all VLM's layers are fed in parallel into a Layer Integration Module (LIM), which efficiently integrates fine-grained details and semantic abstractions and provides the fused representation as a condition to the diffusion model. To further enhance performance, we reveal that these hierarchical layers respond unequally to different rewards in Reinforcement Learning (RL). Crucially, we design a Layer-wise Dynamic Adjustment Mechanism (LDAM) to facilitate multiple reward improvements that aligns the hierarchical properties of these layers using RL. Extensive experiments show ParaUni leverages complementary multi-layer features to substantially improve generation quality and shows strong potential for multiple reward advances during RL stages. Code is available at https://github.com/JosephTiTan/ParaUni.

