---
layout: default
title: Attention-guided reference point shifting for Gaussian-mixture-based partial point set registration
---

# Attention-guided reference point shifting for Gaussian-mixture-based partial point set registration
**arXiv**：[2512.02496v1](https://arxiv.org/abs/2512.02496) · [PDF](https://arxiv.org/pdf/2512.02496.pdf)  
**作者**：Mizuki Kikkawa, Tatsuya Yatagawa, Yutaka Ohtake, Hiromasa Suzuki  

**一句话要点**：提出注意力引导参考点偏移层以提升基于高斯混合模型的部分点云配准性能

**关键词**：点云配准, 高斯混合模型, 注意力机制, 深度学习, 部分点云

## 3 点简述
- 分析基于深度学习和GMM的部分点云配准方法在平移旋转下的特征不变性问题
- 引入ARPS层通过注意力模块稳健识别共同参考点以获取变换不变特征
- 实验显示ARPS显著增强DeepGMR和UGMMReg，优于现有基于注意力的方法

## 摘要（原文）

> This study investigates the impact of the invariance of feature vectors for partial-to-partial point set registration under translation and rotation of input point sets, particularly in the realm of techniques based on deep learning and Gaussian mixture models (GMMs). We reveal both theoretical and practical problems associated with such deep-learning-based registration methods using GMMs, with a particular focus on the limitations of DeepGMR, a pioneering study in this line, to the partial-to-partial point set registration. Our primary goal is to uncover the causes behind such methods and propose a comprehensible solution for that. To address this, we introduce an attention-based reference point shifting (ARPS) layer, which robustly identifies a common reference point of two partial point sets, thereby acquiring transformation-invariant features. The ARPS layer employs a well-studied attention module to find a common reference point rather than the overlap region. Owing to this, it significantly enhances the performance of DeepGMR and its recent variant, UGMMReg. Furthermore, these extension models outperform even prior deep learning methods using attention blocks and Transformer to extract the overlap region or common reference points. We believe these findings provide deeper insights into registration methods using deep learning and GMMs.

