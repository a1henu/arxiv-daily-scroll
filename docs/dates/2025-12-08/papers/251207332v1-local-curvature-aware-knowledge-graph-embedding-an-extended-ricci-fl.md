---
layout: default
title: Local-Curvature-Aware Knowledge Graph Embedding: An Extended Ricci Flow Approach
---

# Local-Curvature-Aware Knowledge Graph Embedding: An Extended Ricci Flow Approach
**arXiv**：[2512.07332v1](https://arxiv.org/abs/2512.07332) · [PDF](https://arxiv.org/pdf/2512.07332.pdf)  
**作者**：Zhengquan Luo, Guy Tadmor, Or Amar, David Zeevi, Zhiqiang Xu  

**一句话要点**：提出RicciKGE方法，通过扩展Ricci流耦合局部曲率与嵌入优化，以解决知识图谱嵌入中预定义均匀流形无法适应局部曲率变化的问题。

**关键词**：知识图谱嵌入, 局部曲率适应, Ricci流, 几何优化, 链接预测, 节点分类

## 3 点简述
- 核心问题：预定义均匀流形（如欧几里得、双曲）无法适应知识图谱局部曲率的剧烈变化，导致嵌入失真和表达能力下降。
- 方法要点：将KGE损失梯度与局部曲率耦合在扩展Ricci流中，使嵌入与流形几何动态协同演化，实现相互适应。
- 实验或效果：在链接预测和节点分类基准测试中表现提升，验证了RicciKGE适应异构知识图谱结构的有效性。

## 摘要（原文）

> Knowledge graph embedding (KGE) relies on the geometry of the embedding space to encode semantic and structural relations. Existing methods place all entities on one homogeneous manifold, Euclidean, spherical, hyperbolic, or their product/multi-curvature variants, to model linear, symmetric, or hierarchical patterns. Yet a predefined, homogeneous manifold cannot accommodate the sharply varying curvature that real-world graphs exhibit across local regions. Since this geometry is imposed a priori, any mismatch with the knowledge graph's local curvatures will distort distances between entities and hurt the expressiveness of the resulting KGE. To rectify this, we propose RicciKGE to have the KGE loss gradient coupled with local curvatures in an extended Ricci flow such that entity embeddings co-evolve dynamically with the underlying manifold geometry towards mutual adaptation. Theoretically, when the coupling coefficient is bounded and properly selected, we rigorously prove that i) all the edge-wise curvatures decay exponentially, meaning that the manifold is driven toward the Euclidean flatness; and ii) the KGE distances strictly converge to a global optimum, which indicates that geometric flattening and embedding optimization are promoting each other. Experimental improvements on link prediction and node classification benchmarks demonstrate RicciKGE's effectiveness in adapting to heterogeneous knowledge graph structures.

