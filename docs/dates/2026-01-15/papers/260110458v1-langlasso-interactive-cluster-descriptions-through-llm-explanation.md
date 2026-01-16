---
layout: default
title: LangLasso: Interactive Cluster Descriptions through LLM Explanation
---

# LangLasso: Interactive Cluster Descriptions through LLM Explanation
**arXiv**：[2601.10458v1](https://arxiv.org/abs/2601.10458) · [PDF](https://arxiv.org/pdf/2601.10458.pdf)  
**作者**：Raphael Buchmüller, Dennis Collaris, Linhao Meng, Angelos Chatzimparmpas  

**一句话要点**：提出LangLasso，通过LLM生成交互式自然语言描述以增强降维聚类可解释性

**关键词**：降维聚类, 可解释性, 大语言模型, 自然语言描述, 视觉分析, 交互式工具

## 3 点简述
- 核心问题：降维聚类结果缺乏语义可解释性，现有方法需技术专长和大量人工努力
- 方法要点：结合视觉分析方法，利用大语言模型生成交互式、人类可读的聚类描述，集成外部上下文知识
- 实验或效果：系统评估解释可靠性，证明LangLasso能有效帮助非专家参与聚类解释，工具已公开可用

## 摘要（原文）

> Dimensionality reduction is a powerful technique for revealing structure and potential clusters in data. However, as the axes are complex, non-linear combinations of features, they often lack semantic interpretability. Existing visual analytics (VA) methods support cluster interpretation through feature comparison and interactive exploration, but they require technical expertise and intense human effort. We present \textit{LangLasso}, a novel method that complements VA approaches through interactive, natural language descriptions of clusters using large language models (LLMs). It produces human-readable descriptions that make cluster interpretation accessible to non-experts and allow integration of external contextual knowledge beyond the dataset. We systematically evaluate the reliability of these explanations and demonstrate that \langlasso provides an effective first step for engaging broader audiences in cluster interpretation. The tool is available at https://langlasso.vercel.app

