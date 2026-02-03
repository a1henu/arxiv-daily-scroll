---
layout: default
title: CAM: A Causality-based Analysis Framework for Multi-Agent Code Generation Systems
---

# CAM: A Causality-based Analysis Framework for Multi-Agent Code Generation Systems
**arXiv**：[2602.02138v1](https://arxiv.org/abs/2602.02138) · [PDF](https://arxiv.org/pdf/2602.02138.pdf)  
**作者**：Lyu Zongyi, Ji Zhenlan, Chen Songqiang, Wang Liwen, Huang Yuheng, Wang Shuai, Cheung Shing-Chi  

**一句话要点**：提出基于因果关系的分析框架CAM，以量化多智能体代码生成系统中中间特征对系统正确性的贡献。

**关键词**：多智能体代码生成, 因果分析, 中间特征量化, 系统优化, 失败修复, 特征剪枝

## 3 点简述
- 多智能体代码生成系统中间输出重要性不透明，阻碍针对性优化。
- CAM通过分类中间输出和模拟错误，量化特征贡献并识别重要性排名。
- 应用包括失败修复和特征剪枝，提升性能并减少中间令牌消耗。

## 摘要（原文）

> Despite the remarkable success that Multi-Agent Code Generation Systems (MACGS) have achieved, the inherent complexity of multi-agent architectures produces substantial volumes of intermediate outputs. To date, the individual importance of these intermediate outputs to the system correctness remains opaque, which impedes targeted optimization of MACGS designs. To address this challenge, we propose CAM, the first \textbf{C}ausality-based \textbf{A}nalysis framework for \textbf{M}ACGS that systematically quantifies the contribution of different intermediate features for system correctness. By comprehensively categorizing intermediate outputs and systematically simulating realistic errors on intermediate features, we identify the important features for system correctness and aggregate their importance rankings.
>   We conduct extensive empirical analysis on the identified importance rankings. Our analysis reveals intriguing findings: first, we uncover context-dependent features\textemdash features whose importance emerges mainly through interactions with other features, revealing that quality assurance for MACGS should incorporate cross-feature consistency checks; second, we reveal that hybrid backend MACGS with different backend LLMs assigned according to their relative strength achieves up to 7.2\% Pass@1 improvement, underscoring hybrid architectures as a promising direction for future MACGS design. We further demonstrate CAM's practical utility through two applications: (1) failure repair which achieves a 73.3\% success rate by optimizing top-3 importance-ranked features and (2) feature pruning that reduces up to 66.8\% intermediate token consumption while maintaining generation performance. Our work provides actionable insights for MACGS design and deployment, establishing causality analysis as a powerful approach for understanding and improving MACGS.

