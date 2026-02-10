---
layout: default
title: Artifact Reduction in Undersampled 3D Cone-Beam CTs using a Hybrid 2D-3D CNN Framework
---

# Artifact Reduction in Undersampled 3D Cone-Beam CTs using a Hybrid 2D-3D CNN Framework
**arXiv**：[2602.08727v1](https://arxiv.org/abs/2602.08727) · [PDF](https://arxiv.org/pdf/2602.08727.pdf)  
**作者**：Johannes Thalhammer, Tina Dorosti, Sebastian Peterhansl, Daniela Pfeiffer, Franz Pfeiffer, Florian Schaff  

**一句话要点**：提出混合2D-3D CNN框架以减少欠采样3D锥束CT中的伪影

**关键词**：欠采样CT, 伪影减少, 混合深度学习, 2D-3D CNN, 锥束CT, 图像后处理

## 3 点简述
- 欠采样CT减少采集时间但引入伪影，影响图像质量和诊断价值
- 采用两阶段方法：2D U-Net提取切片特征，3D解码器利用跨切片上下文预测无伪影3D体积
- 实验显示冠状面和矢状面切片间一致性显著提升，计算开销低

## 摘要（原文）

> Undersampled CT volumes minimize acquisition time and radiation exposure but introduce artifacts degrading image quality and diagnostic utility. Reducing these artifacts is critical for high-quality imaging. We propose a computationally efficient hybrid deep-learning framework that combines the strengths of 2D and 3D models. First, a 2D U-Net operates on individual slices of undersampled CT volumes to extract feature maps. These slice-wise feature maps are then stacked across the volume and used as input to a 3D decoder, which utilizes contextual information across slices to predict an artifact-free 3D CT volume. The proposed two-stage approach balances the computational efficiency of 2D processing with the volumetric consistency provided by 3D modeling. The results show substantial improvements in inter-slice consistency in coronal and sagittal direction with low computational overhead. This hybrid framework presents a robust and efficient solution for high-quality 3D CT image post-processing. The code of this project can be found on github: https://github.com/J-3TO/2D-3DCNN_sparseview/.

