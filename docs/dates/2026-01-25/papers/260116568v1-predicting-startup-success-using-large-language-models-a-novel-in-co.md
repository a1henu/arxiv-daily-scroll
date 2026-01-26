---
layout: default
title: Predicting Startup Success Using Large Language Models: A Novel In-Context Learning Approach
---

# Predicting Startup Success Using Large Language Models: A Novel In-Context Learning Approach
**arXiv**：[2601.16568v1](https://arxiv.org/abs/2601.16568) · [PDF](https://arxiv.org/pdf/2601.16568.pdf)  
**作者**：Abdurahman Maarouf, Alket Bakiaj, Stefan Feuerriegel  

**一句话要点**：提出kNN-ICL框架，利用大语言模型进行上下文学习以预测早期初创企业成功

**关键词**：初创企业成功预测, 上下文学习, 大语言模型, k近邻算法, 风险投资决策, 数据稀缺环境

## 3 点简述
- 核心问题：早期初创企业成功预测因数据稀缺而困难，传统机器学习方法受限。
- 方法要点：基于k近邻选择相似初创企业作为示例，无需模型训练，实现上下文学习。
- 实验或效果：在Crunchbase数据上，kNN-ICL比监督学习和普通上下文学习准确率更高，仅需50个示例即可达到高平衡准确率。

## 摘要（原文）

> Venture capital (VC) investments in early-stage startups that end up being successful can yield high returns. However, predicting early-stage startup success remains challenging due to data scarcity (e.g., many VC firms have information about only a few dozen of early-stage startups and whether they were successful). This limits the effectiveness of traditional machine learning methods that rely on large labeled datasets for model training. To address this challenge, we propose an in-context learning framework for startup success prediction using large language models (LLMs) that requires no model training and leverages only a small set of labeled startups as demonstration examples. Specifically, we propose a novel k-nearest-neighbor-based in-context learning framework, called kNN-ICL, which selects the most relevant past startups as examples based on similarity. Using real-world profiles from Crunchbase, we find that the kNN-ICL approach achieves higher prediction accuracy than supervised machine learning baselines and vanilla in-context learning. Further, we study how performance varies with the number of in-context examples and find that a high balanced accuracy can be achieved with as few as 50 examples. Together, we demonstrate that in-context learning can serve as a decision-making tool for VC firms operating in data-scarce environments.

