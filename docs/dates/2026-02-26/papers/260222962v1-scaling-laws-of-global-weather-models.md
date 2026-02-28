---
layout: default
title: Scaling Laws of Global Weather Models
---

# Scaling Laws of Global Weather Models
**arXiv**：[2602.22962v1](https://arxiv.org/abs/2602.22962) · [PDF](https://arxiv.org/pdf/2602.22962.pdf)  
**作者**：Yuejiang Yu, Langwen Huang, Alexandru Calotoiu, Torsten Hoefler  

**一句话要点**：分析全球天气模型缩放定律以优化训练效率与性能

**关键词**：天气预测模型, 缩放定律, 数据驱动模型, 计算优化, 模型架构分析

## 3 点简述
- 核心问题：探索模型性能与模型大小、数据集大小和计算预算的缩放关系
- 方法要点：通过实证分析，比较不同模型在数据缩放、参数效率和硬件利用方面的表现
- 实验或效果：发现天气模型偏好宽度而非深度，计算预算下延长训练优于增大模型

## 摘要（原文）

> Data-driven models are revolutionizing weather forecasting. To optimize training efficiency and model performance, this paper analyzes empirical scaling laws within this domain. We investigate the relationship between model performance (validation loss) and three key factors: model size ($N$), dataset size ($D$), and compute budget ($C$). Across a range of models, we find that Aurora exhibits the strongest data-scaling behavior: increasing the training dataset by 10x reduces validation loss by up to 3.2x. GraphCast demonstrates the highest parameter efficiency, yet suffers from limited hardware utilization. Our compute-optimal analysis indicates that, under fixed compute budgets, allocating resources to longer training durations yields greater performance gains than increasing model size. Furthermore, we analyze model shape and uncover scaling behaviors that differ fundamentally from those observed in language models: weather forecasting models consistently favor increased width over depth. These findings suggest that future weather models should prioritize wider architectures and larger effective training datasets to maximize predictive performance.

