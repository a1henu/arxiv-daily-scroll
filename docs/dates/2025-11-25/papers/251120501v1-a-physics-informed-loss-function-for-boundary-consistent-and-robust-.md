---
layout: default
title: A Physics-Informed Loss Function for Boundary-Consistent and Robust Artery Segmentation in DSA Sequences
---

# A Physics-Informed Loss Function for Boundary-Consistent and Robust Artery Segmentation in DSA Sequences
**arXiv**：[2511.20501v1](https://arxiv.org/abs/2511.20501) · [PDF](https://arxiv.org/pdf/2511.20501.pdf)  
**作者**：Muhammad Irfan, Nasir Rahim, Khalid Mahmood Malik  

**一句话要点**：提出物理信息损失函数以解决DSA序列中动脉分割的边界一致性和鲁棒性问题

**关键词**：动脉分割, 物理信息损失, 边界一致性, DSA序列, 深度学习, 血管几何

## 3 点简述
- 传统损失函数依赖像素重叠，忽略血管边界的几何和物理一致性，导致分割结果不稳定
- 引入基于位错理论的物理正则化项，强制平滑轮廓演化，提升对精细血管几何的捕捉能力
- 在多个分割架构和公共数据集上验证，优于交叉熵、Dice等损失，提高敏感性和边界一致性

## 摘要（原文）

> Accurate extraction and segmentation of the cerebral arteries from digital subtraction angiography (DSA) sequences is essential for developing reliable clinical management models of complex cerebrovascular diseases. Conventional loss functions often rely solely on pixel-wise overlap, overlooking the geometric and physical consistency of vascular boundaries, which can lead to fragmented or unstable vessel predictions. To overcome this limitation, we propose a novel \textit{Physics-Informed Loss} (PIL) that models the interaction between the predicted and ground-truth boundaries as an elastic process inspired by dislocation theory in materials physics. This formulation introduces a physics-based regularization term that enforces smooth contour evolution and structural consistency, allowing the network to better capture fine vascular geometry. The proposed loss is integrated into several segmentation architectures, including U-Net, U-Net++, SegFormer, and MedFormer, and evaluated on two public benchmarks: DIAS and DSCA. Experimental results demonstrate that PIL consistently outperforms conventional loss functions such as Cross-Entropy, Dice, Active Contour, and Surface losses, achieving superior sensitivity, F1 score, and boundary coherence. These findings confirm that the incorporation of physics-based boundary interactions into deep neural networks improves both the precision and robustness of vascular segmentation in dynamic angiographic imaging. The implementation of the proposed method is publicly available at https://github.com/irfantahir301/Physicsis_loss.

