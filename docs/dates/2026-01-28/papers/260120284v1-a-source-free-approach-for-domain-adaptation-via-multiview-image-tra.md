---
layout: default
title: A Source-Free Approach for Domain Adaptation via Multiview Image Transformation and Latent Space Consistency
---

# A Source-Free Approach for Domain Adaptation via Multiview Image Transformation and Latent Space Consistency
**arXiv**：[2601.20284v1](https://arxiv.org/abs/2601.20284) · [PDF](https://arxiv.org/pdf/2601.20284.pdf)  
**作者**：Debopom Sutradhar, Md. Abdur Rahman, Mohaimenul Azam Khan Raiaan, Reem E. Mohamed, Sami Azam  

**一句话要点**：提出基于多视图图像变换与潜在空间一致性的源自由域适应方法，以解决目标域数据分布差异问题。

**关键词**：源自由域适应, 多视图增强, 潜在空间一致性, ConvNeXt编码器, 分类损失, 目标域学习

## 3 点简述
- 核心问题：域适应中源域数据访问、对抗训练或复杂伪标签技术导致计算成本高。
- 方法要点：通过多视图增强和潜在空间一致性，直接从目标域学习域不变特征，无需源-目标对齐。
- 实验或效果：在Office-31、Office-Home和Office-Caltech数据集上平均准确率分别达90.72%、84%和97.12%。

## 摘要（原文）

> Domain adaptation (DA) addresses the challenge of transferring knowledge from a source domain to a target domain where image data distributions may differ. Existing DA methods often require access to source domain data, adversarial training, or complex pseudo-labeling techniques, which are computationally expensive. To address these challenges, this paper introduces a novel source-free domain adaptation method. It is the first approach to use multiview augmentation and latent space consistency techniques to learn domain-invariant features directly from the target domain. Our method eliminates the need for source-target alignment or pseudo-label refinement by learning transferable representations solely from the target domain by enforcing consistency between multiple augmented views in the latent space. Additionally, the method ensures consistency in the learned features by generating multiple augmented views of target domain data and minimizing the distance between their feature representations in the latent space. We also introduce a ConvNeXt-based encoder and design a loss function that combines classification and consistency objectives to drive effective adaptation directly from the target domain. The proposed model achieves an average classification accuracy of 90. 72\%, 84\%, and 97. 12\% in Office-31, Office-Home and Office-Caltech datasets, respectively. Further evaluations confirm that our study improves existing methods by an average classification accuracy increment of +1.23\%, +7.26\%, and +1.77\% on the respective datasets.

