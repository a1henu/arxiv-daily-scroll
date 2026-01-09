---
layout: default
title: Orion-RAG: Path-Aligned Hybrid Retrieval for Graphless Data
---

# Orion-RAG: Path-Aligned Hybrid Retrieval for Graphless Data
**arXiv**：[2601.04764v1](https://arxiv.org/abs/2601.04764) · [PDF](https://arxiv.org/pdf/2601.04764.pdf)  
**作者**：Zhen Chen, Weihao Xie, Peilin Chen, Shiqi Wang, Jianping Wang  

**一句话要点**：提出Orion-RAG以解决离散碎片化数据中的检索增强生成问题

**关键词**：检索增强生成, 碎片化数据, 轻量路径提取, 半结构化数据, 实时更新, 人机验证

## 3 点简述
- 核心问题：离散碎片化数据缺乏显式链接，标准检索方法忽略文件间关联
- 方法要点：使用低复杂度策略提取轻量路径，自然链接相关概念，形成半结构化数据
- 实验或效果：在FinanceBench等实验中优于主流框架，精度相对提升25.2%，支持实时更新和人机验证

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) has proven effective for knowledge synthesis, yet it encounters significant challenges in practical scenarios where data is inherently discrete and fragmented. In most environments, information is distributed across isolated files like reports and logs that lack explicit links. Standard search engines process files independently, ignoring the connections between them. Furthermore, manually building Knowledge Graphs is impractical for such vast data. To bridge this gap, we present Orion-RAG. Our core insight is simple yet effective: we do not need heavy algorithms to organize this data. Instead, we use a low-complexity strategy to extract lightweight paths that naturally link related concepts. We demonstrate that this streamlined approach suffices to transform fragmented documents into semi-structured data, enabling the system to link information across different files effectively. Extensive experiments demonstrate that Orion-RAG consistently outperforms mainstream frameworks across diverse domains, supporting real-time updates and explicit Human-in-the-Loop verification with high cost-efficiency. Experiments on FinanceBench demonstrate superior precision with a 25.2% relative improvement over strong baselines.

