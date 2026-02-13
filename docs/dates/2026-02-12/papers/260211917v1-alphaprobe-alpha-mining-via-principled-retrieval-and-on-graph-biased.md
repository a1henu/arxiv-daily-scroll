---
layout: default
title: AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution
---

# AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution
**arXiv**：[2602.11917v1](https://arxiv.org/abs/2602.11917) · [PDF](https://arxiv.org/pdf/2602.11917.pdf)  
**作者**：Taian Guo, Haiyang Shen, Junyu Luo, Binqi Chen, Hongjun Ding, Jinsheng Huang, Luchen Liu, Yun Ma, Ming Zhang  

**一句话要点**：提出AlphaPROBE框架，通过有向无环图导航解决量化金融中alpha因子挖掘的全局结构缺失问题。

**关键词**：量化金融, alpha因子挖掘, 有向无环图, 贝叶斯检索, 因子演化, 自动化发现

## 3 点简述
- 核心问题：现有自动化alpha因子挖掘方法缺乏全局结构视图，导致搜索冗余和多样性受限。
- 方法要点：将因子池建模为动态有向无环图，结合贝叶斯因子检索器和图感知因子生成器进行策略性导航。
- 实验或效果：在三个中国股市数据集上优于8个基线，提升预测准确性、收益稳定性和训练效率。

## 摘要（原文）

> Extracting signals through alpha factor mining is a fundamental challenge in quantitative finance. Existing automated methods primarily follow two paradigms: Decoupled Factor Generation, which treats factor discovery as isolated events, and Iterative Factor Evolution, which focuses on local parent-child refinements. However, both paradigms lack a global structural view, often treating factor pools as unstructured collections or fragmented chains, which leads to redundant search and limited diversity. To address these limitations, we introduce AlphaPROBE (Alpha Mining via Principled Retrieval and On-graph Biased Evolution), a framework that reframes alpha mining as the strategic navigation of a Directed Acyclic Graph (DAG). By modeling factors as nodes and evolutionary links as edges, AlphaPROBE treats the factor pool as a dynamic, interconnected ecosystem. The framework consists of two core components: a Bayesian Factor Retriever that identifies high-potential seeds by balancing exploitation and exploration through a posterior probability model, and a DAG-aware Factor Generator that leverages the full ancestral trace of factors to produce context-aware, nonredundant optimizations. Extensive experiments on three major Chinese stock market datasets against 8 competitive baselines demonstrate that AlphaPROBE significantly gains enhanced performance in predictive accuracy, return stability and training efficiency. Our results confirm that leveraging global evolutionary topology is essential for efficient and robust automated alpha discovery. We have open-sourced our implementation at https://github.com/gta0804/AlphaPROBE.

