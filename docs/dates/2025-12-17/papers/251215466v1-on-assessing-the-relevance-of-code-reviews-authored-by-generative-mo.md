---
layout: default
title: On Assessing the Relevance of Code Reviews Authored by Generative Models
---

# On Assessing the Relevance of Code Reviews Authored by Generative Models
**arXiv**：[2512.15466v1](https://arxiv.org/abs/2512.15466) · [PDF](https://arxiv.org/pdf/2512.15466.pdf)  
**作者**：Robert Heumüller, Frank Ortmeier  

**一句话要点**：提出多主观排序方法以评估生成模型在代码审查中的相关性

**关键词**：代码审查评估, 生成模型, 多主观排序, ChatGPT, 人工智能安全, 软件工程

## 3 点简述
- 核心问题：现有代码审查生成评估方法依赖单一标准或主观有用性，无法捕捉人类视角多样性
- 方法要点：引入多主观排序，基于CodeReview StackExchange数据集，让多人对ChatGPT生成评论与人类回答进行排名
- 实验或效果：ChatGPT评论排名显著优于人类回答，甚至超过平台采纳答案，方法促进更有效评估并警示风险

## 摘要（原文）

> The use of large language models like ChatGPT in code review offers promising efficiency gains but also raises concerns about correctness and safety. Existing evaluation methods for code review generation either rely on automatic comparisons to a single ground truth, which fails to capture the variability of human perspectives, or on subjective assessments of "usefulness", a highly ambiguous concept. We propose a novel evaluation approach based on what we call multi-subjective ranking. Using a dataset of 280 self-contained code review requests and corresponding comments from CodeReview StackExchange, multiple human judges ranked the quality of ChatGPT-generated comments alongside the top human responses from the platform. Results show that ChatGPT's comments were ranked significantly better than human ones, even surpassing StackExchange's accepted answers. Going further, our proposed method motivates and enables more meaningful assessments of generative AI's performance in code review, while also raising awareness of potential risks of unchecked integration into review processes.

