---
layout: default
title: Feature-Aware One-Shot Federated Learning via Hierarchical Token Sequences
---

# Feature-Aware One-Shot Federated Learning via Hierarchical Token Sequences
**arXiv**：[2601.03882v1](https://arxiv.org/abs/2601.03882) · [PDF](https://arxiv.org/pdf/2601.03882.pdf)  
**作者**：Shudong Liu, Hanwen Zhang, Xiuling Wang, Yuesheng Zhu, Guibo Luo  

**一句话要点**：提出FALCON框架，通过特征感知分层令牌序列和知识蒸馏增强单次联邦学习在非IID图像数据上的性能。

**关键词**：单次联邦学习, 非IID数据, 分层令牌序列, 知识蒸馏, 医疗成像, 多尺度语义

## 3 点简述
- 核心问题：单次联邦学习在非IID图像数据上性能不足，尤其在医疗成像等领域。
- 方法要点：使用预训练视觉编码器生成分层令牌序列，结合多尺度自回归变换器生成合成序列，并集成知识蒸馏。
- 实验或效果：在医疗和自然图像数据集上验证，平均准确率比最佳基线提升9.58%。

## 摘要（原文）

> One-shot federated learning (OSFL) reduces the communication cost and privacy risks of iterative federated learning by constructing a global model with a single round of communication. However, most existing methods struggle to achieve robust performance on real-world domains such as medical imaging, or are inefficient when handling non-IID (Independent and Identically Distributed) data. To address these limitations, we introduce FALCON, a framework that enhances the effectiveness of OSFL over non-IID image data. The core idea of FALCON is to leverage the feature-aware hierarchical token sequences generation and knowledge distillation into OSFL. First, each client leverages a pretrained visual encoder with hierarchical scale encoding to compress images into hierarchical token sequences, which capture multi-scale semantics. Second, a multi-scale autoregressive transformer generator is used to model the distribution of these token sequences and generate the synthetic sequences. Third, clients upload the synthetic sequences along with the local classifier trained on the real token sequences to the server. Finally, the server incorporates knowledge distillation into global training to reduce reliance on precise distribution modeling. Experiments on medical and natural image datasets validate the effectiveness of FALCON in diverse non-IID scenarios, outperforming the best OSFL baselines by 9.58% in average accuracy.

