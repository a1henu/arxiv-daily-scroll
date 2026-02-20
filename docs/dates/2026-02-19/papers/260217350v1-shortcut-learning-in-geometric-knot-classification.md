---
layout: default
title: Shortcut learning in geometric knot classification
---

# Shortcut learning in geometric knot classification
**arXiv**：[2602.17350v1](https://arxiv.org/abs/2602.17350) · [PDF](https://arxiv.org/pdf/2602.17350.pdf)  
**作者**：Djordje Mihajlovic, Davide Michieletto  

**一句话要点**：揭示机器学习在几何结分类中的捷径学习问题，并提供无偏数据集与代码以促进拓扑分类研究

**关键词**：几何结分类, 捷径学习, 拓扑特征, 机器学习, 分子动力学模拟, 数据集生成

## 3 点简述
- 研究机器学习在几何结分类任务中如何利用非拓扑特征进行捷径学习
- 通过分子动力学模拟生成数据，发现隐藏的非拓扑特征被用于分类
- 开发公开数据集和代码，旨在消除非拓扑特征，为未来研究提供基础

## 摘要（原文）

> Classifying the topology of closed curves is a central problem in low dimensional topology with applications beyond mathematics spanning protein folding, polymer physics and even magnetohydrodynamics. The central problem is how to determine whether two embeddings of a closed arc are equivalent under ambient isotopy. Given the striking ability of neural networks to solve complex classification tasks, it is therefore natural to ask if the knot classification problem can be tackled using Machine Learning (ML). In this paper, we investigate generic shortcut methods employed by ML to solve the knot classification challenge and specifically discover hidden non-topological features in training data generated through Molecular Dynamics simulations of polygonal knots that are used by ML to arrive to positive classifications results. We then provide a rigorous foundation for future attempts to tackle the knot classification challenge using ML by developing a publicly-available (i) dataset, that aims to remove the potential of non-topological feature classification and (ii) code, that can generate knot embeddings that faithfully explore chosen geometric state space with fixed knot topology. We expect that our work will accelerate the development of ML models that can solve complex geometric knot classification challenges.

