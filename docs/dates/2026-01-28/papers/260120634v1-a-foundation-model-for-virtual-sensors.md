---
layout: default
title: A Foundation Model for Virtual Sensors
---

# A Foundation Model for Virtual Sensors
**arXiv**：[2601.20634v1](https://arxiv.org/abs/2601.20634) · [PDF](https://arxiv.org/pdf/2601.20634.pdf)  
**作者**：Leon Götz, Lars Frederik Peiss, Erik Sauer, Andreas Udo Sass, Thorsten Bagdonat, Stephan Günnemann, Leo Schwinn  

**一句话要点**：提出首个虚拟传感器基础模型，以统一架构高效预测多样传感器信号并减少计算资源需求。

**关键词**：虚拟传感器, 基础模型, 时间序列预测, 计算效率, 传感器网络, 机器学习

## 3 点简述
- 现有虚拟传感器方法需针对每个传感器定制模型，无法利用任务协同且缺乏标准基准。
- 该模型能同时预测多种虚拟传感器，自动学习输入信号，提升可解释性并保持计算效率。
- 在大规模评估中，相比基线实现计算时间减少415倍、内存需求减少951倍，预测质量相当或更优。

## 摘要（原文）

> Virtual sensors use machine learning to predict target signals from available measurements, replacing expensive physical sensors in critical applications. Existing virtual sensor approaches require application-specific models with hand-selected inputs for each sensor, cannot leverage task synergies, and lack consistent benchmarks. At the same time, emerging time series foundation models are computationally expensive and limited to predicting their input signals, making them incompatible with virtual sensors. We introduce the first foundation model for virtual sensors addressing both limitations. Our unified model can simultaneously predict diverse virtual sensors exploiting synergies while maintaining computational efficiency. It learns relevant input signals for each virtual sensor, eliminating expert knowledge requirements while adding explainability. In our large-scale evaluation on a standard benchmark and an application-specific dataset with over 18 billion samples, our architecture achieves 415x reduction in computation time and 951x reduction in memory requirements, while maintaining or even improving predictive quality compared to baselines. Our model scales gracefully to hundreds of virtual sensors with nearly constant parameter count, enabling practical deployment in large-scale sensor networks.

