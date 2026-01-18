---
layout: default
title: On the origin of neural scaling laws: from random graphs to natural language
---

# On the origin of neural scaling laws: from random graphs to natural language
**arXiv**：[2601.10684v1](https://arxiv.org/abs/2601.10684) · [PDF](https://arxiv.org/pdf/2601.10684.pdf)  
**作者**：Maissam Barkeshli, Alberto Alfarano, Andrey Gromov  

**一句话要点**：通过随机图与简化语言模型探究神经缩放定律起源，揭示其不依赖数据幂律结构

**关键词**：神经缩放定律, 随机图, Transformer, 语言模型, 参数效率, 计算最优曲线

## 3 点简述
- 核心问题：神经缩放定律是否源于数据中的幂律结构，作者在简化设置中检验其起源
- 方法要点：使用可调复杂度的随机图训练Transformer预测随机游走，并系统简化自然语言生成模型
- 实验或效果：在无数据幂律相关性的随机图中观察到缩放定律，缩放指数随语言复杂度单调演化

## 摘要（原文）

> Scaling laws have played a major role in the modern AI revolution, providing practitioners predictive power over how the model performance will improve with increasing data, compute, and number of model parameters. This has spurred an intense interest in the origin of neural scaling laws, with a common suggestion being that they arise from power law structure already present in the data. In this paper we study scaling laws for transformers trained to predict random walks (bigrams) on graphs with tunable complexity. We demonstrate that this simplified setting already gives rise to neural scaling laws even in the absence of power law structure in the data correlations. We further consider dialing down the complexity of natural language systematically, by training on sequences sampled from increasingly simplified generative language models, from 4,2,1-layer transformer language models down to language bigrams, revealing a monotonic evolution of the scaling exponents. Our results also include scaling laws obtained from training on random walks on random graphs drawn from Erdös-Renyi and scale-free Barabási-Albert ensembles. Finally, we revisit conventional scaling laws for language modeling, demonstrating that several essential results can be reproduced using 2 layer transformers with context length of 50, provide a critical analysis of various fits used in prior literature, demonstrate an alternative method for obtaining compute optimal curves as compared with current practice in published literature, and provide preliminary evidence that maximal update parameterization may be more parameter efficient than standard parameterization.

