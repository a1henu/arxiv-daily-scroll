---
layout: default
title: CSSG: Measuring Code Similarity with Semantic Graphs
---

# CSSG: Measuring Code Similarity with Semantic Graphs
**arXiv**：[2601.04085v1](https://arxiv.org/abs/2601.04085) · [PDF](https://arxiv.org/pdf/2601.04085.pdf)  
**作者**：Jingwen Xu, Yiyang Lu, Changze Lv, Zisu Huang, Zhengkang Guo, Zhengyuan Wang, Muzhao Tian, Xuanjing Huang, Xiaoqing Zheng  

**一句话要点**：提出CSSG以基于程序依赖图衡量代码语义相似性

**关键词**：代码相似性度量, 程序依赖图, 语义表示, 跨语言代码分析, 代码理解

## 3 点简述
- 现有代码相似性度量依赖表面字符串或语法树，难以捕获深层语义关系
- CSSG利用程序依赖图建模控制依赖和变量交互，提供语义感知表示
- 在CodeContests+数据集上，CSSG在单语言和跨语言设置中优于现有度量

## 摘要（原文）

> Existing code similarity metrics, such as BLEU, CodeBLEU, and TSED, largely rely on surface-level string overlap or abstract syntax tree structures, and often fail to capture deeper semantic relationships between programs.We propose CSSG (Code Similarity using Semantic Graphs), a novel metric that leverages program dependence graphs to explicitly model control dependencies and variable interactions, providing a semantics-aware representation of code.Experiments on the CodeContests+ dataset show that CSSG consistently outperforms existing metrics in distinguishing more similar code from less similar code under both monolingual and cross-lingual settings, demonstrating that dependency-aware graph representations offer a more effective alternative to surface-level or syntax-based similarity measures.

