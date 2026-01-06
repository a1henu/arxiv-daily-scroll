---
layout: default
title: Face Normal Estimation from Rags to Riches
---

# Face Normal Estimation from Rags to Riches
**arXiv**：[2601.01950v1](https://arxiv.org/abs/2601.01950) · [PDF](https://arxiv.org/pdf/2601.01950.pdf)  
**作者**：Meng Wang, Wenjing Dai, Jiawan Zhang, Xiaojie Guo  

**一句话要点**：提出粗到细人脸法线估计方法以减少大规模配对数据依赖

**关键词**：人脸法线估计, 粗到细估计, 自注意力机制, 数据高效训练, 法线细化

## 3 点简述
- 核心问题：人脸法线估计依赖大规模配对数据，训练成本高。
- 方法要点：先训练粗估计模型生成引导，再用自注意力机制细化以消除局部伪影。
- 实验或效果：实验显示方法在训练开销和估计质量上优于现有技术。

## 摘要（原文）

> Although recent approaches to face normal estimation have achieved promising results, their effectiveness heavily depends on large-scale paired data for training. This paper concentrates on relieving this requirement via developing a coarse-to-fine normal estimator. Concretely, our method first trains a neat model from a small dataset to produce coarse face normals that perform as guidance (called exemplars) for the following refinement. A self-attention mechanism is employed to capture long-range dependencies, thus remedying severe local artifacts left in estimated coarse facial normals. Then, a refinement network is customized for the sake of mapping input face images together with corresponding exemplars to fine-grained high-quality facial normals. Such a logical function split can significantly cut the requirement of massive paired data and computational resource. Extensive experiments and ablation studies are conducted to demonstrate the efficacy of our design and reveal its superiority over state-of-the-art methods in terms of both training expense as well as estimation quality. Our code and models are open-sourced at: https://github.com/AutoHDR/FNR2R.git.

