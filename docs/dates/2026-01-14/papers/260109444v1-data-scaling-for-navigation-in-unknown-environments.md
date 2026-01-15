---
layout: default
title: Data Scaling for Navigation in Unknown Environments
---

# Data Scaling for Navigation in Unknown Environments
**arXiv**：[2601.09444v1](https://arxiv.org/abs/2601.09444) · [PDF](https://arxiv.org/pdf/2601.09444.pdf)  
**作者**：Lauri Suomela, Naoki Takahata, Sasanka Kuruppu Arachchige, Harry Edelman, Joni-Kristian Kämäräinen  

**一句话要点**：研究数据规模与多样性对未知环境视觉导航泛化性能的影响

**关键词**：视觉导航, 数据多样性, 模仿学习, 端到端控制, 泛化性能, 众包数据

## 3 点简述
- 核心问题：模仿学习导航策略在训练未见环境中的泛化能力不足
- 方法要点：使用大规模众包数据集，分析数据量和多样性对端到端视觉导航的影响
- 实验或效果：数据多样性比数量更重要，简单回归模型在噪声数据下表现更优

## 摘要（原文）

> Generalization of imitation-learned navigation policies to environments unseen in training remains a major challenge. We address this by conducting the first large-scale study of how data quantity and data diversity affect real-world generalization in end-to-end, map-free visual navigation. Using a curated 4,565-hour crowd-sourced dataset collected across 161 locations in 35 countries, we train policies for point goal navigation and evaluate their closed-loop control performance on sidewalk robots operating in four countries, covering 125 km of autonomous driving.
>   Our results show that large-scale training data enables zero-shot navigation in unknown environments, approaching the performance of policies trained with environment-specific demonstrations. Critically, we find that data diversity is far more important than data quantity. Doubling the number of geographical locations in a training set decreases navigation errors by ~15%, while performance benefit from adding data from existing locations saturates with very little data. We also observe that, with noisy crowd-sourced data, simple regression-based models outperform generative and sequence-based architectures. We release our policies, evaluation setup and example videos on the project page.

