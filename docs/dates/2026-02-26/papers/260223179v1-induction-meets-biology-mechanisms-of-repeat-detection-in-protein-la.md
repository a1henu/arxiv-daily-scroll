---
layout: default
title: Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models
---

# Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models
**arXiv**：[2602.23179v1](https://arxiv.org/abs/2602.23179) · [PDF](https://arxiv.org/pdf/2602.23179.pdf)  
**作者**：Gal Kesten-Pomeranz, Yaniv Nikankin, Anja Reusch, Tomer Tsaban, Ora Schueler-Furman, Yonatan Belinkov  

**一句话要点**：揭示蛋白质语言模型检测重复序列的内部机制，结合语言模式匹配与生物知识

**关键词**：蛋白质语言模型, 重复序列检测, 内部机制分析, 生物信息学, 注意力机制

## 3 点简述
- 核心问题：研究PLMs如何检测蛋白质序列中的精确和近似重复，以理解其内部机制
- 方法要点：通过分析掩码标记预测，发现PLMs使用位置注意头和生物专用组件构建特征表示
- 实验或效果：揭示机制分两阶段：特征构建和诱导头对齐重复段，促进正确预测

## 摘要（原文）

> Protein sequences are abundant in repeating segments, both as exact copies and as approximate segments with mutations. These repeats are important for protein structure and function, motivating decades of algorithmic work on repeat identification. Recent work has shown that protein language models (PLMs) identify repeats, by examining their behavior in masked-token prediction. To elucidate their internal mechanisms, we investigate how PLMs detect both exact and approximate repeats. We find that the mechanism for approximate repeats functionally subsumes that of exact repeats. We then characterize this mechanism, revealing two main stages: PLMs first build feature representations using both general positional attention heads and biologically specialized components, such as neurons that encode amino-acid similarity. Then, induction heads attend to aligned tokens across repeated segments, promoting the correct answer. Our results reveal how PLMs solve this biological task by combining language-based pattern matching with specialized biological knowledge, thereby establishing a basis for studying more complex evolutionary processes in PLMs.

