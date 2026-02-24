---
layout: default
title: Fully Convolutional Spatiotemporal Learning for Microstructure Evolution Prediction
---

# Fully Convolutional Spatiotemporal Learning for Microstructure Evolution Prediction
**arXiv**：[2602.19915v1](https://arxiv.org/abs/2602.19915) · [PDF](https://arxiv.org/pdf/2602.19915.pdf)  
**作者**：Michael Trimboli, Mohammed Alsubaie, Sirani M. Perera, Ke-Gang Wang, Xianqi Li  

**一句话要点**：提出全卷积时空学习框架以加速材料微观结构演化预测

**关键词**：微观结构演化预测, 全卷积时空模型, 自监督学习, 材料科学模拟, 计算加速

## 3 点简述
- 核心问题：传统相场模型计算成本高，需在精细时空分辨率下求解复杂偏微分方程。
- 方法要点：采用全卷积时空模型，通过自监督学习从模拟序列图像中学习物理动力学。
- 实验或效果：模型在训练和推理中显著降低计算成本，准确捕捉短期局部行为和长期统计特性。

## 摘要（原文）

> Understanding and predicting microstructure evolution is fundamental to materials science, as it governs the resulting properties and performance of materials. Traditional simulation methods, such as phase-field models, offer high-fidelity results but are computationally expensive due to the need to solve complex partial differential equations at fine spatiotemporal resolutions. To address this challenge, we propose a deep learning-based framework that accelerates microstructure evolution predictions while maintaining high accuracy. Our approach utilizes a fully convolutional spatiotemporal model trained in a self-supervised manner using sequential images generated from simulations of microstructural processes, including grain growth and spinodal decomposition. The trained neural network effectively learns the underlying physical dynamics and can accurately capture both short-term local behaviors and long-term statistical properties of evolving microstructures, while also demonstrating generalization to unseen spatiotemporal domains and variations in configuration and material parameters. Compared to recurrent neural architectures, our model achieves state-of-the-art predictive performance with significantly reduced computational cost in both training and inference. This work establishes a robust baseline for spatiotemporal learning in materials science and offers a scalable, data-driven alternative for fast and reliable microstructure simulations.

