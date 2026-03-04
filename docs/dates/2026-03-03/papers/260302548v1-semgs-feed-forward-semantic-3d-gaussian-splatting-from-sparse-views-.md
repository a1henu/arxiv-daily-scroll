---
layout: default
title: SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding
---

# SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding
**arXiv**：[2603.02548v1](https://arxiv.org/abs/2603.02548) · [PDF](https://arxiv.org/pdf/2603.02548.pdf)  
**作者**：Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  

**一句话要点**：提出SemGS框架，从稀疏视图重建可泛化语义场以解决3D场景理解问题

**关键词**：语义3D高斯溅射, 稀疏视图重建, 可泛化场景理解, 双分支架构, 相机感知注意力

## 3 点简述
- 核心问题：现有方法依赖密集多视图输入和场景特定优化，限制实际应用。
- 方法要点：采用双分支架构提取颜色和语义特征，结合相机感知注意力机制和双高斯解码。
- 实验或效果：在基准数据集上实现先进性能，提供快速推理和强泛化能力。

## 摘要（原文）

> Semantic understanding of 3D scenes is essential for robots to operate effectively and safely in complex environments. Existing methods for semantic scene reconstruction and semantic-aware novel view synthesis often rely on dense multi-view inputs and require scene-specific optimization, limiting their practicality and scalability in real-world applications. To address these challenges, we propose SemGS, a feed-forward framework for reconstructing generalizable semantic fields from sparse image inputs. SemGS uses a dual-branch architecture to extract color and semantic features, where the two branches share shallow CNN layers, allowing semantic reasoning to leverage textural and structural cues in color appearance. We also incorporate a camera-aware attention mechanism into the feature extractor to explicitly model geometric relationships between camera viewpoints. The extracted features are decoded into dual-Gaussians that share geometric consistency while preserving branch-specific attributes, and further rasterized to synthesize semantic maps under novel viewpoints. Additionally, we introduce a regional smoothness loss to enhance semantic coherence. Experiments show that SemGS achieves state-of-the-art performance on benchmark datasets, while providing rapid inference and strong generalization capabilities across diverse synthetic and real-world scenarios.

