---
layout: default
title: Estimating problem difficulty without ground truth using Large Language Model comparisons
---

# Estimating problem difficulty without ground truth using Large Language Model comparisons
**arXiv**：[2512.14220v1](https://arxiv.org/abs/2512.14220) · [PDF](https://arxiv.org/pdf/2512.14220.pdf)  
**作者**：Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis  

**一句话要点**：提出LLM比较法以无真值估计问题难度，支持分布外问题评估。

**关键词**：问题难度估计, 大语言模型, Bradley-Terry模型, 分布外评估, 无真值学习, 课程设计

## 3 点简述
- 核心问题：现有难度估计方法依赖真值或人工，难以泛化至分布外问题。
- 方法要点：使用大语言模型进行成对难度比较，基于Bradley-Terry模型计算连续分数。
- 实验或效果：验证显示与人类标注强相关（Pearson r≥0.80），对幻觉鲁棒（噪声注入下退化<6%）。

## 摘要（原文）

> Recent advances in the finetuning of large language models (LLMs) have significantly improved their performance on established benchmarks, emphasizing the need for increasingly difficult, synthetic data. A key step in this data generation pipeline is a method for estimating problem difficulty. Current approaches, such as human calibration or performance-based scoring, fail to generalize to out-of-distribution problems, i.e. problems currently unsolvable by humans and LLMs, because they are not scalable, time-consuming, and ground truth dependent. Therefore, we propose a new method for estimating problem difficulty, LLM compare, that addresses these limitations. An LLM performs pairwise difficulty comparisons, and then Bradley-Terry scores are computed based on the outcomes. To validate our method, we first propose a conceptual framework that positions existing approaches on three orthogonal planes--construction, scale and dependence--identifying which quadrants a measure needs to occupy to score out-of-distribution problems. LLM compare naturally occupies all desirable quadrants as the first measure that is continuous and dynamic, model-agnostic and independent of ground truth information. As a second validation, we show that LLM compare demonstrates strong alignment with human annotations: Pearson $r \geq 0.80$ for $n=1876$. Thirdly, we show that LLM compare is robust to hallucinations, with less than $6\%$ degradation in Pearson correlation for $10\%$ noise injection. Our work represents a significant step towards replacing time-consuming human annotations and synthetic data generation, and will be an important driver for curriculum design, model evaluation, and AI-assisted research ideation.

