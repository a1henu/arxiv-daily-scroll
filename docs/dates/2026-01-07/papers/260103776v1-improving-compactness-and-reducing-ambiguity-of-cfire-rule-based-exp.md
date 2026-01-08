---
layout: default
title: Improving Compactness and Reducing Ambiguity of CFIRE Rule-Based Explanations
---

# Improving Compactness and Reducing Ambiguity of CFIRE Rule-Based Explanations
**arXiv**：[2601.03776v1](https://arxiv.org/abs/2601.03776) · [PDF](https://arxiv.org/pdf/2601.03776.pdf)  
**作者**：Sebastian Müller, Tobias Schneider, Ruben Kemna, Vanessa Toborek  

**一句话要点**：提出后剪枝策略以解决CFIRE规则解释中的歧义问题，提升紧凑性

**关键词**：规则解释, 后剪枝策略, 表格数据模型, 歧义减少, 紧凑性提升

## 3 点简述
- CFIRE算法在表格数据模型解释中可能为同一样本分配不同类别的规则，导致歧义
- 通过移除低贡献或冲突覆盖的规则，提出后剪枝策略以减少模型大小和歧义
- 多数据集实验验证了该方法在保持预测性能的同时有效改善紧凑性和清晰度

## 摘要（原文）

> Models trained on tabular data are widely used in sensitive domains, increasing the demand for explanation methods to meet transparency needs. CFIRE is a recent algorithm in this domain that constructs compact surrogate rule models from local explanations. While effective, CFIRE may assign rules associated with different classes to the same sample, introducing ambiguity. We investigate this ambiguity and propose a post-hoc pruning strategy that removes rules with low contribution or conflicting coverage, yielding smaller and less ambiguous models while preserving fidelity. Experiments across multiple datasets confirm these improvements with minimal impact on predictive performance.

