---
layout: default
title: Explainable Pathomics Feature Visualization via Correlation-aware Conditional Feature Editing
---

# Explainable Pathomics Feature Visualization via Correlation-aware Conditional Feature Editing
**arXiv**：[2602.05397v1](https://arxiv.org/abs/2602.05397) · [PDF](https://arxiv.org/pdf/2602.05397.pdf)  
**作者**：Yuechen Yang, Junlin Guo, Ruining Deng, Junchao Zhu, Zhengyi Lu, Chongyu Qu, Yanfan Zhu, Xingyi Guo, Yu Wang, Shilin Zhao, Haichun Yang, Yuankai Huo  

**一句话要点**：提出流形感知扩散框架以解决病理组学特征编辑中的相关性忽略问题

**关键词**：病理组学, 特征编辑, 扩散模型, 变分自编码器, 生物流形, 数字病理

## 3 点简述
- 核心问题：病理组学特征内在相关，传统条件扩散模型假设特征独立，导致编辑时产生不真实伪影。
- 方法要点：使用变分自编码器学习解耦潜在空间，正则化特征轨迹，确保编辑时保持生物流形内的分布。
- 实验或效果：在条件特征编辑任务中优于基线方法，能导航特征流形并保持结构一致性。

## 摘要（原文）

> Pathomics is a recent approach that offers rich quantitative features beyond what black-box deep learning can provide, supporting more reproducible and explainable biomarkers in digital pathology. However, many derived features (e.g., "second-order moment") remain difficult to interpret, especially across different clinical contexts, which limits their practical adoption. Conditional diffusion models show promise for explainability through feature editing, but they typically assume feature independence**--**an assumption violated by intrinsically correlated pathomics features. Consequently, editing one feature while fixing others can push the model off the biological manifold and produce unrealistic artifacts. To address this, we propose a Manifold-Aware Diffusion (MAD) framework for controllable and biologically plausible cell nuclei editing. Unlike existing approaches, our method regularizes feature trajectories within a disentangled latent space learned by a variational auto-encoder (VAE). This ensures that manipulating a target feature automatically adjusts correlated attributes to remain within the learned distribution of real cells. These optimized features then guide a conditional diffusion model to synthesize high-fidelity images. Experiments demonstrate that our approach is able to navigate the manifold of pathomics features when editing those features. The proposed method outperforms baseline methods in conditional feature editing while preserving structural coherence.

