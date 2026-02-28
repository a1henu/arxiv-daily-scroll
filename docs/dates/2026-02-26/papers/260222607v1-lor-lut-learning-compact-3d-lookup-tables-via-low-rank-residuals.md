---
layout: default
title: LoR-LUT: Learning Compact 3D Lookup Tables via Low-Rank Residuals
---

# LoR-LUT: Learning Compact 3D Lookup Tables via Low-Rank Residuals
**arXiv**：[2602.22607v1](https://arxiv.org/abs/2602.22607) · [PDF](https://arxiv.org/pdf/2602.22607.pdf)  
**作者**：Ziqi Zhao, Abhijit Mishra, Shounak Roychowdhury  

**一句话要点**：提出LoR-LUT，通过低秩残差学习紧凑3D查找表，用于图像增强与风格迁移。

**关键词**：3D查找表, 低秩残差, 图像增强, 风格迁移, 紧凑模型, 交互可视化

## 3 点简述
- 核心问题：传统3D-LUT方法依赖密集基表融合，导致模型参数多、效率低。
- 方法要点：引入低秩残差校正与基表联合优化，减少参数同时保持三线性插值复杂度。
- 实验或效果：在MIT-Adobe FiveK数据集上训练，实现专家级调色效果，模型尺寸小于1MB。

## 摘要（原文）

> We present LoR-LUT, a unified low-rank formulation for compact and interpretable 3D lookup table (LUT) generation. Unlike conventional 3D-LUT-based techniques that rely on fusion of basis LUTs, which are usually dense tensors, our unified approach extends the current framework by jointly using residual corrections, which are in fact low-rank tensors, together with a set of basis LUTs. The approach described here improves the existing perceptual quality of an image, which is primarily due to the technique's novel use of residual corrections. At the same time, we achieve the same level of trilinear interpolation complexity, using a significantly smaller number of network, residual corrections, and LUT parameters. The experimental results obtained from LoR-LUT, which is trained on the MIT-Adobe FiveK dataset, reproduce expert-level retouching characteristics with high perceptual fidelity and a sub-megabyte model size. Furthermore, we introduce an interactive visualization tool, termed LoR-LUT Viewer, which transforms an input image into the LUT-adjusted output image, via a number of slidebars that control different parameters. The tool provides an effective way to enhance interpretability and user confidence in the visual results. Overall, our proposed formulation offers a compact, interpretable, and efficient direction for future LUT-based image enhancement and style transfer.

