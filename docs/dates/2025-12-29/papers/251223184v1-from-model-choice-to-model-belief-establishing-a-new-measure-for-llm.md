---
layout: default
title: From Model Choice to Model Belief: Establishing a New Measure for LLM-Based Research
---

# From Model Choice to Model Belief: Establishing a New Measure for LLM-Based Research
**arXiv**：[2512.23184v1](https://arxiv.org/abs/2512.23184) · [PDF](https://arxiv.org/pdf/2512.23184.pdf)  
**作者**：Hongshen Sun, Juanjuan Zhang  

**一句话要点**：提出模型信念以提升大语言模型生成数据的统计效率

**关键词**：大语言模型, 模型信念, 统计效率, 需求估计, 概率建模

## 3 点简述
- 问题：现有方法将LLM输出视为单点数据，未充分利用其概率信息。
- 方法：基于LLM的token级概率定义模型信念，捕获选择分布。
- 效果：在需求估计实验中，模型信念比模型选择更准确，计算效率提升约20倍。

## 摘要（原文）

> Large language models (LLMs) are increasingly used to simulate human behavior, but common practices to use LLM-generated data are inefficient. Treating an LLM's output ("model choice") as a single data point underutilizes the information inherent to the probabilistic nature of LLMs. This paper introduces and formalizes "model belief," a measure derived from an LLM's token-level probabilities that captures the model's belief distribution over choice alternatives in a single generation run. The authors prove that model belief is asymptotically equivalent to the mean of model choices (a non-trivial property) but forms a more statistically efficient estimator, with lower variance and a faster convergence rate. Analogous properties are shown to hold for smooth functions of model belief and model choice often used in downstream applications. The authors demonstrate the performance of model belief through a demand estimation study, where an LLM simulates consumer responses to different prices. In practical settings with limited numbers of runs, model belief explains and predicts ground-truth model choice better than model choice itself, and reduces the computation needed to reach sufficiently accurate estimates by roughly a factor of 20. The findings support using model belief as the default measure to extract more information from LLM-generated data.

