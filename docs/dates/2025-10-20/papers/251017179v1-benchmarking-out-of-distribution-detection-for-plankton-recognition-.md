---
layout: default
title: Benchmarking Out-of-Distribution Detection for Plankton Recognition: A Systematic Evaluation of Advanced Methods in Marine Ecological Monitoring
---

# Benchmarking Out-of-Distribution Detection for Plankton Recognition: A Systematic Evaluation of Advanced Methods in Marine Ecological Monitoring
**arXiv**：[2510.17179v1](https://arxiv.org/abs/2510.17179) · [PDF](https://arxiv.org/pdf/2510.17179.pdf)  
**作者**：Yingzi Han, Jiakai He, Chuanlong Xie, Jianping Li  

**一句话要点**：系统评估浮游生物识别中的OoD检测方法，ViM在远分布偏移场景表现最佳

**关键词**：浮游生物识别, 分布外检测, 基准评估, 计算机视觉, 海洋生态监测

## 3 点简述
- 浮游生物识别模型面临训练与测试数据分布偏移问题，导致部署时错误
- 基于DYB-PlanktonNet数据集构建OoD基准，评估22种检测方法
- ViM方法在远分布偏移场景显著优于其他，提升关键指标

## 摘要（原文）

> Automated plankton recognition models face significant challenges during
> real-world deployment due to distribution shifts (Out-of-Distribution, OoD)
> between training and test data. This stems from plankton's complex
> morphologies, vast species diversity, and the continuous discovery of novel
> species, which leads to unpredictable errors during inference. Despite rapid
> advancements in OoD detection methods in recent years, the field of plankton
> recognition still lacks a systematic integration of the latest computer vision
> developments and a unified benchmark for large-scale evaluation. To address
> this, this paper meticulously designed a series of OoD benchmarks simulating
> various distribution shift scenarios based on the DYB-PlanktonNet dataset
> \cite{875n-f104-21}, and systematically evaluated twenty-two OoD detection
> methods. Extensive experimental results demonstrate that the ViM
> \cite{wang2022vim} method significantly outperforms other approaches in our
> constructed benchmarks, particularly excelling in Far-OoD scenarios with
> substantial improvements in key metrics. This comprehensive evaluation not only
> provides a reliable reference for algorithm selection in automated plankton
> recognition but also lays a solid foundation for future research in plankton
> OoD detection. To our knowledge, this study marks the first large-scale,
> systematic evaluation and analysis of Out-of-Distribution data detection
> methods in plankton recognition. Code is available at
> https://github.com/BlackJack0083/PlanktonOoD.

