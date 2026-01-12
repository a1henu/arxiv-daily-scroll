---
layout: default
title: Detecting Autism Spectrum Disorder with Deep Eye Movement Features
---

# Detecting Autism Spectrum Disorder with Deep Eye Movement Features
**arXiv**：[2601.05812v1](https://arxiv.org/abs/2601.05812) · [PDF](https://arxiv.org/pdf/2601.05812.pdf)  
**作者**：Zhanpei Huang, Taochen chen, Fangqing Gu, Yiqun Zhang  

**一句话要点**：提出离散短期序列建模框架以提升自闭症谱系障碍的深度眼动特征检测

**关键词**：自闭症谱系障碍检测, 眼动数据分析, 离散短期序列建模, 类感知表示, 不平衡感知机制, 深度学习

## 3 点简述
- 核心问题：自闭症谱系障碍检测中，眼动数据的离散性和短期依赖性限制了全局注意力机制的有效性。
- 方法要点：设计离散短期序列建模框架，结合类感知表示和不平衡感知机制，以捕捉局部眼动模式。
- 实验或效果：在多个眼动数据集上，该框架优于传统机器学习和深度学习模型。

## 摘要（原文）

> Autism Spectrum Disorder (ASD) is a neurodevelopmental disorder characterized by deficits in social communication and behavioral patterns. Eye movement data offers a non-invasive diagnostic tool for ASD detection, as it is inherently discrete and exhibits short-term temporal dependencies, reflecting localized gaze focus between fixation points. These characteristics enable the data to provide deeper insights into subtle behavioral markers, distinguishing ASD-related patterns from typical development. Eye movement signals mainly contain short-term and localized dependencies. However, despite the widespread application of stacked attention layers in Transformer-based models for capturing long-range dependencies, our experimental results indicate that this approach yields only limited benefits when applied to eye movement data. This may be because discrete fixation points and short-term dependencies in gaze focus reduce the utility of global attention mechanisms, making them less efficient than architectures focusing on local temporal patterns. To efficiently capture subtle and complex eye movement patterns, distinguishing ASD from typically developing (TD) individuals, a discrete short-term sequential (DSTS) modeling framework is designed with Class-aware Representation and Imbalance-aware Mechanisms. Through extensive experiments on several eye movement datasets, DSTS outperforms both traditional machine learning techniques and more sophisticated deep learning models.

