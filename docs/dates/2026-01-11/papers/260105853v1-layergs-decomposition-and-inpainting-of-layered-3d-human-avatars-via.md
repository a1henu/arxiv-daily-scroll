---
layout: default
title: LayerGS: Decomposition and Inpainting of Layered 3D Human Avatars via 2D Gaussian Splatting
---

# LayerGS: Decomposition and Inpainting of Layered 3D Human Avatars via 2D Gaussian Splatting
**arXiv**：[2601.05853v1](https://arxiv.org/abs/2601.05853) · [PDF](https://arxiv.org/pdf/2601.05853.pdf)  
**作者**：Yinghan Xu, John Dingliana  

**一句话要点**：提出LayerGS框架，通过2D高斯溅射分解和修复多层3D人体化身，实现虚拟试穿。

**关键词**：3D人体化身, 多层分解, 2D高斯溅射, 虚拟试穿, 扩散模型修复

## 3 点简述
- 核心问题：传统单层重建方法将衣物锁定于单一身份，多层方法难以处理遮挡区域。
- 方法要点：使用2D高斯编码各层几何与渲染，结合预训练扩散模型修复隐藏区域。
- 实验效果：在4D-Dress和Thuman2.0数据集上优于现有方法，支持新视角和姿态下的虚拟试穿。

## 摘要（原文）

> We propose a novel framework for decomposing arbitrarily posed humans into animatable multi-layered 3D human avatars, separating the body and garments. Conventional single-layer reconstruction methods lock clothing to one identity, while prior multi-layer approaches struggle with occluded regions. We overcome both limitations by encoding each layer as a set of 2D Gaussians for accurate geometry and photorealistic rendering, and inpainting hidden regions with a pretrained 2D diffusion model via score-distillation sampling (SDS). Our three-stage training strategy first reconstructs the coarse canonical garment via single-layer reconstruction, followed by multi-layer training to jointly recover the inner-layer body and outer-layer garment details. Experiments on two 3D human benchmark datasets (4D-Dress, Thuman2.0) show that our approach achieves better rendering quality and layer decomposition and recomposition than the previous state-of-the-art, enabling realistic virtual try-on under novel viewpoints and poses, and advancing practical creation of high-fidelity 3D human assets for immersive applications. Our code is available at https://github.com/RockyXu66/LayerGS

