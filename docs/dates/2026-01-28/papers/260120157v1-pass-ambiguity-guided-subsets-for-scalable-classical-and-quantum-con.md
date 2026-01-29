---
layout: default
title: PASS: Ambiguity Guided Subsets for Scalable Classical and Quantum Constrained Clustering
---

# PASS: Ambiguity Guided Subsets for Scalable Classical and Quantum Constrained Clustering
**arXiv**：[2601.20157v1](https://arxiv.org/abs/2601.20157) · [PDF](https://arxiv.org/pdf/2601.20157.pdf)  
**作者**：Pedro Chumpitaz-Flores, My Duong, Ying Mao, Kaixun Hua  

**一句话要点**：提出PASS框架以解决成对约束聚类在可扩展性和量子应用中的挑战

**关键词**：成对约束聚类, 可扩展聚类, 量子聚类, 子集选择, 信息几何, 约束满足

## 3 点简述
- 核心问题：成对约束聚类在数据可扩展性上存在困难，尤其在量子或量子混合聚类等小众应用中。
- 方法要点：PASS通过将必须链接约束折叠为伪点，并提供基于边界和信息几何的规则来选择子集，以保持约束满足并实现可扩展聚类。
- 实验或效果：在多样基准测试中，PASS以显著更低的成本达到竞争性SSE，并在先前方法失效的场景中保持有效。

## 摘要（原文）

> Pairwise-constrained clustering augments unsupervised partitioning with side information by enforcing must-link (ML) and cannot-link (CL) constraints between specific samples, yielding labelings that respect known affinities and separations. However, ML and CL constraints add an extra layer of complexity to the clustering problem, with current methods struggling in data scalability, especially in niche applications like quantum or quantum-hybrid clustering. We propose PASS, a pairwise-constraints and ambiguity-driven subset selection framework that preserves ML and CL constraints satisfaction while allowing scalable, high-quality clustering solution. PASS collapses ML constraints into pseudo-points and offers two selectors: a constraint-aware margin rule that collects near-boundary points and all detected CL violations, and an information-geometric rule that scores points via a Fisher-Rao distance derived from soft assignment posteriors, then selects the highest-information subset under a simple budget. Across diverse benchmarks, PASS attains competitive SSE at substantially lower cost than exact or penalty-based methods, and remains effective in regimes where prior approaches fail.

