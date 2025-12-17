---
layout: default
title: Improving Semantic Uncertainty Quantification in LVLMs with Semantic Gaussian Processes
---

# Improving Semantic Uncertainty Quantification in LVLMs with Semantic Gaussian Processes
**arXiv**：[2512.14177v1](https://arxiv.org/abs/2512.14177) · [PDF](https://arxiv.org/pdf/2512.14177.pdf)  
**作者**：Joseph Hoche, Andrei Bursuc, David Brellmann, Gilles Louppe, Pavel Izmailov, Angela Yao, Gianni Franchi  

**一句话要点**：提出语义高斯过程不确定性框架以提升大视觉语言模型的语义不确定性量化

**关键词**：语义不确定性量化, 大视觉语言模型, 高斯过程分类器, 谱表示, 校准性能, 跨模态泛化

## 3 点简述
- 核心问题：大视觉语言模型输出不可靠，现有语义不确定性估计方法依赖聚类，易受措辞变化影响，导致估计不稳定。
- 方法要点：引入语义高斯过程不确定性，通过分析答案嵌入的几何结构，避免脆弱聚类，利用谱表示和分类器学习语义一致性模式。
- 实验或效果：在六个模型和八个数据集上，实现校准和判别性能最优，并展示跨模型和模态的泛化能力。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) often produce plausible but unreliable outputs, making robust uncertainty estimation essential. Recent work on semantic uncertainty estimates relies on external models to cluster multiple sampled responses and measure their semantic consistency. However, these clustering methods are often fragile, highly sensitive to minor phrasing variations, and can incorrectly group or separate semantically similar answers, leading to unreliable uncertainty estimates. We propose Semantic Gaussian Process Uncertainty (SGPU), a Bayesian framework that quantifies semantic uncertainty by analyzing the geometric structure of answer embeddings, avoiding brittle clustering. SGPU maps generated answers into a dense semantic space, computes the Gram matrix of their embeddings, and summarizes their semantic configuration via the eigenspectrum. This spectral representation is then fed into a Gaussian Process Classifier that learns to map patterns of semantic consistency to predictive uncertainty, and that can be applied in both black-box and white-box settings. Across six LLMs and LVLMs on eight datasets spanning VQA, image classification, and textual QA, SGPU consistently achieves state-of-the-art calibration (ECE) and discriminative (AUROC, AUARC) performance. We further show that SGPU transfers across models and modalities, indicating that its spectral representation captures general patterns of semantic uncertainty.

