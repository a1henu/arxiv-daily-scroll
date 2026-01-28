---
layout: default
title: Hyperbolic Additive Margin Softmax with Hierarchical Information for Speaker Verification
---

# Hyperbolic Additive Margin Softmax with Hierarchical Information for Speaker Verification
**arXiv**：[2601.19709v1](https://arxiv.org/abs/2601.19709) · [PDF](https://arxiv.org/pdf/2601.19709.pdf)  
**作者**：Zhihua Fang, Liang He  

**一句话要点**：提出基于双曲空间的H-Softmax和HAM-Softmax方法，以增强说话人验证中的层次信息建模能力。

**关键词**：说话人验证, 双曲空间, 层次信息建模, 边界约束, 嵌入学习

## 3 点简述
- 核心问题：欧几里得空间说话人嵌入学习在建模特征层次信息方面不足。
- 方法要点：将嵌入和说话人中心投影到双曲空间，利用双曲距离计算，HAM-Softmax引入边界约束增强类间分离性。
- 实验或效果：相比标准Softmax和AM-Softmax，平均相对EER分别降低27.84%和14.23%，验证了性能提升和层次结构建模能力。

## 摘要（原文）

> Speaker embedding learning based on Euclidean space has achieved significant progress, but it is still insufficient in modeling hierarchical information within speaker features. Hyperbolic space, with its negative curvature geometric properties, can efficiently represent hierarchical information within a finite volume, making it more suitable for the feature distribution of speaker embeddings. In this paper, we propose Hyperbolic Softmax (H-Softmax) and Hyperbolic Additive Margin Softmax (HAM-Softmax) based on hyperbolic space. H-Softmax incorporates hierarchical information into speaker embeddings by projecting embeddings and speaker centers into hyperbolic space and computing hyperbolic distances. HAM-Softmax further enhances inter-class separability by introducing margin constraint on this basis. Experimental results show that H-Softmax and HAM-Softmax achieve average relative EER reductions of 27.84% and 14.23% compared with standard Softmax and AM-Softmax, respectively, demonstrating that the proposed methods effectively improve speaker verification performance and at the same time preserve the capability of hierarchical structure modeling. The code will be released at https://github.com/PunkMale/HAM-Softmax.

