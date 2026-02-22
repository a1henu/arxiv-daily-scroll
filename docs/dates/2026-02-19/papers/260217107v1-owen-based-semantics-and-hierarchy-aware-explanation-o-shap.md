---
layout: default
title: Owen-based Semantics and Hierarchy-Aware Explanation (O-Shap)
---

# Owen-based Semantics and Hierarchy-Aware Explanation (O-Shap)
**arXiv**：[2602.17107v1](https://arxiv.org/abs/2602.17107) · [PDF](https://arxiv.org/pdf/2602.17107.pdf)  
**作者**：Xiangyu Zhou, Chenhan Xiao, Yang Weng  

**一句话要点**：提出O-Shap方法，基于Owen值改进SHAP，通过语义对齐的分割解决视觉任务中特征依赖问题。

**关键词**：可解释人工智能, Shapley值, Owen值, 特征归因, 语义分割, 层次结构

## 3 点简述
- 核心问题：SHAP方法在视觉任务中因特征依赖假设失效，导致解释不准确。
- 方法要点：引入Owen值支持分组归因，提出满足T-性质的分割方法确保语义对齐。
- 实验或效果：在图像和表格数据集上，O-Shap在归因精度、语义一致性和运行效率上优于基线。

## 摘要（原文）

> Shapley value-based methods have become foundational in explainable artificial intelligence (XAI), offering theoretically grounded feature attributions through cooperative game theory. However, in practice, particularly in vision tasks, the assumption of feature independence breaks down, as features (i.e., pixels) often exhibit strong spatial and semantic dependencies. To address this, modern SHAP implementations now include the Owen value, a hierarchical generalization of the Shapley value that supports group attributions. While the Owen value preserves the foundations of Shapley values, its effectiveness critically depends on how feature groups are defined. We show that commonly used segmentations (e.g., axis-aligned or SLIC) violate key consistency properties, and propose a new segmentation approach that satisfies the $T$-property to ensure semantic alignment across hierarchy levels. This hierarchy enables computational pruning while improving attribution accuracy and interpretability. Experiments on image and tabular datasets demonstrate that O-Shap outperforms baseline SHAP variants in attribution precision, semantic coherence, and runtime efficiency, especially when structure matters.

