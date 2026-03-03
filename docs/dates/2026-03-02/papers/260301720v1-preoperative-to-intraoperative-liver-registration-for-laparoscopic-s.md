---
layout: default
title: Preoperative-to-intraoperative Liver Registration for Laparoscopic Surgery via Latent-Grounded Correspondence Constraints
---

# Preoperative-to-intraoperative Liver Registration for Laparoscopic Surgery via Latent-Grounded Correspondence Constraints
**arXiv**：[2603.01720v1](https://arxiv.org/abs/2603.01720) · [PDF](https://arxiv.org/pdf/2603.01720.pdf)  
**作者**：Ruize Cui, Jialun Pei, Haiqiao Wang, Jun Zhou, Jeremy Yuen-Chun Teoh, Pheng-Ann Heng, Jing Qin  

**一句话要点**：提出Land-Reg框架，通过潜在基础对应约束解决腹腔镜肝手术中术前到术中2D-3D配准问题。

**关键词**：腹腔镜肝手术配准, 2D-3D对应学习, 可变形配准, 潜在空间对齐, 地标检测, 增强现实

## 3 点简述
- 核心问题：现有配准方法缺乏基于潜在证据的可靠2D-3D几何对应建模，导致可解释性差和临床对齐不稳定。
- 方法要点：引入对应驱动的可变形配准框架，学习潜在基础2D-3D地标对应作为中间表示，包括跨模态潜在对齐和不确定性增强重叠地标检测器。
- 实验或效果：在P2ILF数据集上验证了方法在刚性姿态估计和非刚性变形上的优越性，代码将开源。

## 摘要（原文）

> In laparoscopic liver surgery, augmented reality technology enhances intraoperative anatomical guidance by overlaying 3D liver models from preoperative CT/MRI onto laparoscopic 2D views. However, existing registration methods lack explicit modeling of reliable 2D-3D geometric correspondences supported by latent evidence, leading to limited interpretability and potentially unstable alignment in clinical scenarios. In this work, we introduce Land-Reg, a correspondence-driven deformable registration framework that explicitly learns latent-grounded 2D-3D landmark correspondences as an interpretable intermediate representation to bridge cross-modal alignment. For rigid registration, Land-Reg embraces a Cross-modal Latent Alignment module to map multi-modal features into a unified latent space. Further, an Uncertainty-enhanced Overlap Landmark Detector with similarity matching is proposed to robustly estimate explicit 2D-3D landmark correspondences. For non-rigid registration, we design a novel shape-constrained supervision strategy that anchors shape deformation to matched landmarks through reprojection consistency and incorporates local-isometric regularization to alleviate inherent 2D-3D depth ambiguity, while a rendered-mask alignment enforces global shape consistency. Experimental results on the P2ILF dataset demonstrate the superiority of our method on both rigid pose estimation and non-rigid deformation. Our code will be available at https://github.com/cuiruize/Land-Reg.

