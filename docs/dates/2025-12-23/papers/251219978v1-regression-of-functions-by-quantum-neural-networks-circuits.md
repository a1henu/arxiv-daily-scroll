---
layout: default
title: Regression of Functions by Quantum Neural Networks Circuits
---

# Regression of Functions by Quantum Neural Networks Circuits
**arXiv**：[2512.19978v1](https://arxiv.org/abs/2512.19978) · [PDF](https://arxiv.org/pdf/2512.19978.pdf)  
**作者**：Fernando M. de Paula Neto, Lucas dos Reis Silva, Paulo S. G. de Mattos Neto, Felipe F. Fanchini  

**一句话要点**：提出遗传算法框架以自动化构建量子神经网络回归器架构

**关键词**：量子神经网络, 回归任务, 遗传算法, 自动化架构设计, 数据集复杂度分析, 量子回归

## 3 点简述
- 研究量子神经网络回归任务中架构选择难题，涉及电路深度与数据编码
- 引入遗传算法优化量子电路构建，探索参数化门配置与灵活数据重上传模式
- 在基准函数上评估，量子模型参数更少且性能竞争，分析数据集复杂度指导架构选择

## 摘要（原文）

> The performance of quantum neural network models depends strongly on architectural decisions, including circuit depth, placement of parametrized operations, and data-encoding strategies. Selecting an effective architecture is challenging and closely related to the classical difficulty of choosing suitable neural-network topologies, which is computationally hard. This work investigates automated quantum-circuit construction for regression tasks and introduces a genetic-algorithm framework that discovers Reduced Regressor QNN architectures. The approach explores depth, parametrized gate configurations, and flexible data re-uploading patterns, formulating the construction of quantum regressors as an optimization process. The discovered circuits are evaluated against seventeen classical regression models on twenty-two nonlinear benchmark functions and four analytical functions. Although classical methods often achieve comparable results, they typically require far more parameters, whereas the evolved quantum models remain compact while providing competitive performance. We further analyze dataset complexity using twelve structural descriptors and show, across five increasingly challenging meta-learning scenarios, that these measures can reliably predict which quantum architecture will perform best. The results demonstrate perfect or near-perfect predictive accuracy in several scenarios, indicating that complexity metrics offer powerful and compact representations of dataset structure and can effectively guide automated model selection. Overall, this study provides a principled basis for meta-learning-driven quantum architecture design and advances the understanding of how quantum models behave in regression settings--a topic that has received limited exploration in prior work. These findings pave the way for more systematic and theoretically grounded approaches to quantum regression.

