---
layout: default
title: Proxy-Guided Measurement Calibration
---

# Proxy-Guided Measurement Calibration
**arXiv**：[2603.09288v1](https://arxiv.org/abs/2603.09288) · [PDF](https://arxiv.org/pdf/2603.09288.pdf)  
**作者**：Saketh Vishnubhatla, Shu Wan, Andre Harrison, Adrienne Raglin, Huan Liu  

**一句话要点**：提出基于代理变量的测量校准框架，以纠正聚合结果变量中的系统误差。

**关键词**：测量校准, 系统误差, 代理变量, 变分自编码器, 因果图, 灾害损失

## 3 点简述
- 核心问题：聚合结果变量（如灾害损失数据）存在系统测量误差，影响下游分析。
- 方法要点：利用因果图分离内容和偏差潜变量，通过代理变量识别偏差，采用变分自编码器进行解耦。
- 实验或效果：在合成数据、半合成数据和真实灾害损失报告案例中评估方法有效性。

## 摘要（原文）

> Aggregate outcome variables collected through surveys and administrative records are often subject to systematic measurement error. For instance, in disaster loss databases, county-level losses reported may differ from the true damages due to variations in on-the-ground data collection capacity, reporting practices, and event characteristics. Such miscalibration complicates downstream analysis and decision-making. We study the problem of outcome miscalibration and propose a framework guided by proxy variables for estimating and correcting the systematic errors. We model the data-generating process using a causal graph that separates latent content variables driving the true outcome from the latent bias variables that induce systematic errors. The key insight is that proxy variables that depend on the true outcome but are independent of the bias mechanism provide identifying information for quantifying the bias. Leveraging this structure, we introduce a two-stage approach that utilizes variational autoencoders to disentangle content and bias latents, enabling us to estimate the effect of bias on the outcome of interest. We analyze the assumptions underlying our approach and evaluate it on synthetic data, semi-synthetic datasets derived from randomized trials, and a real-world case study of disaster loss reporting.

