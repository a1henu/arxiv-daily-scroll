---
layout: default
title: Balanced Anomaly-guided Ego-graph Diffusion Model for Inductive Graph Anomaly Detection
---

# Balanced Anomaly-guided Ego-graph Diffusion Model for Inductive Graph Anomaly Detection
**arXiv**：[2602.05232v1](https://arxiv.org/abs/2602.05232) · [PDF](https://arxiv.org/pdf/2602.05232.pdf)  
**作者**：Chunyu Wei, Siyuan He, Yu Wang, Yueguo Chen, Yunhai Wang, Bing Bai, Yidong Zhang, Yong Xie, Shunming Zhang, Fei Wang  

**一句话要点**：提出平衡异常引导的自我图扩散模型，以解决动态图异常检测中的归纳学习和类别不平衡问题。

**关键词**：图异常检测, 归纳学习, 类别不平衡, 自我图扩散, 异常合成, 动态图建模

## 3 点简述
- 核心问题：现有图异常检测方法面临静态归纳学习框架和极端类别不平衡，导致模型在动态网络中泛化能力差。
- 方法要点：采用离散自我图扩散模型捕获异常局部拓扑，结合课程异常增强机制动态生成平衡合成数据。
- 实验或效果：在五个数据集上验证了框架的有效性，提升了异常检测性能和泛化能力。

## 摘要（原文）

> Graph anomaly detection (GAD) is crucial in applications like fraud detection and cybersecurity. Despite recent advancements using graph neural networks (GNNs), two major challenges persist. At the model level, most methods adopt a transductive learning paradigm, which assumes static graph structures, making them unsuitable for dynamic, evolving networks. At the data level, the extreme class imbalance, where anomalous nodes are rare, leads to biased models that fail to generalize to unseen anomalies. These challenges are interdependent: static transductive frameworks limit effective data augmentation, while imbalance exacerbates model distortion in inductive learning settings. To address these challenges, we propose a novel data-centric framework that integrates dynamic graph modeling with balanced anomaly synthesis. Our framework features: (1) a discrete ego-graph diffusion model, which captures the local topology of anomalies to generate ego-graphs aligned with anomalous structural distribution, and (2) a curriculum anomaly augmentation mechanism, which dynamically adjusts synthetic data generation during training, focusing on underrepresented anomaly patterns to improve detection and generalization. Experiments on five datasets demonstrate that the effectiveness of our framework.

