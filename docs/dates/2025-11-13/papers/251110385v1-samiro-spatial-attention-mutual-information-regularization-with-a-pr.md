---
layout: default
title: SAMIRO: Spatial Attention Mutual Information Regularization with a Pre-trained Model as Oracle for Lane Detection
---

# SAMIRO: Spatial Attention Mutual Information Regularization with a Pre-trained Model as Oracle for Lane Detection
**arXiv**：[2511.10385v1](https://arxiv.org/abs/2511.10385) · [PDF](https://arxiv.org/pdf/2511.10385.pdf)  
**作者**：Hyunjong Lee, Jangho Lee, Jaekoo Lee  

**一句话要点**：提出SAMIRO以解决车道检测中的环境挑战，通过预训练模型知识转移提升性能。

**关键词**：车道检测, 知识转移, 空间注意力, 互信息正则化, 预训练模型, 基准测试

## 3 点简述
- 核心问题：真实环境如背景杂乱、光照变化和遮挡对数据驱动车道检测构成挑战。
- 方法要点：使用预训练模型作为Oracle，通过空间注意力互信息正则化保留领域无关空间信息。
- 实验或效果：在CULane等基准测试中，SAMIRO可插拔集成多种模型，一致提升性能。

## 摘要（原文）

> Lane detection is an important topic in the future mobility solutions. Real-world environmental challenges such as background clutter, varying illumination, and occlusions pose significant obstacles to effective lane detection, particularly when relying on data-driven approaches that require substantial effort and cost for data collection and annotation. To address these issues, lane detection methods must leverage contextual and global information from surrounding lanes and objects. In this paper, we propose a Spatial Attention Mutual Information Regularization with a pre-trained model as an Oracle, called SAMIRO. SAMIRO enhances lane detection performance by transferring knowledge from a pretrained model while preserving domain-agnostic spatial information. Leveraging SAMIRO's plug-and-play characteristic, we integrate it into various state-of-the-art lane detection approaches and conduct extensive experiments on major benchmarks such as CULane, Tusimple, and LLAMAS. The results demonstrate that SAMIRO consistently improves performance across different models and datasets. The code will be made available upon publication.

