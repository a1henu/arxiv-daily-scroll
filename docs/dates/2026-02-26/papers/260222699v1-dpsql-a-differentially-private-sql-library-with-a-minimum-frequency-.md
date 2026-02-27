---
layout: default
title: DPSQL+: A Differentially Private SQL Library with a Minimum Frequency Rule
---

# DPSQL+: A Differentially Private SQL Library with a Minimum Frequency Rule
**arXiv**：[2602.22699v1](https://arxiv.org/abs/2602.22699) · [PDF](https://arxiv.org/pdf/2602.22699.pdf)  
**作者**：Tomoya Matsumoto, Shokichi Takakura, Shun Takagi, Satoshi Hasegawa  

**一句话要点**：提出DPSQL+库，结合差分隐私与最小频率规则以保护SQL查询隐私。

**关键词**：差分隐私, SQL库, 最小频率规则, 隐私保护, 数据查询, 模块化架构

## 3 点简述
- 核心问题：SQL查询结果可能泄露敏感信息，差分隐私单独使用无法满足最小频率规则等治理要求。
- 方法要点：采用模块化架构，包括查询验证器、隐私损失会计师和可移植后端，同时强制执行用户级差分隐私和最小频率规则。
- 实验或效果：在TPC-H基准测试中，DPSQL+在多种分析工作负载下实现实用精度，并在固定隐私预算下支持更多查询。

## 摘要（原文）

> SQL is the de facto interface for exploratory data analysis; however, releasing exact query results can expose sensitive information through membership or attribute inference attacks. Differential privacy (DP) provides rigorous privacy guarantees, but in practice, DP alone may not satisfy governance requirements such as the \emph{minimum frequency rule}, which requires each released group (cell) to include contributions from at least $k$ distinct individuals. In this paper, we present \textbf{DPSQL+}, a privacy-preserving SQL library that simultaneously enforces user-level $(\varepsilon,δ)$-DP and the minimum frequency rule. DPSQL+ adopts a modular architecture consisting of: (i) a \emph{Validator} that statically restricts queries to a DP-safe subset of SQL; (ii) an \emph{Accountant} that consistently tracks cumulative privacy loss across multiple queries; and (iii) a \emph{Backend} that interfaces with various database engines, ensuring portability and extensibility. Experiments on the TPC-H benchmark demonstrate that DPSQL+ achieves practical accuracy across a wide range of analytical workloads -- from basic aggregates to quadratic statistics and join operations -- and allows substantially more queries under a fixed global privacy budget than prior libraries in our evaluation.

