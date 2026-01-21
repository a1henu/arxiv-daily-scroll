---
layout: default
title: MN-TSG:Continuous Time Series Generation with Irregular Observations
---

# MN-TSG:Continuous Time Series Generation with Irregular Observations
**arXiv**：[2601.13534v1](https://arxiv.org/abs/2601.13534) · [PDF](https://arxiv.org/pdf/2601.13534.pdf)  
**作者**：Xu Zhang, Junwei Deng, Chang Xu, Hao Li, Jiang Bian  

**一句话要点**：提出MN-TSG框架，基于混合专家NCDE解决不规则观测的连续时间序列生成问题

**关键词**：时间序列生成, 不规则观测, 神经控制微分方程, 混合专家, 连续生成, 医疗监测

## 3 点简述
- 核心问题：现有方法假设规则采样，不适用于医疗等场景中的不规则稀疏观测
- 方法要点：结合混合专家NCDE与现有TSG模型，动态参数化专家函数以优化生成
- 实验或效果：在十个数据集上验证，在不规则到规则及连续生成任务中优于基线

## 摘要（原文）

> Time series generation (TSG) plays a critical role in a wide range of domains, such as healthcare. However, most existing methods assume regularly sampled observations and fixed output resolutions, which are often misaligned with real-world scenarios where data are irregularly sampled and sparsely observed. This mismatch is particularly problematic in applications such as clinical monitoring, where irregular measurements must support downstream tasks requiring continuous and high-resolution time series.
>   Neural Controlled Differential Equations (NCDEs) have shown strong potential for modeling irregular time series, yet they still face challenges in capturing complex dynamic temporal patterns and supporting continuous TSG. To address these limitations, we propose MN-TSG, a novel framework that explores Mixture-of-Experts (MoE)-based NCDEs and integrates them with existing TSG models for irregular and continuous generation tasks.
>   The core of MN-TSG lies in a MoE-NCDE architecture with dynamically parameterized expert functions and a decoupled design that facilitates more effective optimization of MoE dynamics. Furthermore, we leverage existing TSG models to learn the joint distribution over the mixture of experts and the generated time series. This enables the framework not only to generate new samples, but also to produce appropriate expert configurations tailored to each sample, thereby supporting refined continuous TSG.
>   Extensive experiments on ten public and synthetic datasets demonstrate the effectiveness of MN-TSG, consistently outperforming strong TSG baselines on both irregular-to-regular and irregular-to-continuous generation tasks.

