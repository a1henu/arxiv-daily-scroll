---
layout: default
title: Benchmarking Unlearning for Vision Transformers
---

# Benchmarking Unlearning for Vision Transformers
**arXiv**：[2602.20114v1](https://arxiv.org/abs/2602.20114) · [PDF](https://arxiv.org/pdf/2602.20114.pdf)  
**作者**：Kairan Zhao, Iurie Luca, Peter Triantafillou  

**一句话要点**：首次为视觉Transformer建立机器遗忘基准，评估不同算法与协议的性能

**关键词**：机器遗忘, 视觉Transformer, 基准测试, 训练数据记忆化, 遗忘算法评估

## 3 点简述
- 核心问题：机器遗忘研究在视觉任务中集中于CNN，缺乏针对视觉Transformer的基准。
- 方法要点：使用不同数据集、算法和遗忘协议，聚焦基于训练数据记忆化的算法。
- 实验或效果：评估遗忘质量与准确性，为现有和未来算法提供可复现比较基础。

## 摘要（原文）

> Research in machine unlearning (MU) has gained strong momentum: MU is now widely regarded as a critical capability for building safe and fair AI. In parallel, research into transformer architectures for computer vision tasks has been highly successful: Increasingly, Vision Transformers (VTs) emerge as strong alternatives to CNNs. Yet, MU research for vision tasks has largely centered on CNNs, not VTs. While benchmarking MU efforts have addressed LLMs, diffusion models, and CNNs, none exist for VTs. This work is the first to attempt this, benchmarking MU algorithm performance in different VT families (ViT and Swin-T) and at different capacities. The work employs (i) different datasets, selected to assess the impacts of dataset scale and complexity; (ii) different MU algorithms, selected to represent fundamentally different approaches for MU; and (iii) both single-shot and continual unlearning protocols. Additionally, it focuses on benchmarking MU algorithms that leverage training data memorization, since leveraging memorization has been recently discovered to significantly improve the performance of previously SOTA algorithms. En route, the work characterizes how VTs memorize training data relative to CNNs, and assesses the impact of different memorization proxies on performance. The benchmark uses unified evaluation metrics that capture two complementary notions of forget quality along with accuracy on unseen (test) data and on retained data. Overall, this work offers a benchmarking basis, enabling reproducible, fair, and comprehensive comparisons of existing (and future) MU algorithms on VTs. And, for the first time, it sheds light on how well existing algorithms work in VT settings, establishing a promising reference performance baseline.

