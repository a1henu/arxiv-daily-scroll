---
layout: default
title: Dual-Stream Cross-Modal Representation Learning via Residual Semantic Decorrelation
---

# Dual-Stream Cross-Modal Representation Learning via Residual Semantic Decorrelation
**arXiv**：[2512.07568v1](https://arxiv.org/abs/2512.07568) · [PDF](https://arxiv.org/pdf/2512.07568.pdf)  
**作者**：Xuecheng Li, Weikuan Jia, Alisher Kurbonaliev, Qurbonaliev Alisher, Khudzhamkulov Rustam, Ismoilov Shuhratjon, Eshmatov Javhariddin, Yuanjie Zheng  

**一句话要点**：提出双流残差语义去相关网络以解决跨模态学习中模态主导和冗余耦合问题

**关键词**：跨模态学习, 残差分解, 语义去相关, 双流网络, 模态解耦, 教育预测

## 3 点简述
- 核心问题：跨模态学习存在模态主导、冗余信息耦合和虚假相关性，影响泛化和可解释性
- 方法要点：通过残差分解和语义去相关约束，分离模态特定与共享信息，并正则化共享空间
- 实验或效果：在两个大规模教育基准上，优于单模态、早期融合、晚期融合和协同注意力基线

## 摘要（原文）

> Cross-modal learning has become a fundamental paradigm for integrating heterogeneous information sources such as images, text, and structured attributes. However, multimodal representations often suffer from modality dominance, redundant information coupling, and spurious cross-modal correlations, leading to suboptimal generalization and limited interpretability. In particular, high-variance modalities tend to overshadow weaker but semantically important signals, while naïve fusion strategies entangle modality-shared and modality-specific factors in an uncontrolled manner. This makes it difficult to understand which modality actually drives a prediction and to maintain robustness when some modalities are noisy or missing. To address these challenges, we propose a Dual-Stream Residual Semantic Decorrelation Network (DSRSD-Net), a simple yet effective framework that disentangles modality-specific and modality-shared information through residual decomposition and explicit semantic decorrelation constraints. DSRSD-Net introduces: (1) a dual-stream representation learning module that separates intra-modal (private) and inter-modal (shared) latent factors via residual projection; (2) a residual semantic alignment head that maps shared factors from different modalities into a common space using a combination of contrastive and regression-style objectives; and (3) a decorrelation and orthogonality loss that regularizes the covariance structure of the shared space while enforcing orthogonality between shared and private streams, thereby suppressing cross-modal redundancy and preventing feature collapse. Experimental results on two large-scale educational benchmarks demonstrate that DSRSD-Net consistently improves next-step prediction and final outcome prediction over strong single-modality, early-fusion, late-fusion, and co-attention baselines.

