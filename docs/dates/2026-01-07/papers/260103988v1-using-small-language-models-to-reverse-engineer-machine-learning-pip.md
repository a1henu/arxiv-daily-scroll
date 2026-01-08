---
layout: default
title: Using Small Language Models to Reverse-Engineer Machine Learning Pipelines Structures
---

# Using Small Language Models to Reverse-Engineer Machine Learning Pipelines Structures
**arXiv**：[2601.03988v1](https://arxiv.org/abs/2601.03988) · [PDF](https://arxiv.org/pdf/2601.03988.pdf)  
**作者**：Nicolas Lacroix, Mireille Blay-Fornarino, Sébastien Mosser, Frederic Precioso  

**一句话要点**：评估小语言模型以逆向工程机器学习流水线结构，提升数据科学实践理解

**关键词**：小语言模型, 机器学习流水线, 逆向工程, 数据科学实践, 统计测试, 代码理解

## 3 点简述
- 核心问题：从源代码提取ML流水线阶段面临领域多样性挑战，现有方法灵活性不足。
- 方法要点：基于参考研究，通过统计测试比较SLMs性能，并分析分类定义变化的影响。
- 实验或效果：使用Cochran's Q和McNemar's测试评估模型，并通过拟合优度分析对比数据科学实践见解。

## 摘要（原文）

> Background: Extracting the stages that structure Machine Learning (ML) pipelines from source code is key for gaining a deeper understanding of data science practices. However, the diversity caused by the constant evolution of the ML ecosystem (e.g., algorithms, libraries, datasets) makes this task challenging. Existing approaches either depend on non-scalable, manual labeling, or on ML classifiers that do not properly support the diversity of the domain. These limitations highlight the need for more flexible and reliable solutions.
>   Objective: We evaluate whether Small Language Models (SLMs) can leverage their code understanding and classification abilities to address these limitations, and subsequently how they can advance our understanding of data science practices.
>   Method: We conduct a confirmatory study based on two reference works selected for their relevance regarding current state-of-the-art's limitations. First, we compare several SLMs using Cochran's Q test. The best-performing model is then evaluated against the reference studies using two distinct McNemar's tests. We further analyze how variations in taxonomy definitions affect performance through an additional Cochran's Q test. Finally, a goodness-of-fit analysis is conducted using Pearson's chi-squared tests to compare our insights on data science practices with those from prior studies.

