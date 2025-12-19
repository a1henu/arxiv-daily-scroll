---
layout: default
title: Towards Reproducibility in Predictive Process Mining: SPICE - A Deep Learning Library
---

# Towards Reproducibility in Predictive Process Mining: SPICE - A Deep Learning Library
**arXiv**：[2512.16715v1](https://arxiv.org/abs/2512.16715) · [PDF](https://arxiv.org/pdf/2512.16715.pdf)  
**作者**：Oliver Stritzel, Nick Hühnerbein, Simon Rauch, Itzel Zarate, Lukas Fleischmann, Moike Buck, Attila Lischka, Christian Frey  

**一句话要点**：提出SPICE框架以解决预测过程挖掘中深度学习方法缺乏可复现性和可比性的问题。

**关键词**：预测过程挖掘, 深度学习框架, 可复现性, PyTorch, 基准测试

## 3 点简述
- 核心问题：预测过程挖掘方法常缺乏可复现性、透明度和统一基准，导致比较困难。
- 方法要点：SPICE在PyTorch中重新实现三种基线深度学习方法，提供可配置基础框架。
- 实验或效果：在11个数据集上比较SPICE与原方法，评估其复现性和公平性。

## 摘要（原文）

> In recent years, Predictive Process Mining (PPM) techniques based on artificial neural networks have evolved as a method for monitoring the future behavior of unfolding business processes and predicting Key Performance Indicators (KPIs). However, many PPM approaches often lack reproducibility, transparency in decision making, usability for incorporating novel datasets and benchmarking, making comparisons among different implementations very difficult. In this paper, we propose SPICE, a Python framework that reimplements three popular, existing baseline deep-learning-based methods for PPM in PyTorch, while designing a common base framework with rigorous configurability to enable reproducible and robust comparison of past and future modelling approaches. We compare SPICE to original reported metrics and with fair metrics on 11 datasets.

