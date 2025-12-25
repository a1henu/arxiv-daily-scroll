---
layout: default
title: A Turn Toward Better Alignment: Few-Shot Generative Adaptation with Equivariant Feature Rotation
---

# A Turn Toward Better Alignment: Few-Shot Generative Adaptation with Equivariant Feature Rotation
**arXiv**：[2512.21174v1](https://arxiv.org/abs/2512.21174) · [PDF](https://arxiv.org/pdf/2512.21174.pdf)  
**作者**：Chenghao Xu, Qi Liu, Jiexi Yan, Muli Yang, Cheng Deng  

**一句话要点**：提出等变特征旋转方法以解决少样本图像生成中的领域对齐问题

**关键词**：少样本图像生成, 领域自适应, 等变特征旋转, 生成模型, 李群变换, 知识迁移

## 3 点简述
- 核心问题：现有少样本图像生成方法因领域分布差异和样本稀缺，导致对齐约束过严或过松，影响生成质量。
- 方法要点：通过参数化李群自适应旋转特征，在等变代理空间中进行双层次对齐，保留结构信息并促进知识迁移。
- 实验或效果：在多个常用数据集上验证，显著提升目标领域的生成性能。

## 摘要（原文）

> Few-shot image generation aims to effectively adapt a source generative model to a target domain using very few training images. Most existing approaches introduce consistency constraints-typically through instance-level or distribution-level loss functions-to directly align the distribution patterns of source and target domains within their respective latent spaces. However, these strategies often fall short: overly strict constraints can amplify the negative effects of the domain gap, leading to distorted or uninformative content, while overly relaxed constraints may fail to leverage the source domain effectively. This limitation primarily stems from the inherent discrepancy in the underlying distribution structures of the source and target domains. The scarcity of target samples further compounds this issue by hindering accurate estimation of the target domain's distribution. To overcome these limitations, we propose Equivariant Feature Rotation (EFR), a novel adaptation strategy that aligns source and target domains at two complementary levels within a self-rotated proxy feature space. Specifically, we perform adaptive rotations within a parameterized Lie Group to transform both source and target features into an equivariant proxy space, where alignment is conducted. These learnable rotation matrices serve to bridge the domain gap by preserving intra-domain structural information without distortion, while the alignment optimization facilitates effective knowledge transfer from the source to the target domain. Comprehensive experiments on a variety of commonly used datasets demonstrate that our method significantly enhances the generative performance within the targeted domain.

