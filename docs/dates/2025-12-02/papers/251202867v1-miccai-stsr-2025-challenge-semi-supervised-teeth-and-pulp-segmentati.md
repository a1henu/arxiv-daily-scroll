---
layout: default
title: MICCAI STSR 2025 Challenge: Semi-Supervised Teeth and Pulp Segmentation and CBCT-IOS Registration
---

# MICCAI STSR 2025 Challenge: Semi-Supervised Teeth and Pulp Segmentation and CBCT-IOS Registration
**arXiv**：[2512.02867v1](https://arxiv.org/abs/2512.02867) · [PDF](https://arxiv.org/pdf/2512.02867.pdf)  
**作者**：Yaqi Wang, Zhi Li, Chengyu Wu, Jun Liu, Yifan Zhang, Jialuo Chen, Jiaxue Ni, Qian Luo, Jin Liu, Can Han, Changkai Ji, Zhi Qin Tan, Ajo Babu George, Liangyu Chen, Qianni Zhang, Dahong Qian, Shuai Wang, Huiyu Zhou  

**一句话要点**：组织MICCAI STSR 2025挑战赛，推动半监督学习在牙齿与牙髓分割及CBCT-IOS配准中的应用

**关键词**：半监督学习, 牙齿分割, CBCT-IOS配准, 深度学习, 数字牙科, 开源数据集

## 3 点简述
- 核心问题：数字牙科中CBCT和IOS数据标注稀缺，限制自动化分割与跨模态配准发展
- 方法要点：挑战赛设半监督分割与配准任务，提供标注与未标注数据集，鼓励开源深度学习方案
- 实验或效果：分割任务中最佳方法Dice得分0.967，配准任务结合PointNetLK与几何增强实现精准对齐

## 摘要（原文）

> Cone-Beam Computed Tomography (CBCT) and Intraoral Scanning (IOS) are essential for digital dentistry, but annotated data scarcity limits automated solutions for pulp canal segmentation and cross-modal registration. To benchmark semi-supervised learning (SSL) in this domain, we organized the STSR 2025 Challenge at MICCAI 2025, featuring two tasks: (1) semi-supervised segmentation of teeth and pulp canals in CBCT, and (2) semi-supervised rigid registration of CBCT and IOS. We provided 60 labeled and 640 unlabeled IOS samples, plus 30 labeled and 250 unlabeled CBCT scans with varying resolutions and fields of view. The challenge attracted strong community participation, with top teams submitting open-source deep learning-based SSL solutions. For segmentation, leading methods used nnU-Net and Mamba-like State Space Models with pseudo-labeling and consistency regularization, achieving a Dice score of 0.967 and Instance Affinity of 0.738 on the hidden test set. For registration, effective approaches combined PointNetLK with differentiable SVD and geometric augmentation to handle modality gaps; hybrid neural-classical refinement enabled accurate alignment despite limited labels. All data and code are publicly available at https://github.com/ricoleehduu/STS-Challenge-2025 to ensure reproducibility.

