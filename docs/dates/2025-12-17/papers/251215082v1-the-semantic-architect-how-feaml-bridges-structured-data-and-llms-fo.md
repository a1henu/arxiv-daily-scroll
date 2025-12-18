---
layout: default
title: The Semantic Architect: How FEAML Bridges Structured Data and LLMs for Multi-Label Tasks
---

# The Semantic Architect: How FEAML Bridges Structured Data and LLMs for Multi-Label Tasks
**arXiv**：[2512.15082v1](https://arxiv.org/abs/2512.15082) · [PDF](https://arxiv.org/pdf/2512.15082.pdf)  
**作者**：Wanfu Gao, Zebin He, Jun Gao  

**一句话要点**：提出FEAML方法，利用LLMs代码生成能力自动化特征工程以解决多标签学习任务中的特征建模问题。

**关键词**：多标签学习, 特征工程自动化, 大语言模型, 代码生成, 反馈机制

## 3 点简述
- 现有基于LLMs的特征工程方法未应用于多标签学习，缺乏对复杂标签依赖的建模能力。
- FEAML利用元数据和标签共现矩阵引导LLMs理解特征与任务关系，生成高质量特征并评估优化。
- 在多标签数据集上的实验表明，FEAML优于其他特征工程方法，实现高效、可解释和自改进的特征工程。

## 摘要（原文）

> Existing feature engineering methods based on large language models (LLMs) have not yet been applied to multi-label learning tasks. They lack the ability to model complex label dependencies and are not specifically adapted to the characteristics of multi-label tasks. To address the above issues, we propose Feature Engineering Automation for Multi-Label Learning (FEAML), an automated feature engineering method for multi-label classification which leverages the code generation capabilities of LLMs. By utilizing metadata and label co-occurrence matrices, LLMs are guided to understand the relationships between data features and task objectives, based on which high-quality features are generated. The newly generated features are evaluated in terms of model accuracy to assess their effectiveness, while Pearson correlation coefficients are used to detect redundancy. FEAML further incorporates the evaluation results as feedback to drive LLMs to continuously optimize code generation in subsequent iterations. By integrating LLMs with a feedback mechanism, FEAML realizes an efficient, interpretable and self-improving feature engineering paradigm. Empirical results on various multi-label datasets demonstrate that our FEAML outperforms other feature engineering methods.

