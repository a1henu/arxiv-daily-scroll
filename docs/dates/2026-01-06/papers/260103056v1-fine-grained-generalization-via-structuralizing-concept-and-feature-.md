---
layout: default
title: Fine-Grained Generalization via Structuralizing Concept and Feature Space into Commonality, Specificity and Confounding
---

# Fine-Grained Generalization via Structuralizing Concept and Feature Space into Commonality, Specificity and Confounding
**arXiv**：[2601.03056v1](https://arxiv.org/abs/2601.03056) · [PDF](https://arxiv.org/pdf/2601.03056.pdf)  
**作者**：Zhen Wang, Jiaojiao Zhao, Qilong Wang, Yongfeng Dong, Wenlong Yu  

**一句话要点**：提出概念-特征结构化泛化模型以解决细粒度域泛化中模型对细微线索过度敏感的问题

**关键词**：细粒度域泛化, 概念解耦, 特征结构化, 自适应机制, 可解释性分析

## 3 点简述
- 细粒度域泛化因类间差异细微和类内变化显著而更具挑战性，模型在域偏移下易抑制关键特征
- 模型将概念和特征空间解耦为共同、特定和混淆三个结构化组件，并引入自适应机制动态调整比例
- 在三个单源基准数据集上平均性能提升9.87%，优于现有方法3.08%，可解释性分析验证了结构化知识的整合

## 摘要（原文）

> Fine-Grained Domain Generalization (FGDG) presents greater challenges than conventional domain generalization due to the subtle inter-class differences and relatively pronounced intra-class variations inherent in fine-grained recognition tasks. Under domain shifts, the model becomes overly sensitive to fine-grained cues, leading to the suppression of critical features and a significant drop in performance. Cognitive studies suggest that humans classify objects by leveraging both common and specific attributes, enabling accurate differentiation between fine-grained categories. However, current deep learning models have yet to incorporate this mechanism effectively. Inspired by this mechanism, we propose Concept-Feature Structuralized Generalization (CFSG). This model explicitly disentangles both the concept and feature spaces into three structured components: common, specific, and confounding segments. To mitigate the adverse effects of varying degrees of distribution shift, we introduce an adaptive mechanism that dynamically adjusts the proportions of common, specific, and confounding components. In the final prediction, explicit weights are assigned to each pair of components. Extensive experiments on three single-source benchmark datasets demonstrate that CFSG achieves an average performance improvement of 9.87% over baseline models and outperforms existing state-of-the-art methods by an average of 3.08%. Additionally, explainability analysis validates that CFSG effectively integrates multi-granularity structured knowledge and confirms that feature structuralization facilitates the emergence of concept structuralization.

