---
layout: default
title: Broken neural scaling laws in materials science
---

# Broken neural scaling laws in materials science
**arXiv**：[2602.05702v1](https://arxiv.org/abs/2602.05702) · [PDF](https://arxiv.org/pdf/2602.05702.pdf)  
**作者**：Max Großmann, Malte Grunert, Erich Runge  

**一句话要点**：研究材料科学中神经缩放定律的断裂现象，聚焦金属介电函数预测任务

**关键词**：材料科学, 神经缩放定律, 图神经网络, 介电函数预测, 高通量计算, 多目标学习

## 3 点简述
- 核心问题：材料科学数据稀缺昂贵，需明确模型性能随数据集大小和模型容量的缩放规律以区分数据与模型限制区域
- 方法要点：使用高通量从头计算生成超20万介电函数，训练多目标图神经网络预测频率依赖的复杂带间介电函数和Drude频率
- 实验或效果：观察到数据集大小相关的神经缩放定律断裂，而模型参数数量缩放遵循简单幂律并快速饱和

## 摘要（原文）

> In materials science, data are scarce and expensive to generate, whether computationally or experimentally. Therefore, it is crucial to identify how model performance scales with dataset size and model capacity to distinguish between data- and model-limited regimes. Neural scaling laws provide a framework for quantifying this behavior and guide the design of materials datasets and machine learning architectures. Here, we investigate neural scaling laws for a paradigmatic materials science task: predicting the dielectric function of metals, a high-dimensional response that governs how solids interact with light. Using over 200,000 dielectric functions from high-throughput ab initio calculations, we study two multi-objective graph neural networks trained to predict the frequency-dependent complex interband dielectric function and the Drude frequency. We observe broken neural scaling laws with respect to dataset size, whereas scaling with the number of model parameters follows a simple power law that rapidly saturates.

