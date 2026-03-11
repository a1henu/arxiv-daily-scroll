---
layout: default
title: LCA: Local Classifier Alignment for Continual Learning
---

# LCA: Local Classifier Alignment for Continual Learning
**arXiv**：[2603.09888v1](https://arxiv.org/abs/2603.09888) · [PDF](https://arxiv.org/pdf/2603.09888.pdf)  
**作者**：Tung Tran, Danilo Vasconcellos Vargas, Khoat Than  

**一句话要点**：提出局部分类器对齐损失以解决持续学习中分类器与骨干网络不匹配问题。

**关键词**：持续学习, 灾难性遗忘, 模型对齐, 分类器优化, 骨干网络适应

## 3 点简述
- 核心问题：持续学习模型易受灾难性遗忘影响，分类器与适应后的骨干网络可能不匹配。
- 方法要点：引入局部分类器对齐损失，优化分类器与骨干网络的对齐，提升泛化与鲁棒性。
- 实验或效果：在标准基准测试中表现领先，有时大幅超越现有方法。

## 摘要（原文）

> A fundamental requirement for intelligent systems is the ability to learn continuously under changing environments. However, models trained in this regime often suffer from catastrophic forgetting. Leveraging pre-trained models has recently emerged as a promising solution, since their generalized feature extractors enable faster and more robust adaptation. While some earlier works mitigate forgetting by fine-tuning only on the first task, this approach quickly deteriorates as the number of tasks grows and the data distributions diverge. More recent research instead seeks to consolidate task knowledge into a unified backbone, or adapting the backbone as new tasks arrive. However, such approaches may create a (potential) \textit{mismatch} between task-specific classifiers and the adapted backbone. To address this issue, we propose a novel \textit{Local Classifier Alignment} (LCA) loss to better align the classifier with backbone. Theoretically, we show that this LCA loss can enable the classifier to not only generalize well for all observed tasks, but also improve robustness. Furthermore, we develop a complete solution for continual learning, following the model merging approach and using LCA. Extensive experiments on several standard benchmarks demonstrate that our method often achieves leading performance, sometimes surpasses the state-of-the-art methods with a large margin.

