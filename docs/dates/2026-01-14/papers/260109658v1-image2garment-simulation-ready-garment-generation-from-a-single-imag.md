---
layout: default
title: Image2Garment: Simulation-ready Garment Generation from a Single Image
---

# Image2Garment: Simulation-ready Garment Generation from a Single Image
**arXiv**：[2601.09658v1](https://arxiv.org/abs/2601.09658) · [PDF](https://arxiv.org/pdf/2601.09658.pdf)  
**作者**：Selim Emir Can, Jan Ackermann, Kiyohiro Nakayama, Ruofan Liu, Tong Wu, Yang Zheng, Hugo Bertiche, Menglei Chai, Thabo Beeler, Gordon Wetzstein  

**一句话要点**：提出Image2Garment框架，从单张图像生成仿真就绪的服装，无需迭代优化。

**关键词**：单图像服装生成, 物理仿真, 材料属性推断, 视觉语言模型, 数据集构建

## 3 点简述
- 核心问题：单张图像估计物理准确的仿真就绪服装，缺乏图像到物理数据集且问题不适定。
- 方法要点：先微调视觉语言模型推断材料属性，再训练轻量预测器映射到物理参数，引入新数据集。
- 实验或效果：在材料组成估计和织物属性预测上更准确，实现更高保真度的仿真。

## 摘要（原文）

> Estimating physically accurate, simulation-ready garments from a single image is challenging due to the absence of image-to-physics datasets and the ill-posed nature of this problem. Prior methods either require multi-view capture and expensive differentiable simulation or predict only garment geometry without the material properties required for realistic simulation. We propose a feed-forward framework that sidesteps these limitations by first fine-tuning a vision-language model to infer material composition and fabric attributes from real images, and then training a lightweight predictor that maps these attributes to the corresponding physical fabric parameters using a small dataset of material-physics measurements. Our approach introduces two new datasets (FTAG and T2P) and delivers simulation-ready garments from a single image without iterative optimization. Experiments show that our estimator achieves superior accuracy in material composition estimation and fabric attribute prediction, and by passing them through our physics parameter estimator, we further achieve higher-fidelity simulations compared to state-of-the-art image-to-garment methods.

