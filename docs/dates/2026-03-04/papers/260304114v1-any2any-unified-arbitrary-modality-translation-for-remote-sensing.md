---
layout: default
title: Any2Any: Unified Arbitrary Modality Translation for Remote Sensing
---

# Any2Any: Unified Arbitrary Modality Translation for Remote Sensing
**arXiv**：[2603.04114v1](https://arxiv.org/abs/2603.04114) · [PDF](https://arxiv.org/pdf/2603.04114.pdf)  
**作者**：Haoyang Chen, Jing Zhang, Hebaixu Wang, Shiqin Wang, Pohsun Huang, Jiayuan Li, Haonan Guo, Di Wang, Zheng Wang, Bo Du  

**一句话要点**：提出Any2Any统一潜在扩散框架，解决遥感多模态翻译中模态组合泛化问题。

**关键词**：遥感多模态翻译, 潜在扩散模型, 零样本泛化, 几何对齐潜在空间, 残差适配器

## 3 点简述
- 核心问题：现有跨模态翻译方法独立处理每对模态，导致二次复杂度且难以泛化到未见模态组合。
- 方法要点：基于共享潜在表示，通过几何对齐潜在空间和轻量残差适配器，实现任意模态间的统一翻译。
- 实验或效果：在14个翻译任务中优于成对方法，并展示对未见模态对的强零样本泛化能力。

## 摘要（原文）

> Multi-modal remote sensing imagery provides complementary observations of the same geographic scene, yet such observations are frequently incomplete in practice. Existing cross-modal translation methods treat each modality pair as an independent task, resulting in quadratic complexity and limited generalization to unseen modality combinations. We formulate Any-to-Any translation as inference over a shared latent representation of the scene, where different modalities correspond to partial observations of the same underlying semantics. Based on this formulation, we propose Any2Any, a unified latent diffusion framework that projects heterogeneous inputs into a geometrically aligned latent space. Such structure performs anchored latent regression with a shared backbone, decoupling modality-specific representation learning from semantic mapping. Moreover, lightweight target-specific residual adapters are used to correct systematic latent mismatches without increasing inference complexity. To support learning under sparse but connected supervision, we introduce RST-1M, the first million-scale remote sensing dataset with paired observations across five sensing modalities, providing supervision anchors for any-to-any translation. Experiments across 14 translation tasks show that Any2Any consistently outperforms pairwise translation methods and exhibits strong zero-shot generalization to unseen modality pairs. Code and models will be available at https://github.com/MiliLab/Any2Any.

