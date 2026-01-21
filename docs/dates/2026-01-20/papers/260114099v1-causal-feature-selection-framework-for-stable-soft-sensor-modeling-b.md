---
layout: default
title: Causal feature selection framework for stable soft sensor modeling based on time-delayed cross mapping
---

# Causal feature selection framework for stable soft sensor modeling based on time-delayed cross mapping
**arXiv**：[2601.14099v1](https://arxiv.org/abs/2601.14099) · [PDF](https://arxiv.org/pdf/2601.14099.pdf)  
**作者**：Shi-Shun Chen, Xiao-Yang Li, Enrico Zio  

**一句话要点**：提出基于时滞交叉映射的因果特征选择框架，以提升工业软传感器建模的准确性与稳定性。

**关键词**：因果特征选择, 软传感器建模, 时滞交叉映射, 工业过程监控, 状态空间重构

## 3 点简述
- 核心问题：现有因果特征选择方法忽略工业过程中变量的时滞因果关系和相互依赖性，导致软传感器模型性能不足。
- 方法要点：引入时滞收敛交叉映射（TDCCM）和时滞偏交叉映射（TDPCM），结合状态空间重构处理变量依赖和时滞因果强度。
- 实验或效果：在真实案例中，TDCCM实现最高平均性能，TDPCM在极端场景下提升模型稳定性和性能。

## 摘要（原文）

> Soft sensor modeling plays a crucial role in process monitoring. Causal feature selection can enhance the performance of soft sensor models in industrial applications. However, existing methods ignore two critical characteristics of industrial processes. Firstly, causal relationships between variables always involve time delays, whereas most causal feature selection methods investigate causal relationships in the same time dimension. Secondly, variables in industrial processes are often interdependent, which contradicts the decorrelation assumption of traditional causal inference methods. Consequently, soft sensor models based on existing causal feature selection approaches often lack sufficient accuracy and stability. To overcome these challenges, this paper proposes a causal feature selection framework based on time-delayed cross mapping. Time-delayed cross mapping employs state space reconstruction to effectively handle interdependent variables in causality analysis, and considers varying causal strength across time delay. Time-delayed convergent cross mapping (TDCCM) is introduced for total causal inference, and time-delayed partial cross mapping (TDPCM) is developed for direct causal inference. Then, in order to achieve automatic feature selection, an objective feature selection strategy is presented. The causal threshold is automatically determined based on the model performance on the validation set, and the causal features are then selected. Two real-world case studies show that TDCCM achieves the highest average performance, while TDPCM improves soft sensor stability and performance in the worst scenario. The code is publicly available at https://github.com/dirge1/TDPCM.

