---
layout: default
title: The Chicken and Egg Dilemma: Co-optimizing Data and Model Configurations for LLMs
---

# The Chicken and Egg Dilemma: Co-optimizing Data and Model Configurations for LLMs
**arXiv**：[2602.08351v1](https://arxiv.org/abs/2602.08351) · [PDF](https://arxiv.org/pdf/2602.08351.pdf)  
**作者**：Zhiliang Chen, Alfred Wei Lun Leong, Shao Yong Ong, Apivich Hemachandram, Gregory Kang Ruey Lau, Chuan-Sheng Foo, Zhengyuan Liu, Nancy F. Chen, Bryan Kian Hsiang Low  

**一句话要点**：提出JoBS方法，通过性能预测器辅助贝叶斯优化，高效联合优化LLM的数据与模型配置。

**关键词**：大语言模型训练, 联合优化, 贝叶斯优化, 性能预测器, 数据配置优化, 模型配置优化

## 3 点简述
- 核心问题：LLM训练中数据与模型配置的联合优化存在鸡与蛋困境，现有方法常忽略其交互。
- 方法要点：使用缩放定律启发的性能预测器，结合贝叶斯优化，通过部分预算学习预测器以降低全训练成本。
- 实验或效果：在相同优化预算下，JoBS优于现有多保真度贝叶斯优化及单独优化方法，平均遗憾更小。

## 摘要（原文）

> Co-optimizing data and model configurations for training LLMs presents a classic chicken-and-egg dilemma: The best training data configuration (e.g., data mixture) for a downstream task depends on the chosen model configuration (e.g., model architecture), and vice versa. However, jointly optimizing both data and model configurations is often deemed intractable, and existing methods focus on either data or model optimization without considering their interaction. We introduce JoBS, an approach that uses a scaling-law-inspired performance predictor to aid Bayesian optimization (BO) in jointly optimizing LLM training data and model configurations efficiently. JoBS allocates a portion of the optimization budget to learn an LLM performance predictor that predicts how promising a training configuration is from a small number of training steps. The remaining budget is used to perform BO entirely with the predictor, effectively amortizing the cost of running full-training runs. We study JoBS's average regret and devise the optimal budget allocation to minimize regret. JoBS outperforms existing multi-fidelity BO baselines, as well as data and model optimization approaches across diverse LLM tasks under the same optimization budget.

