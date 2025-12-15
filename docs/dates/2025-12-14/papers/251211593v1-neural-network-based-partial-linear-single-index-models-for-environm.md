---
layout: default
title: Neural Network-based Partial-Linear Single-Index Models for Environmental Mixtures Analysis
---

# Neural Network-based Partial-Linear Single-Index Models for Environmental Mixtures Analysis
**arXiv**：[2512.11593v1](https://arxiv.org/abs/2512.11593) · [PDF](https://arxiv.org/pdf/2512.11593.pdf)  
**作者**：Hyungrok Do, Yuyan Wang, Mengling Liu, Myeonggyun Lee  

**一句话要点**：提出基于神经网络的偏线性单指数模型，用于环境混合物健康效应分析。

**关键词**：环境混合物分析, 神经网络建模, 半参数回归, 可解释性, 健康效应评估, 开源软件

## 3 点简述
- 核心问题：评估复杂环境混合物的健康效应，现有方法在灵活性、可解释性和适用性上存在局限。
- 方法要点：结合半参数回归的可解释性与深度学习的表达能力，通过可学习投影构建暴露指数，并用神经网络建模其与结局的关系。
- 实验或效果：通过模拟研究和NHANES数据应用验证模型，提供开源软件包支持下游可视化和推断。

## 摘要（原文）

> Evaluating the health effects of complex environmental mixtures remains a central challenge in environmental health research. Existing approaches vary in their flexibility, interpretability, scalability, and support for diverse outcome types, often limiting their utility in real-world applications. To address these limitations, we propose a neural network-based partial-linear single-index (NeuralPLSI) modeling framework that bridges semiparametric regression modeling interpretability with the expressive power of deep learning. The NeuralPLSI model constructs an interpretable exposure index via a learnable projection and models its relationship with the outcome through a flexible neural network. The framework accommodates continuous, binary, and time-to-event outcomes, and supports inference through a bootstrap-based procedure that yields confidence intervals for key model parameters. We evaluated NeuralPLSI through simulation studies under a range of scenarios and applied it to data from the National Health and Nutrition Examination Survey (NHANES) to demonstrate its practical utility. Together, our contributions establish NeuralPLSI as a scalable, interpretable, and versatile modeling tool for mixture analysis. To promote adoption and reproducibility, we release a user-friendly open-source software package that implements the proposed methodology and supports downstream visualization and inference (\texttt{https://github.com/hyungrok-do/NeuralPLSI}).

