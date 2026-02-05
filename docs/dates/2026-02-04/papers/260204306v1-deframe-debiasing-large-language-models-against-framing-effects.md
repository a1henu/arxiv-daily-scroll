---
layout: default
title: DeFrame: Debiasing Large Language Models Against Framing Effects
---

# DeFrame: Debiasing Large Language Models Against Framing Effects
**arXiv**：[2602.04306v1](https://arxiv.org/abs/2602.04306) · [PDF](https://arxiv.org/pdf/2602.04306.pdf)  
**作者**：Kahee Lim, Soyeon Kim, Steven Euijong Whang  

**一句话要点**：提出DeFrame方法以解决大语言模型在框架效应下的隐藏偏见问题

**关键词**：大语言模型, 框架效应, 偏见检测, 去偏方法, 公平性评估

## 3 点简述
- 核心问题：大语言模型在语义等效但表达不同的提示下产生偏见，标准评估难以检测
- 方法要点：引入框架差异概念，开发框架感知去偏方法，提升模型跨框架一致性
- 实验或效果：实验显示该方法减少总体偏见，增强对框架差异的鲁棒性

## 摘要（原文）

> As large language models (LLMs) are increasingly deployed in real-world applications, ensuring their fair responses across demographics has become crucial. Despite many efforts, an ongoing challenge is hidden bias: LLMs appear fair under standard evaluations, but can produce biased responses outside those evaluation settings. In this paper, we identify framing -- differences in how semantically equivalent prompts are expressed (e.g., "A is better than B" vs. "B is worse than A") -- as an underexplored contributor to this gap. We first introduce the concept of "framing disparity" to quantify the impact of framing on fairness evaluation. By augmenting fairness evaluation benchmarks with alternative framings, we find that (1) fairness scores vary significantly with framing and (2) existing debiasing methods improve overall (i.e., frame-averaged) fairness, but often fail to reduce framing-induced disparities. To address this, we propose a framing-aware debiasing method that encourages LLMs to be more consistent across framings. Experiments demonstrate that our approach reduces overall bias and improves robustness against framing disparities, enabling LLMs to produce fairer and more consistent responses.

