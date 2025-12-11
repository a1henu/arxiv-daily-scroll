---
layout: default
title: PathCo-LatticE: Pathology-Constrained Lattice-Of Experts Framework for Fully-supervised Few-Shot Cardiac MRI Segmentation
---

# PathCo-LatticE: Pathology-Constrained Lattice-Of Experts Framework for Fully-supervised Few-Shot Cardiac MRI Segmentation
**arXiv**：[2512.09779v1](https://arxiv.org/abs/2512.09779) · [PDF](https://arxiv.org/pdf/2512.09779.pdf)  
**作者**：Mohamed Elbayumi, Mohammed S. M. Elbaz  

**一句话要点**：提出PathCo-LatticE框架，通过病理约束合成监督解决全监督少样本心脏MRI分割的泛化问题。

**关键词**：少样本学习, 心脏MRI分割, 病理约束合成, 零样本泛化, 动态专家网络

## 3 点简述
- 核心问题：少样本学习依赖半监督方法，对领域偏移敏感，限制零样本泛化能力。
- 方法要点：使用虚拟患者引擎合成病理引导的标签数据，结合自增强交错验证和动态专家网络提升泛化。
- 实验或效果：在严格分布外设置下，仅用少量锚点实现优于现有方法的性能，接近全监督水平。

## 摘要（原文）

> Few-shot learning (FSL) mitigates data scarcity in cardiac MRI segmentation but typically relies on semi-supervised techniques sensitive to domain shifts and validation bias, restricting zero-shot generalizability. We propose PathCo-LatticE, a fully supervised FSL framework that replaces unlabeled data with pathology-guided synthetic supervision. First, our Virtual Patient Engine models continuous latent disease trajectories from sparse clinical anchors, using generative modeling to synthesize physiologically plausible, fully labeled 3D cohorts. Second, Self-Reinforcing Interleaved Validation (SIV) provides a leakage-free protocol that evaluates models online with progressively challenging synthetic samples, eliminating the need for real validation data. Finally, a dynamic Lattice-of-Experts (LoE) organizes specialized networks within a pathology-aware topology and activates the most relevant experts per input, enabling robust zero-shot generalization to unseen data without target-domain fine-tuning. We evaluated PathCo-LatticE in a strict out-of-distribution (OOD) setting, deriving all anchors and severity statistics from a single-source domain (ACDC) and performing zero-shot testing on the multi-center, multi-vendor M&Ms dataset. PathCo-LatticE outperforms four state-of-the-art FSL methods by 4.2-11% Dice starting from only 7 labeled anchors, and approaches fully supervised performance (within 1% Dice) with only 19 labeled anchors. The method shows superior harmonization across four vendors and generalization to unseen pathologies. [Code will be made publicly available].

