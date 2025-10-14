---
layout: default
title: DocReward: A Document Reward Model for Structuring and Stylizing
---

# DocReward: A Document Reward Model for Structuring and Stylizing
**arXiv**：[2510.11391v1](https://arxiv.org/abs/2510.11391) · [PDF](https://arxiv.org/pdf/2510.11391.pdf)  
**作者**：Junpeng Liu, Yuzhong Zhao, Bowen Cao, Jiayu Ding, Yilin Jia, Tengchao Lv, Yupan Huang, Shaohan Huang, Nan Yang, Li Dong, Lei Cui, Tao Ge, Xun Wang, Huitian Jiao, Sun Mao, FNU Kartik, Si-Qing Chen, Wai Lam, Furu Wei  

**一句话要点**：提出DocReward文档奖励模型，以解决代理工作流中视觉结构与风格评估的缺失问题。

**关键词**：文档奖励模型, 代理工作流, 多领域数据集, Bradley-Terry损失, 文档生成评估

## 3 点简述
- 核心问题：代理工作流自动化文档生成时，缺乏对视觉结构与风格的评估，影响可读性与参与度。
- 方法要点：构建多领域DocPair数据集，使用Bradley-Terry损失训练模型，实现文本质量无关的专业性评分。
- 实验或效果：在测试集上，DocReward准确率超越GPT-4o和GPT-5，并在文档生成评估中赢得更高胜率。

## 摘要（原文）

> Recent advances in agentic workflows have enabled the automation of tasks
> such as professional document generation. However, they primarily focus on
> textual quality, neglecting visual structure and style, which are crucial for
> readability and engagement. This gap arises mainly from the absence of suitable
> reward models to guide agentic workflows toward producing documents with
> stronger structural and stylistic quality. To address this, we propose
> DocReward, a document reward model that evaluates documents based on their
> structure and style. We construct a multi-domain dataset DocPair of 117K paired
> documents, covering 32 domains and 267 document types, each including a high-
> and low-professionalism document with identical content but different structure
> and style. This enables the model to evaluate professionalism comprehensively,
> and in a textual-quality-agnostic way. DocReward is trained using the
> Bradley-Terry loss to score documents, penalizing predictions that contradict
> the annotated ranking. To assess the performance of reward models, we create a
> test dataset containing document bundles ranked by well-educated human
> evaluators. Notably, DocReward outperforms GPT-4o and GPT-5 in accuracy by 30.6
> and 19.4 percentage points, respectively, demonstrating its superiority over
> baselines. In an extrinsic evaluation of document generation, DocReward
> achieves a significantly higher win rate of 60.8%, compared to GPT-5's 37.7%
> win rate, demonstrating its utility in guiding generation agents toward
> producing human-preferred documents.

