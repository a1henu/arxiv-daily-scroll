---
layout: default
title: An Efficient Long-Context Ranking Architecture With Calibrated LLM Distillation: Application to Person-Job Fit
---

# An Efficient Long-Context Ranking Architecture With Calibrated LLM Distillation: Application to Person-Job Fit
**arXiv**：[2601.10321v1](https://arxiv.org/abs/2601.10321) · [PDF](https://arxiv.org/pdf/2601.10321.pdf)  
**作者**：Warren Jouanneau, Emma Jouffroy, Marc Palyart  

**一句话要点**：提出基于晚交叉注意力和LLM蒸馏的长上下文重排架构，用于高效人岗匹配。

**关键词**：长上下文处理, 晚交叉注意力, LLM蒸馏, 人岗匹配, 重排模型, 校准技术

## 3 点简述
- 核心问题：长简历和多语言项目简介下，实时人岗匹配效率低且易受历史数据偏见影响。
- 方法要点：采用晚交叉注意力分解长输入，利用生成式LLM生成细粒度监督信号进行蒸馏训练。
- 实验或效果：在相关性、排序和校准指标上优于现有基线，实现一致且可解释的匹配。

## 摘要（原文）

> Finding the most relevant person for a job proposal in real time is challenging, especially when resumes are long, structured, and multilingual. In this paper, we propose a re-ranking model based on a new generation of late cross-attention architecture, that decomposes both resumes and project briefs to efficiently handle long-context inputs with minimal computational overhead. To mitigate historical data biases, we use a generative large language model (LLM) as a teacher, generating fine-grained, semantically grounded supervision. This signal is distilled into our student model via an enriched distillation loss function. The resulting model produces skill-fit scores that enable consistent and interpretable person-job matching. Experiments on relevance, ranking, and calibration metrics demonstrate that our approach outperforms state-of-the-art baselines.

