---
layout: default
title: Towards Anytime-Valid Statistical Watermarking
---

# Towards Anytime-Valid Statistical Watermarking
**arXiv**：[2602.17608v1](https://arxiv.org/abs/2602.17608) · [PDF](https://arxiv.org/pdf/2602.17608.pdf)  
**作者**：Baihe Huang, Eric Xu, Kannan Ramchandran, Jiantao Jiao, Michael I. Jordan  

**一句话要点**：提出基于e值的锚定水印框架，统一最优采样与任意时间有效推断以检测LLM生成文本

**关键词**：统计水印, 任意时间有效推断, e值, 超鞅, 大语言模型检测, 最优采样

## 3 点简述
- 核心问题：现有统计水印方法缺乏采样分布选择原则，且固定范围假设检验不支持有效早期停止
- 方法要点：利用锚定分布近似目标模型，构建检测过程的测试超鞅，实现任意时间有效推断
- 实验或效果：在基准测试中，样本效率显著提升，检测所需平均令牌预算减少13-15%

## 摘要（原文）

> The proliferation of Large Language Models (LLMs) necessitates efficient mechanisms to distinguish machine-generated content from human text. While statistical watermarking has emerged as a promising solution, existing methods suffer from two critical limitations: the lack of a principled approach for selecting sampling distributions and the reliance on fixed-horizon hypothesis testing, which precludes valid early stopping. In this paper, we bridge this gap by developing the first e-value-based watermarking framework, Anchored E-Watermarking, that unifies optimal sampling with anytime-valid inference. Unlike traditional approaches where optional stopping invalidates Type-I error guarantees, our framework enables valid, anytime-inference by constructing a test supermartingale for the detection process. By leveraging an anchor distribution to approximate the target model, we characterize the optimal e-value with respect to the worst-case log-growth rate and derive the optimal expected stopping time. Our theoretical claims are substantiated by simulations and evaluations on established benchmarks, showing that our framework can significantly enhance sample efficiency, reducing the average token budget required for detection by 13-15% relative to state-of-the-art baselines.

