---
layout: default
title: TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity
---

# TIMI: Training-Free Image-to-3D Multi-Instance Generation with Spatial Fidelity
**arXiv**：[2603.01371v1](https://arxiv.org/abs/2603.01371) · [PDF](https://arxiv.org/pdf/2603.01371.pdf)  
**作者**：Xiao Cai, Lianli Gao, Pengpeng Zeng, Ji Zhang, Heng Tao Shen, Jingkuan Song  

**一句话要点**：提出TIMI训练免费框架以解决图像到3D多实例生成中的空间保真度问题

**关键词**：图像到3D生成, 多实例生成, 空间保真度, 训练免费框架, 实例解缠

## 3 点简述
- 核心问题：现有方法需微调预训练模型，训练成本高且空间保真度不足
- 方法要点：引入实例感知分离引导模块和空间稳定几何自适应更新模块，无需额外训练
- 实验或效果：在全局布局和局部实例上优于现有方法，推理速度更快

## 摘要（原文）

> Precise spatial fidelity in Image-to-3D multi-instance generation is critical for downstream real-world applications. Recent work attempts to address this by fine-tuning pre-trained Image-to-3D (I23D) models on multi-instance datasets, which incurs substantial training overhead and struggles to guarantee spatial fidelity. In fact, we observe that pre-trained I23D models already possess meaningful spatial priors, which remain underutilized as evidenced by instance entanglement issues. Motivated by this, we propose TIMI, a novel Training-free framework for Image-to-3D Multi-Instance generation that achieves high spatial fidelity. Specifically, we first introduce an Instance-aware Separation Guidance (ISG) module, which facilitates instance disentanglement during the early denoising stage. Next, to stabilize the guidance introduced by ISG, we devise a Spatial-stabilized Geometry-adaptive Update (SGU) module that promotes the preservation of the geometric characteristics of instances while maintaining their relative relationships. Extensive experiments demonstrate that our method yields better performance in terms of both global layout and distinct local instances compared to existing multi-instance methods, without requiring additional training and with faster inference speed.

