---
layout: default
title: Joint Semantic and Rendering Enhancements in 3D Gaussian Modeling with Anisotropic Local Encoding
---

# Joint Semantic and Rendering Enhancements in 3D Gaussian Modeling with Anisotropic Local Encoding
**arXiv**：[2601.02339v1](https://arxiv.org/abs/2601.02339) · [PDF](https://arxiv.org/pdf/2601.02339.pdf)  
**作者**：Jingming He, Chongyi Li, Shiqi Wang, Sam Kwong  

**一句话要点**：提出联合增强框架，通过各向异性局部编码提升3D高斯建模的语义分割与渲染质量

**关键词**：3D高斯建模, 语义分割, 各向异性编码, 联合增强, 自适应渲染

## 3 点简述
- 核心问题：现有方法分离语义与渲染分支，依赖2D监督，忽略3D几何，自适应策略不足。
- 方法要点：引入各向异性3D高斯切比雪夫描述符捕获形状细节，结合语义与形状信号自适应调整高斯分配。
- 实验或效果：在多个数据集上提升分割精度与渲染质量，保持高渲染帧率，实现快速收敛。

## 摘要（原文）

> Recent works propose extending 3DGS with semantic feature vectors for simultaneous semantic segmentation and image rendering. However, these methods often treat the semantic and rendering branches separately, relying solely on 2D supervision while ignoring the 3D Gaussian geometry. Moreover, current adaptive strategies adapt the Gaussian set depending solely on rendering gradients, which can be insufficient in subtle or textureless regions. In this work, we propose a joint enhancement framework for 3D semantic Gaussian modeling that synergizes both semantic and rendering branches. Firstly, unlike conventional point cloud shape encoding, we introduce an anisotropic 3D Gaussian Chebyshev descriptor using the Laplace-Beltrami operator to capture fine-grained 3D shape details, thereby distinguishing objects with similar appearances and reducing reliance on potentially noisy 2D guidance. In addition, without relying solely on rendering gradient, we adaptively adjust Gaussian allocation and spherical harmonics with local semantic and shape signals, enhancing rendering efficiency through selective resource allocation. Finally, we employ a cross-scene knowledge transfer module to continuously update learned shape patterns, enabling faster convergence and robust representations without relearning shape information from scratch for each new scene. Experiments on multiple datasets demonstrate improvements in segmentation accuracy and rendering quality while maintaining high rendering frame rates.

