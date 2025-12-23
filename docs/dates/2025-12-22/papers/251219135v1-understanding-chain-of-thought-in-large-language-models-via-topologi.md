---
layout: default
title: Understanding Chain-of-Thought in Large Language Models via Topological Data Analysis
---

# Understanding Chain-of-Thought in Large Language Models via Topological Data Analysis
**arXiv**：[2512.19135v1](https://arxiv.org/abs/2512.19135) · [PDF](https://arxiv.org/pdf/2512.19135.pdf)  
**作者**：Chenghao Li, Chaoning Zhang, Yi Lu, Shuxu Chen, Xudong Wang, Jiaquan Zhang, Zhicheng Wang, Zhengxun Jin, Kuien Liu, Sung-Ho Bae, Guoqing Wang, Yang Yang, Hen Tao Shen  

**一句话要点**：应用拓扑数据分析评估大语言模型推理链的结构质量

**关键词**：大语言模型, 推理链评估, 拓扑数据分析, 持久同调, 语义空间映射

## 3 点简述
- 核心问题：不同推理链性能差异的结构机制未知，现有研究缺乏结构视角分析
- 方法要点：使用持久同调将推理步骤映射到语义空间，提取拓扑特征分析结构变化
- 实验或效果：拓扑结构复杂度与准确性正相关，成功推理链拓扑更简单，减少冗余和循环

## 摘要（原文）

> With the development of large language models (LLMs), particularly with the introduction of the long reasoning chain technique, the reasoning ability of LLMs in complex problem-solving has been significantly enhanced. While acknowledging the power of long reasoning chains, we cannot help but wonder: Why do different reasoning chains perform differently in reasoning? What components of the reasoning chains play a key role? Existing studies mainly focus on evaluating reasoning chains from a functional perspective, with little attention paid to their structural mechanisms. To address this gap, this work is the first to analyze and evaluate the quality of the reasoning chain from a structural perspective. We apply persistent homology from Topological Data Analysis (TDA) to map reasoning steps into semantic space, extract topological features, and analyze structural changes. These changes reveal semantic coherence, logical redundancy, and identify logical breaks and gaps. By calculating homology groups, we assess connectivity and redundancy at various scales, using barcode and persistence diagrams to quantify stability and consistency. Our results show that the topological structural complexity of reasoning chains correlates positively with accuracy. More complex chains identify correct answers sooner, while successful reasoning exhibits simpler topologies, reducing redundancy and cycles, enhancing efficiency and interpretability. This work provides a new perspective on reasoning chain quality assessment and offers guidance for future optimization.

