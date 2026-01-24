---
layout: default
title: LL-GaussianMap: Zero-shot Low-Light Image Enhancement via 2D Gaussian Splatting Guided Gain Maps
---

# LL-GaussianMap: Zero-shot Low-Light Image Enhancement via 2D Gaussian Splatting Guided Gain Maps
**arXiv**：[2601.15766v1](https://arxiv.org/abs/2601.15766) · [PDF](https://arxiv.org/pdf/2601.15766.pdf)  
**作者**：Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Jingrui Zhang, Kefei Qian, Wenbo Chu, Keqiang Li  

**一句话要点**：提出LL-GaussianMap，通过2D高斯溅射引导增益图实现零样本低光图像增强

**关键词**：低光图像增强, 2D高斯溅射, 增益图生成, 无监督学习, 显式表示, 结构感知

## 3 点简述
- 现有低光增强方法忽视图像几何结构先验，LL-GaussianMap首次将2D高斯溅射引入该任务
- 方法分两阶段：先利用2D高斯溅射进行高保真结构重建，再通过统一增强模块生成增益图
- 实验显示，该方法在无监督下实现优异增强效果，存储开销极低，验证了显式高斯表示的有效性

## 摘要（原文）

> Significant progress has been made in low-light image enhancement with respect to visual quality. However, most existing methods primarily operate in the pixel domain or rely on implicit feature representations. As a result, the intrinsic geometric structural priors of images are often neglected. 2D Gaussian Splatting (2DGS) has emerged as a prominent explicit scene representation technique characterized by superior structural fitting capabilities and high rendering efficiency. Despite these advantages, the utilization of 2DGS in low-level vision tasks remains unexplored. To bridge this gap, LL-GaussianMap is proposed as the first unsupervised framework incorporating 2DGS into low-light image enhancement. Distinct from conventional methodologies, the enhancement task is formulated as a gain map generation process guided by 2DGS primitives. The proposed method comprises two primary stages. First, high-fidelity structural reconstruction is executed utilizing 2DGS. Then, data-driven enhancement dictionary coefficients are rendered via the rasterization mechanism of Gaussian splatting through an innovative unified enhancement module. This design effectively incorporates the structural perception capabilities of 2DGS into gain map generation, thereby preserving edges and suppressing artifacts during enhancement. Additionally, the reliance on paired data is circumvented through unsupervised learning. Experimental results demonstrate that LL-GaussianMap achieves superior enhancement performance with an extremely low storage footprint, highlighting the effectiveness of explicit Gaussian representations for image enhancement.

