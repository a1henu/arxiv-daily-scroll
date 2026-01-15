---
layout: default
title: DeepLight: A Sobolev-trained Image-to-Image Surrogate Model for Light Transport in Tissue
---

# DeepLight: A Sobolev-trained Image-to-Image Surrogate Model for Light Transport in Tissue
**arXiv**：[2601.09439v1](https://arxiv.org/abs/2601.09439) · [PDF](https://arxiv.org/pdf/2601.09439.pdf)  
**作者**：Philipp Haim, Vasilis Ntziachristos, Torsten Enßlin, Dominik Jüstel  

**一句话要点**：提出Sobolev训练的图像到图像代理模型以解决组织光传输逆问题中的导数精度问题

**关键词**：光声成像, 光传输模型, 神经代理模型, Sobolev训练, 逆问题, 导数精度

## 3 点简述
- 核心问题：光声成像中，组织吸收系数反演依赖准确可微的光传输模型，但现有神经代理模型导数不匹配物理算子，阻碍高保真重建。
- 方法要点：采用Sobolev训练提升代理模型导数精度，该方法适用于高维模型，旨在改善模型在逆问题中的实用性。
- 实验或效果：Sobolev训练不仅提高导数准确性，还降低分布内和分布外样本的泛化误差，增强下游任务性能。

## 摘要（原文）

> In optoacoustic imaging, recovering the absorption coefficients of tissue by inverting the light transport remains a challenging problem. Improvements in solving this problem can greatly benefit the clinical value of optoacoustic imaging. Existing variational inversion methods require an accurate and differentiable model of this light transport. As neural surrogate models allow fast and differentiable simulations of complex physical processes, they are considered promising candidates to be used in solving such inverse problems. However, there are in general no guarantees that the derivatives of these surrogate models accurately match those of the underlying physical operator. As accurate derivatives are central to solving inverse problems, errors in the model derivative can considerably hinder high fidelity reconstructions. To overcome this limitation, we present a surrogate model for light transport in tissue that uses Sobolev training to improve the accuracy of the model derivatives. Additionally, the form of Sobolev training we used is suitable for high-dimensional models in general. Our results demonstrate that Sobolev training for a light transport surrogate model not only improves derivative accuracy but also reduces generalization error for in-distribution and out-of-distribution samples. These improvements promise to considerably enhance the utility of the surrogate model in downstream tasks, especially in solving inverse problems.

