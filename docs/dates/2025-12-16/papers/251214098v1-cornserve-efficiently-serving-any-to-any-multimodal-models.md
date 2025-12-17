---
layout: default
title: Cornserve: Efficiently Serving Any-to-Any Multimodal Models
---

# Cornserve: Efficiently Serving Any-to-Any Multimodal Models
**arXiv**：[2512.14098v1](https://arxiv.org/abs/2512.14098) · [PDF](https://arxiv.org/pdf/2512.14098.pdf)  
**作者**：Jeff J. Ma, Jae-Won Chung, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury  

**一句话要点**：提出Cornserve系统以高效在线服务Any-to-Any多模态模型

**关键词**：多模态模型服务, 异构计算优化, 在线推理系统, 分布式部署, Any-to-Any模型

## 3 点简述
- 核心问题：Any-to-Any模型在输入输出类型、计算路径和规模上存在异构性，导致在线服务效率低。
- 方法要点：Cornserve通过描述计算图，自动规划优化部署，并利用分布式运行时处理异构性。
- 实验效果：相比现有方案，Cornserve提升吞吐量达3.81倍，降低尾部延迟达5.79倍。

## 摘要（原文）

> We present Cornserve, an efficient online serving system for an emerging class of multimodal models called Any-to-Any models. Any-to-Any models accept combinations of text and multimodal data (e.g., image, video, audio) as input and also generate combinations of text and multimodal data as output, introducing request type, computation path, and computation scaling heterogeneity in model serving.
>   Cornserve allows model developers to describe the computation graph of generic Any-to-Any models, which consists of heterogeneous components such as multimodal encoders, autoregressive models like Large Language Models (LLMs), and multimodal generators like Diffusion Transformers (DiTs). Given this, Cornserve's planner automatically finds an optimized deployment plan for the model, including whether and how to disaggregate the model into smaller components based on model and workload characteristics. Cornserve's distributed runtime then executes the model per the plan, efficiently handling Any-to-Any model heterogeneity during online serving. Evaluations show that Cornserve can efficiently serve diverse Any-to-Any models and workloads, delivering up to 3.81$\times$ throughput improvement and up to 5.79$\times$ tail latency reduction over existing solutions.

