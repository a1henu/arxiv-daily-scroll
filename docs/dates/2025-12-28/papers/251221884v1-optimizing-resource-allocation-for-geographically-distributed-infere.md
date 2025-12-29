---
layout: default
title: Optimizing Resource Allocation for Geographically-Distributed Inference by Large Language Models
---

# Optimizing Resource Allocation for Geographically-Distributed Inference by Large Language Models
**arXiv**：[2512.21884v1](https://arxiv.org/abs/2512.21884) · [PDF](https://arxiv.org/pdf/2512.21884.pdf)  
**作者**：Tingyang Sun, Ting He, Bo Ji, Parimal Parag  

**一句话要点**：提出优化块放置与请求路由的资源分配方法，以提升地理分布式大语言模型推理性能

**关键词**：分布式推理, 资源分配优化, 大语言模型, 块放置, 请求路由, 性能建模

## 3 点简述
- 核心问题：分布式LLM推理中资源分配（块放置与请求路由）的优化问题未知
- 方法要点：建立实验验证的性能模型，将离线优化建模为混合整数线性规划问题并提供多项式复杂度算法
- 实验或效果：通过实验和模拟验证，相比现有方案显著减少推理时间，并开发轻量级CPU模拟器

## 摘要（原文）

> Large language models have demonstrated extraordinary performance in many AI tasks but are expensive to use, even after training, due to their requirement of high-end GPUs. Recently, a distributed system called PETALS was developed to lower the barrier for deploying LLMs by splitting the model blocks across multiple servers with low-end GPUs distributed over the Internet, which was much faster than swapping the model parameters between the GPU memory and other cheaper but slower local storage media. However, the performance of such a distributed system critically depends on the resource allocation, and how to do so optimally remains unknown. In this work, we present the first systematic study of the resource allocation problem in distributed LLM inference, with focus on two important decisions: block placement and request routing. Our main results include: experimentally validated performance models that can predict the inference performance under given block placement and request routing decisions, a formulation of the offline optimization of block placement and request routing as a mixed integer linear programming problem together with the NP-hardness proof and a polynomial-complexity algorithm with guaranteed performance, and an adaptation of the offline algorithm for the online setting with the same performance guarantee under bounded load. Through both experiments and experimentally-validated simulations, we have verified that the proposed solution can substantially reduce the inference time compared to the state-of-the-art solution in diverse settings with geographically-distributed servers. As a byproduct, we have also developed a light-weighted CPU-only simulator capable of predicting the performance of distributed LLM inference on GPU servers, which can evaluate large deployments and facilitate future research for researchers with limited GPU access.

