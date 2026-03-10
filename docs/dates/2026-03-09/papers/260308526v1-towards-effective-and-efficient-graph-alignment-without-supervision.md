---
layout: default
title: Towards Effective and Efficient Graph Alignment without Supervision
---

# Towards Effective and Efficient Graph Alignment without Supervision
**arXiv**：[2603.08526v1](https://arxiv.org/abs/2603.08526) · [PDF](https://arxiv.org/pdf/2603.08526.pdf)  
**作者**：Songyang Chen, Youfang Lin, Yu Liu, Shuai Zheng, Lei Zou  

**一句话要点**：提出GlobAlign及其高效变体，以全局表示与最优传输解决无监督图对齐的准确性与效率权衡问题。

**关键词**：无监督图对齐, 全局表示, 最优传输, 注意力机制, 图神经网络

## 3 点简述
- 核心问题：现有无监督图对齐方法在准确性与效率间存在权衡，局部表示与全局对齐不匹配。
- 方法要点：采用全局注意力机制和分层跨图传输成本，捕获长程节点依赖，提升对齐精度。
- 实验或效果：GlobAlign-E将最优传输复杂度降至二次，实验显示准确性提升达20%，效率提升一个数量级。

## 摘要（原文）

> Unsupervised graph alignment aims to find the node correspondence across different graphs without any anchor node pairs. Despite the recent efforts utilizing deep learning-based techniques, such as the embedding and optimal transport (OT)-based approaches, we observe their limitations in terms of model accuracy-efficiency tradeoff. By focusing on the exploitation of local and global graph information, we formalize them as the ``local representation, global alignment'' paradigm, and present a new ``global representation and alignment'' paradigm to resolve the mismatch between the two phases in the alignment process. We then propose \underline{Gl}obal representation and \underline{o}ptimal transport-\underline{b}ased \underline{Align}ment (\texttt{GlobAlign}), and its variant, \texttt{GlobAlign-E}, for better \underline{E}fficiency. Our methods are equipped with the global attention mechanism and a hierarchical cross-graph transport cost, able to capture long-range and implicit node dependencies beyond the local graph structure. Furthermore, \texttt{GlobAlign-E} successfully closes the time complexity gap between representative embedding and OT-based methods, reducing OT's cubic complexity to quadratic terms. Through extensive experiments, our methods demonstrate superior performance, with up to a 20\% accuracy improvement over the best competitor. Meanwhile, \texttt{GlobAlign-E} achieves the best efficiency, with an order of magnitude speedup against existing OT-based methods.

