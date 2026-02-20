---
layout: default
title: Owen-based Semantics and Hierarchy-Aware Explanation (O-Shap)
---

# Owen-based Semantics and Hierarchy-Aware Explanation (O-Shap)
**arXiv**：[2602.17107v1](https://arxiv.org/abs/2602.17107) · [PDF](https://arxiv.org/pdf/2602.17107.pdf)  
**作者**：Xiangyu Zhou, Chenhan Xiao, Yang Weng  

**一句话要点**：提出基于Owen值的语义层次化解释方法O-Shap，以解决视觉任务中特征依赖性问题。

**关键词**：可解释人工智能, Shapley值, Owen值, 特征分组, 语义分割, 层次化解释

## 3 点简述
- 核心问题：Shapley值方法在视觉任务中假设特征独立，忽略空间和语义依赖，导致解释不准确。
- 方法要点：引入Owen值支持组属性，提出满足T-属性的新分割方法，确保语义对齐和层次一致性。
- 实验或效果：在图像和表格数据集上，O-Shap在属性精度、语义一致性和运行效率上优于基线SHAP变体。

## 摘要（原文）

> Shapley value-based methods have become foundational in explainable artificial intelligence (XAI), offering theoretically grounded feature attributions through cooperative game theory. However, in practice, particularly in vision tasks, the assumption of feature independence breaks down, as features (i.e., pixels) often exhibit strong spatial and semantic dependencies. To address this, modern SHAP implementations now include the Owen value, a hierarchical generalization of the Shapley value that supports group attributions. While the Owen value preserves the foundations of Shapley values, its effectiveness critically depends on how feature groups are defined. We show that commonly used segmentations (e.g., axis-aligned or SLIC) violate key consistency properties, and propose a new segmentation approach that satisfies the $T$-property to ensure semantic alignment across hierarchy levels. This hierarchy enables computational pruning while improving attribution accuracy and interpretability. Experiments on image and tabular datasets demonstrate that O-Shap outperforms baseline SHAP variants in attribution precision, semantic coherence, and runtime efficiency, especially when structure matters.

