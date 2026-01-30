---
layout: default
title: Rethinking Federated Graph Foundation Models: A Graph-Language Alignment-based Approach
---

# Rethinking Federated Graph Foundation Models: A Graph-Language Alignment-based Approach
**arXiv**：[2601.21369v1](https://arxiv.org/abs/2601.21369) · [PDF](https://arxiv.org/pdf/2601.21369.pdf)  
**作者**：Yinlin Zhu, Di Wu, Xianzhi Zhang, Yuming Ai, Xunkai Li, Miao Hu, Guocong Quan  

**一句话要点**：提出FedGALA框架，通过图-语言对齐解决联邦图基础模型中的语义结构正交性与完整性挑战。

**关键词**：联邦学习, 图神经网络, 预训练语言模型, 对比学习, 提示调优, 知识对齐

## 3 点简述
- 核心问题：现有联邦图基础模型在量化过程中存在不可逆知识损失，且需处理数据异构性和通信限制。
- 方法要点：采用无监督对比学习在连续嵌入空间对齐图神经网络与冻结预训练语言模型，并结合高效提示调优机制。
- 实验或效果：在多领域数据集上优于基线，性能提升最高达14.37%，验证了框架的有效性。

## 摘要（原文）

> Recent studies of federated graph foundational models (FedGFMs) break the idealized and untenable assumption of having centralized data storage to train graph foundation models, and accommodate the reality of distributed, privacy-restricted data silos. Despite their simplicity and intuition, existing studies that project aligned generalizable knowledge onto a discrete token space via vector-quantized backbones suffer from irreversible knowledge loss during the quantization process. In this context, we argue that reconciling the semantic-structural orthogonality and integrity between pre-trained language models (PLMs) and graph neural networks (GNNs) is paramount for developing effective FedGFMs while simultaneously mitigating the severe data heterogeneity and communication constraints inherent in distributed, resource-limited environments.
>   To address these issues, we propose FedGALA (Federated Graph And Language Alignment), a framework that resolves graph-based semantic-structural orthogonality and integrity in federated settings by employing unsupervised contrastive learning to align GNNs and frozen PLMs within a continuous embedding space, thereby capturing robust, transferable general knowledge. Subsequently, FedGALA leverages a communication-efficient prompt tuning mechanism to steer these pre-aligned encoders and frozen PLMs, facilitating effective adaptation to diverse downstream tasks while circumventing the prohibitive overhead of full-parameter fine-tuning. The comprehensive experiments validate that FedGALA outperforms all competitive baselines across multi-domain datasets on multiple tasks with up to 14.37% performance improvement.

