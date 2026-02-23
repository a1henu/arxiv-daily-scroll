---
layout: default
title: Quantum-enhanced satellite image classification
---

# Quantum-enhanced satellite image classification
**arXiv**：[2602.18350v1](https://arxiv.org/abs/2602.18350) · [PDF](https://arxiv.org/pdf/2602.18350.pdf)  
**作者**：Qi Zhang, Anton Simen, Carlos Flores-Garrigós, Gabriel Alvarado Barrios, Paolo A. Erdman, Enrique Solano, Aaron C. Kemp, Vincent Beltrani, Vedangi Pathak, Hamed Mohammadbagherpoor  

**一句话要点**：提出量子特征提取方法以增强卫星图像多分类精度

**关键词**：量子特征提取, 卫星图像分类, 量子-经典混合方法, 多体自旋哈密顿量, IBM量子处理器

## 3 点简述
- 核心问题：卫星图像多分类任务中，经典方法精度有限，需提升性能。
- 方法要点：利用多体自旋哈密顿量动力学生成量子特征，结合经典处理实现量子增强。
- 实验或效果：在IBM量子处理器上实现，相比ResNet50基线，准确率从83%提升至87%。

## 摘要（原文）

> We demonstrate the application of a quantum feature extraction method to enhance multi-class image classification for space applications. By harnessing the dynamics of many-body spin Hamiltonians, the method generates expressive quantum features that, when combined with classical processing, lead to quantum-enhanced classification accuracy. Using a strong and well-established ResNet50 baseline, we achieved a maximum classical accuracy of 83%, which can be improved to 84% with a transfer learning approach. In contrast, applying our quantum-classical method the performance is increased to 87% accuracy, demonstrating a clear and reproducible improvement over robust classical approaches. Implemented on several of IBM's quantum processors, our hybrid quantum-classical approach delivers consistent gains of 2-3% in absolute accuracy. These results highlight the practical potential of current and near-term quantum processors in high-stakes, data-driven domains such as satellite imaging and remote sensing, while suggesting broader applicability in real-world machine learning tasks.

