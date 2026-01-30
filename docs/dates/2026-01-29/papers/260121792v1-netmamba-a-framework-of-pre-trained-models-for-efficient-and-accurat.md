---
layout: default
title: NetMamba+: A Framework of Pre-trained Models for Efficient and Accurate Network Traffic Classification
---

# NetMamba+: A Framework of Pre-trained Models for Efficient and Accurate Network Traffic Classification
**arXiv**：[2601.21792v1](https://arxiv.org/abs/2601.21792) · [PDF](https://arxiv.org/pdf/2601.21792.pdf)  
**作者**：Tongze Wang, Xiaohui Xie, Wenduo Wang, Chuyi Wang, Jinzhou Liu, Boyan Huang, Yannan Hu, Youjian Zhao, Yong Cui  

**一句话要点**：提出NetMamba+框架，通过高效架构与多模态表示解决加密流量分类中的计算效率与特征保留问题。

**关键词**：网络流量分类, Mamba架构, 多模态表示, 长尾分布, 少样本学习, 在线系统

## 3 点简述
- 核心问题：加密流量分类面临Transformer计算效率低、特征表示偏差和长尾分布处理差。
- 方法要点：结合Mamba与Flash Attention机制，设计多模态表示方案和标签分布感知微调策略。
- 实验或效果：在四大分类任务中F1分数提升达6.44%，推理吞吐量提高1.7倍，并展示少样本学习能力。

## 摘要（原文）

> With the rapid growth of encrypted network traffic, effective traffic classification has become essential for network security and quality of service management. Current machine learning and deep learning approaches for traffic classification face three critical challenges: computational inefficiency of Transformer architectures, inadequate traffic representations with loss of crucial byte-level features while retaining detrimental biases, and poor handling of long-tail distributions in real-world data. We propose NetMamba+, a framework that addresses these challenges through three key innovations: (1) an efficient architecture considering Mamba and Flash Attention mechanisms, (2) a multimodal traffic representation scheme that preserves essential traffic information while eliminating biases, and (3) a label distribution-aware fine-tuning strategy. Evaluation experiments on massive datasets encompassing four main classification tasks showcase NetMamba+'s superior classification performance compared to state-of-the-art baselines, with improvements of up to 6.44\% in F1 score. Moreover, NetMamba+ demonstrates excellent efficiency, achieving 1.7x higher inference throughput than the best baseline while maintaining comparably low memory usage. Furthermore, NetMamba+ exhibits superior few-shot learning abilities, achieving better classification performance with fewer labeled data. Additionally, we implement an online traffic classification system that demonstrates robust real-world performance with a throughput of 261.87 Mb/s. As the first framework to adapt Mamba architecture for network traffic classification, NetMamba+ opens new possibilities for efficient and accurate traffic analysis in complex network environments.

