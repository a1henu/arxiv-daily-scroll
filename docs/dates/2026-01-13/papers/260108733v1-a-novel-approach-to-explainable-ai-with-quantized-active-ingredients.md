---
layout: default
title: A Novel Approach to Explainable AI with Quantized Active Ingredients in Decision Making
---

# A Novel Approach to Explainable AI with Quantized Active Ingredients in Decision Making
**arXiv**：[2601.08733v1](https://arxiv.org/abs/2601.08733) · [PDF](https://arxiv.org/pdf/2601.08733.pdf)  
**作者**：A. M. A. S. D. Alagiyawanna, Asoka Karunananda, Thushari Silva, A. Mahasinghe  

**一句话要点**：提出基于量子-经典混合模型的解释性AI框架，以提升高风险领域决策的透明度和准确性。

**关键词**：解释性人工智能, 量子玻尔兹曼机, 特征归因, 混合量子-经典模型, 高透明度决策

## 3 点简述
- 核心问题：AI系统在高风险领域（如健康、金融）缺乏解释性，影响信任和应用。
- 方法要点：结合量子玻尔兹曼机和经典玻尔兹曼机，利用量子计算原理增强模型的可解释性。
- 实验或效果：在二值化降维MNIST数据集上，量子模型分类准确率83.5%高于经典模型54%，且特征归因更集中。

## 摘要（原文）

> Artificial Intelligence (AI) systems have shown good success at classifying. However, the lack of explainability is a true and significant challenge, especially in high-stakes domains, such as health and finance, where understanding is paramount. We propose a new solution to this challenge: an explainable AI framework based on our comparative study with Quantum Boltzmann Machines (QBMs) and Classical Boltzmann Machines (CBMs). We leverage principles of quantum computing within classical machine learning to provide substantive transparency around decision-making. The design involves training both models on a binarised and dimensionally reduced MNIST dataset, where Principal Component Analysis (PCA) is applied for preprocessing. For interpretability, we employ gradient-based saliency maps in QBMs and SHAP (SHapley Additive exPlanations) in CBMs to evaluate feature attributions.QBMs deploy hybrid quantum-classical circuits with strongly entangling layers, allowing for richer latent representations, whereas CBMs serve as a classical baseline that utilises contrastive divergence. Along the way, we found that QBMs outperformed CBMs on classification accuracy (83.5% vs. 54%) and had more concentrated distributions in feature attributions as quantified by entropy (1.27 vs. 1.39). In other words, QBMs not only produced better predictive performance than CBMs, but they also provided clearer identification of "active ingredient" or the most important features behind model predictions. To conclude, our results illustrate that quantum-classical hybrid models can display improvements in both accuracy and interpretability, which leads us toward more trustworthy and explainable AI systems.

