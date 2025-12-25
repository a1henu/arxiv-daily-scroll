---
layout: default
title: Can Agentic AI Match the Performance of Human Data Scientists?
---

# Can Agentic AI Match the Performance of Human Data Scientists?
**arXiv**：[2512.20959v1](https://arxiv.org/abs/2512.20959) · [PDF](https://arxiv.org/pdf/2512.20959.pdf)  
**作者**：An Luo, Jin Du, Fangqiao Tian, Xun Xian, Robert Specht, Ganghua Wang, Xuan Bi, Charles Fleming, Jayanth Srinivasa, Ashish Kundu, Mingyi Hong, Jie Ding  

**一句话要点**：揭示代理AI在数据科学中因缺乏领域知识而性能受限，通过隐藏变量预测任务验证

**关键词**：代理AI, 数据科学, 领域知识, 隐藏变量, 预测任务, 图像数据

## 3 点简述
- 核心问题：代理AI能否匹配人类数据科学家利用领域知识处理复杂数据的能力
- 方法要点：设计预测任务，将关键潜在变量隐藏于图像数据而非表格特征中
- 实验或效果：在合成保险数据集上，代理AI表现不佳，人类专家能识别隐藏变量

## 摘要（原文）

> Data science plays a critical role in transforming complex data into actionable insights across numerous domains. Recent developments in large language models (LLMs) have significantly automated data science workflows, but a fundamental question persists: Can these agentic AI systems truly match the performance of human data scientists who routinely leverage domain-specific knowledge? We explore this question by designing a prediction task where a crucial latent variable is hidden in relevant image data instead of tabular features. As a result, agentic AI that generates generic codes for modeling tabular data cannot perform well, while human experts could identify the important hidden variable using domain knowledge. We demonstrate this idea with a synthetic dataset for property insurance. Our experiments show that agentic AI that relies on generic analytics workflow falls short of methods that use domain-specific insights. This highlights a key limitation of the current agentic AI for data science and underscores the need for future research to develop agentic AI systems that can better recognize and incorporate domain knowledge.

