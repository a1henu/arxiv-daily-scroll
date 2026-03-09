---
layout: default
title: Training Flow Matching: The Role of Weighting and Parameterization
---

# Training Flow Matching: The Role of Weighting and Parameterization
**arXiv**：[2603.06454v1](https://arxiv.org/abs/2603.06454) · [PDF](https://arxiv.org/pdf/2603.06454.pdf)  
**作者**：Anne Gagneux, Ségolène Martin, Rémi Gribonval, Mathurin Massias  

**一句话要点**：分析去噪生成模型训练目标中损失加权与输出参数化的影响

**关键词**：去噪生成模型, 训练目标分析, 损失加权, 输出参数化, 流形内在维度, 生成质量评估

## 3 点简述
- 核心问题：研究去噪生成模型训练目标，聚焦损失加权和输出参数化（如噪声、干净图像、速度）的作用
- 方法要点：通过系统数值实验，分析训练选择与数据流形内在维度、模型架构和数据集大小的交互
- 实验或效果：在合成和图像数据集上评估去噪精度（PSNR）和生成质量（FID），提供设计选择的实用见解

## 摘要（原文）

> We study the training objectives of denoising-based generative models, with a particular focus on loss weighting and output parameterization, including noise-, clean image-, and velocity-based formulations. Through a systematic numerical study, we analyze how these training choices interact with the intrinsic dimensionality of the data manifold, model architecture, and dataset size. Our experiments span synthetic datasets with controlled geometry as well as image data, and compare training objectives using quantitative metrics for denoising accuracy (PSNR across noise levels) and generative quality (FID). Rather than proposing a new method, our goal is to disentangle the various factors that matter when training a flow matching model, in order to provide practical insights on design choices.

