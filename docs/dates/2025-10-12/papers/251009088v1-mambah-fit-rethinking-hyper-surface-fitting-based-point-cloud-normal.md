---
layout: default
title: MambaH-Fit: Rethinking Hyper-surface Fitting-based Point Cloud Normal Estimation via State Space Modelling
---

# MambaH-Fit: Rethinking Hyper-surface Fitting-based Point Cloud Normal Estimation via State Space Modelling
**arXiv**：[2510.09088v1](https://arxiv.org/abs/2510.09088) · [PDF](https://arxiv.org/pdf/2510.09088.pdf)  
**作者**：Weijia Wang, Yuanzhi Su, Pei-Gen Ye, Yuan-Gen Wang, Xuequan Lu  
**一句话要点**：提出MambaH-Fit框架，通过状态空间建模改进点云法向量估计的精细几何结构建模。

**关键词**：点云法向量估计, 状态空间模型, 超曲面拟合, 注意力机制, 多尺度特征融合

## 3 点简述
- 现有方法在建模点云精细几何结构方面不足，影响法向量估计精度。
- 引入注意力驱动层次特征融合和补丁状态空间模型，增强局部几何上下文学习。
- 在基准数据集上实验显示，方法在准确性、鲁棒性和灵活性方面优于现有方法。

## 摘要（原文）

> We present MambaH-Fit, a state space modelling framework tailored for
> hyper-surface fitting-based point cloud normal estimation. Existing normal
> estimation methods often fall short in modelling fine-grained geometric
> structures, thereby limiting the accuracy of the predicted normals. Recently,
> state space models (SSMs), particularly Mamba, have demonstrated strong
> modelling capability by capturing long-range dependencies with linear
> complexity and inspired adaptations to point cloud processing. However,
> existing Mamba-based approaches primarily focus on understanding global shape
> structures, leaving the modelling of local, fine-grained geometric details
> largely under-explored. To address the issues above, we first introduce an
> Attention-driven Hierarchical Feature Fusion (AHFF) scheme to adaptively fuse
> multi-scale point cloud patch features, significantly enhancing geometric
> context learning in local point cloud neighbourhoods. Building upon this, we
> further propose Patch-wise State Space Model (PSSM) that models point cloud
> patches as implicit hyper-surfaces via state dynamics, enabling effective
> fine-grained geometric understanding for normal prediction. Extensive
> experiments on benchmark datasets show that our method outperforms existing
> ones in terms of accuracy, robustness, and flexibility. Ablation studies
> further validate the contribution of the proposed components.

