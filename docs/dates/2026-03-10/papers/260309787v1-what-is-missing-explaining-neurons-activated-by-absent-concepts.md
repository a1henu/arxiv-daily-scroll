---
layout: default
title: What is Missing? Explaining Neurons Activated by Absent Concepts
---

# What is Missing? Explaining Neurons Activated by Absent Concepts
**arXiv**：[2603.09787v1](https://arxiv.org/abs/2603.09787) · [PDF](https://arxiv.org/pdf/2603.09787.pdf)  
**作者**：Robin Hesse, Simone Schaub-Meyer, Janina Hesse, Bernt Schiele, Stefan Roth  

**一句话要点**：提出扩展方法以揭示深度神经网络中编码缺失概念的现象

**关键词**：可解释人工智能, 编码缺失概念, 归因方法, 特征可视化, 深度神经网络, 去偏

## 3 点简述
- 核心问题：主流可解释AI方法难以揭示神经元因概念缺失而激活的因果关系
- 方法要点：扩展归因和特征可视化技术，以检测编码缺失概念
- 实验或效果：在ImageNet模型中验证编码缺失的普遍性，并展示其在去偏中的应用

## 摘要（原文）

> Explainable artificial intelligence (XAI) aims to provide human-interpretable insights into the behavior of deep neural networks (DNNs), typically by estimating a simplified causal structure of the model. In existing work, this causal structure often includes relationships where the presence of a concept is associated with a strong activation of a neuron. For example, attribution methods primarily identify input pixels that contribute most to a prediction, and feature visualization methods reveal inputs that cause high activation of a target neuron - the former implicitly assuming that the relevant information resides in the input, and the latter that neurons encode the presence of concepts. However, a largely overlooked type of causal relationship is that of encoded absences, where the absence of a concept increases neural activation. In this work, we show that such missing but relevant concepts are common and that mainstream XAI methods struggle to reveal them when applied in their standard form. To address this, we propose two simple extensions to attribution and feature visualization techniques that uncover encoded absences. Across experiments, we show how mainstream XAI methods can be used to reveal and explain encoded absences, how ImageNet models exploit them, and that debiasing can be improved when considering them.

