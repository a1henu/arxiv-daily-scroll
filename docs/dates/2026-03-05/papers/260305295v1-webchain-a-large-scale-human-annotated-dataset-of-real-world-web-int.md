---
layout: default
title: WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces
---

# WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces
**arXiv**：[2603.05295v1](https://arxiv.org/abs/2603.05295) · [PDF](https://arxiv.org/pdf/2603.05295.pdf)  
**作者**：Sicheng Fan, Rui Wan, Yifei Leng, Gaoning Liang, Li Ling, Yanyi Shang, Dehan Kong  

**一句话要点**：提出WebChain数据集以加速可复现的网页代理研究，包含大规模真实世界交互轨迹。

**关键词**：网页代理, 多模态数据集, 交互轨迹, 真实世界数据, 可复现研究, 双中训练

## 3 点简述
- 核心问题：现有网页代理研究缺乏大规模、真实世界、多模态标注的交互数据，限制可复现性和性能评估。
- 方法要点：通过可扩展管道收集31,725条轨迹，提供视觉、结构和动作的三重对齐数据，支持多模态监督。
- 实验或效果：基于数据集提出双中训练方法，在WebChainBench等基准上实现最先进性能，促进网页代理开发。

## 摘要（原文）

> We introduce WebChain, the largest open-source dataset of human-annotated trajectories on real-world websites, designed to accelerate reproducible research in web agents. It contains 31,725 trajectories and 318k steps, featuring a core Triple Alignment of visual, structural, and action data to provide rich, multi-modal supervision. The data is collected via a scalable pipeline that ensures coverage of complex, high-value tasks often missed by synthetic methods. Leveraging this dataset, we propose a Dual Mid-Training recipe that decouples spatial grounding from planning, achieving state-of-the-art performance on our proposed WebChainBench and other public GUI benchmarks. Our work provides the data and insights necessary to build and rigorously evaluate the next generation of scalable web agents.

