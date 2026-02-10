---
layout: default
title: Data Science and Technology Towards AGI Part I: Tiered Data Management
---

# Data Science and Technology Towards AGI Part I: Tiered Data Management
**arXiv**：[2602.09003v1](https://arxiv.org/abs/2602.09003) · [PDF](https://arxiv.org/pdf/2602.09003.pdf)  
**作者**：Yudong Wang, Zixuan Fu, Hengyu Zhao, Chen Zhao, Chuyue Zhou, Xinle Lin, Hongya Lyu, Shuaikang Xue, Yi Yi, Yingjiao Wang, Zhi Zheng, Yuzhou Zhang, Jie Zhou, Chaojun Xiao, Xu Han, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出分层数据管理框架以支持大语言模型训练全生命周期，实现数据与模型协同进化。

**关键词**：分层数据管理, 大语言模型训练, 数据模型协同进化, 数据质量优化, 训练效率提升

## 3 点简述
- 核心问题：当前大语言模型依赖数据规模单向扩展，面临数据可用性、获取成本和训练效率瓶颈。
- 方法要点：引入L0-L4分层数据管理框架，利用大语言模型进行质量评分和内容编辑，优化数据分配。
- 实验或效果：实证研究表明分层数据利用显著提升训练效率和模型性能，并发布数据集和工具。

## 摘要（原文）

> The development of artificial intelligence can be viewed as an evolution of data-driven learning paradigms, with successive shifts in data organization and utilization continuously driving advances in model capability. Current LLM research is dominated by a paradigm that relies heavily on unidirectional scaling of data size, increasingly encountering bottlenecks in data availability, acquisition cost, and training efficiency. In this work, we argue that the development of AGI is entering a new phase of data-model co-evolution, in which models actively guide data management while high-quality data, in turn, amplifies model capabilities. To implement this vision, we propose a tiered data management framework, designed to support the full LLM training lifecycle across heterogeneous learning objectives and cost constraints. Specifically, we introduce an L0-L4 tiered data management framework, ranging from raw uncurated resources to organized and verifiable knowledge. Importantly, LLMs are fully used in data management processes, such as quality scoring and content editing, to refine data across tiers. Each tier is characterized by distinct data properties, management strategies, and training roles, enabling data to be strategically allocated across LLM training stages, including pre-training, mid-training, and alignment. The framework balances data quality, acquisition cost, and marginal training benefit, providing a systematic approach to scalable and sustainable data management. We validate the effectiveness of the proposed framework through empirical studies, in which tiered datasets are constructed from raw corpora and used across multiple training phases. Experimental results demonstrate that tier-aware data utilization significantly improves training efficiency and model performance. To facilitate further research, we release our tiered datasets and processing tools to the community.

