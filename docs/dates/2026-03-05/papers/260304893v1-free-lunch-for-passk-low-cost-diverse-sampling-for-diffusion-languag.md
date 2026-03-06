---
layout: default
title: Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models
---

# Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models
**arXiv**：[2603.04893v1](https://arxiv.org/abs/2603.04893) · [PDF](https://arxiv.org/pdf/2603.04893.pdf)  
**作者**：Sean Lamont, Christian Walder, Paul Montague, Amir Dezfouli, Michael Norrish  

**一句话要点**：提出低成本干预方法以增强扩散语言模型的生成多样性，提升Pass@k性能。

**关键词**：扩散语言模型, 生成多样性, Pass@k, 低成本采样, 特征空间排斥

## 3 点简述
- 核心问题：扩散语言模型采样时样本易重复，浪费计算资源，影响Pass@k任务探索。
- 方法要点：训练免费，通过顺序修改批次样本，在特征空间排斥冗余，增加多样性。
- 实验或效果：在HumanEval和GSM8K基准上，使用LLaDA-8B-Instruct模型，显著提升多样性和Pass@k性能。

## 摘要（原文）

> Diverse outputs in text generation are necessary for effective exploration in complex reasoning tasks, such as code generation and mathematical problem solving. Such Pass@$k$ problems benefit from distinct candidates covering the solution space. However, traditional sampling approaches often waste computational resources on repetitive failure modes. While Diffusion Language Models have emerged as a competitive alternative to the prevailing Autoregressive paradigm, they remain susceptible to this redundancy, with independent samples frequently collapsing into similar modes. To address this, we propose a training free, low cost intervention to enhance generative diversity in Diffusion Language Models. Our approach modifies intermediate samples in a batch sequentially, where each sample is repelled from the feature space of previous samples, actively penalising redundancy. Unlike prior methods that require retraining or beam search, our strategy incurs negligible computational overhead, while ensuring that each sample contributes a unique perspective to the batch. We evaluate our method on the HumanEval and GSM8K benchmarks using the LLaDA-8B-Instruct model. Our results demonstrate significantly improved diversity and Pass@$k$ performance across various temperature settings. As a simple modification to the sampling process, our method offers an immediate, low-cost improvement for current and future Diffusion Language Models in tasks that benefit from diverse solution search. We make our code available at https://github.com/sean-lamont/odd.

