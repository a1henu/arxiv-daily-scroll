---
layout: default
title: Data Assessment for Embodied Intelligence
---

# Data Assessment for Embodied Intelligence
**arXiv**：[2511.09119v1](https://arxiv.org/abs/2511.09119) · [PDF](https://arxiv.org/pdf/2511.09119.pdf)  
**作者**：Jiahao Xiao, Bowen Yan, Jianbo Zhang, Jia Wang, Chunyi Li, Zhengxue Cheng, Guangtao Zhai  

**一句话要点**：提出多样性熵与可学习性算法以评估具身智能数据集

**关键词**：具身智能, 数据集评估, 多样性熵, 可学习性, 多模态表示, 数据驱动工具

## 3 点简述
- 核心问题：具身数据多模态特性使数据集信息量与可学习性评估困难
- 方法要点：构建统一多模态表示，定义多样性熵，开发无需训练的可学习性量化算法
- 实验或效果：在模拟与真实数据集验证，提供可操作见解以改进数据集

## 摘要（原文）

> In embodied intelligence, datasets play a pivotal role, serving as both a knowledge repository and a conduit for information transfer. The two most critical attributes of a dataset are the amount of information it provides and how easily this information can be learned by models. However, the multimodal nature of embodied data makes evaluating these properties particularly challenging. Prior work has largely focused on diversity, typically counting tasks and scenes or evaluating isolated modalities, which fails to provide a comprehensive picture of dataset diversity. On the other hand, the learnability of datasets has received little attention and is usually assessed post-hoc through model training, an expensive, time-consuming process that also lacks interpretability, offering little guidance on how to improve a dataset. In this work, we address both challenges by introducing two principled, data-driven tools. First, we construct a unified multimodal representation for each data sample and, based on it, propose diversity entropy, a continuous measure that characterizes the amount of information contained in a dataset. Second, we introduce the first interpretable, data-driven algorithm to efficiently quantify dataset learnability without training, enabling researchers to assess a dataset's learnability immediately upon its release. We validate our algorithm on both simulated and real-world embodied datasets, demonstrating that it yields faithful, actionable insights that enable researchers to jointly improve diversity and learnability. We hope this work provides a foundation for designing higher-quality datasets that advance the development of embodied intelligence.

