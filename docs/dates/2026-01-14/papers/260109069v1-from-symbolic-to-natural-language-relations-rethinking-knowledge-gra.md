---
layout: default
title: From Symbolic to Natural-Language Relations: Rethinking Knowledge Graph Construction in the Era of Large Language Models
---

# From Symbolic to Natural-Language Relations: Rethinking Knowledge Graph Construction in the Era of Large Language Models
**arXiv**：[2601.09069v1](https://arxiv.org/abs/2601.09069) · [PDF](https://arxiv.org/pdf/2601.09069.pdf)  
**作者**：Kanyao Han, Yushang Lai  

**一句话要点**：提出自然语言关系描述以解决符号关系知识图谱在LLM时代的语义缺失问题

**关键词**：知识图谱构建, 自然语言关系, 大语言模型, 混合设计, 语义表示

## 3 点简述
- 核心问题：符号关系知识图谱压缩语义细节，不适应LLM的上下文推理需求
- 方法要点：倡导从符号关系转向自然语言描述，结合最小结构骨架的混合设计原则
- 实验或效果：未知，本文为立场论文，未报告具体实验

## 摘要（原文）

> Knowledge graphs (KGs) have commonly been constructed using predefined symbolic relation schemas, typically implemented as categorical relation labels. This design has notable shortcomings: real-world relations are often contextual, nuanced, and sometimes uncertain, and compressing it into discrete relation labels abstracts away critical semantic detail. Nevertheless, symbolic-relation KGs remain widely used because they have been operationally effective and broadly compatible with pre-LLM downstream models and algorithms, in which KG knowledge could be retrieved or encoded into quantified features and embeddings at scale. The emergence of LLMs has reshaped how knowledge is created and consumed. LLMs support scalable synthesis of domain facts directly in concise natural language, and prompting-based inference favors context-rich free-form text over quantified representations. This position paper argues that these changes call for rethinking the representation of relations themselves rather than merely using LLMs to populate conventional schemas more efficiently. We therefore advocate moving from symbolic to natural-language relation descriptions, and we propose hybrid design principles that preserve a minimal structural backbone while enabling more flexible and context-sensitive relational representations.

