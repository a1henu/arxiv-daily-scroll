---
layout: default
title: Know Thyself by Knowing Others: Learning Neuron Identity from Population Context
---

# Know Thyself by Knowing Others: Learning Neuron Identity from Population Context
**arXiv**：[2512.01199v1](https://arxiv.org/abs/2512.01199) · [PDF](https://arxiv.org/pdf/2512.01199.pdf)  
**作者**：Vinam Arora, Divyansha Lachi, Ian J. Knight, Mehdi Azabou, Blake Richards, Cole L. Hurwitz, Josh Siegle, Eva L. Dyer  

**一句话要点**：提出NuCLR框架，通过自监督学习从神经活动中推断神经元身份信息。

**关键词**：神经元身份解码, 自监督学习, 对比学习, 时空Transformer, 零样本泛化, 神经表示学习

## 3 点简述
- 核心问题：从神经活动推断神经元类型、连接和脑区等身份信息具有挑战性。
- 方法要点：使用对比学习整合不同时间和刺激下的神经元视图，并构建置换等变时空Transformer。
- 实验或效果：在多个数据集上实现细胞类型和脑区解码的新SOTA，并展示零样本泛化能力。

## 摘要（原文）

> Neurons process information in ways that depend on their cell type, connectivity, and the brain region in which they are embedded. However, inferring these factors from neural activity remains a significant challenge. To build general-purpose representations that allow for resolving information about a neuron's identity, we introduce NuCLR, a self-supervised framework that aims to learn representations of neural activity that allow for differentiating one neuron from the rest. NuCLR brings together views of the same neuron observed at different times and across different stimuli and uses a contrastive objective to pull these representations together. To capture population context without assuming any fixed neuron ordering, we build a spatiotemporal transformer that integrates activity in a permutation-equivariant manner. Across multiple electrophysiology and calcium imaging datasets, a linear decoding evaluation on top of NuCLR representations achieves a new state-of-the-art for both cell type and brain region decoding tasks, and demonstrates strong zero-shot generalization to unseen animals. We present the first systematic scaling analysis for neuron-level representation learning, showing that increasing the number of animals used during pretraining consistently improves downstream performance. The learned representations are also label-efficient, requiring only a small fraction of labeled samples to achieve competitive performance. These results highlight how large, diverse neural datasets enable models to recover information about neuron identity that generalize across animals. Code is available at https://github.com/nerdslab/nuclr.

