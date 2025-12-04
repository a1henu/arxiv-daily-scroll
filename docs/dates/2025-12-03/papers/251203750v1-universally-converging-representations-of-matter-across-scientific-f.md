---
layout: default
title: Universally Converging Representations of Matter Across Scientific Foundation Models
---

# Universally Converging Representations of Matter Across Scientific Foundation Models
**arXiv**：[2512.03750v1](https://arxiv.org/abs/2512.03750) · [PDF](https://arxiv.org/pdf/2512.03750.pdf)  
**作者**：Sathya Edamadaka, Soojung Yang, Ju Li, Rafael Gómez-Bombarelli  

**一句话要点**：揭示科学基础模型在物质表示上的普遍收敛性，评估其泛化能力

**关键词**：科学基础模型, 表示对齐, 物质表示, 泛化评估, 模态转换

## 3 点简述
- 核心问题：不同模态的科学模型是否学习相似的内部物质表示，以构建可靠泛化的基础模型
- 方法要点：分析近60个科学模型的表示对齐，涵盖字符串、图、3D原子和蛋白质模态
- 实验或效果：发现模型在训练相似输入上表示收敛，但在不同结构上表示崩溃，表明泛化有限

## 摘要（原文）

> Machine learning models of vastly different modalities and architectures are being trained to predict the behavior of molecules, materials, and proteins. However, it remains unclear whether they learn similar internal representations of matter. Understanding their latent structure is essential for building scientific foundation models that generalize reliably beyond their training domains. Although representational convergence has been observed in language and vision, its counterpart in the sciences has not been systematically explored. Here, we show that representations learned by nearly sixty scientific models, spanning string-, graph-, 3D atomistic, and protein-based modalities, are highly aligned across a wide range of chemical systems. Models trained on different datasets have highly similar representations of small molecules, and machine learning interatomic potentials converge in representation space as they improve in performance, suggesting that foundation models learn a common underlying representation of physical reality. We then show two distinct regimes of scientific models: on inputs similar to those seen during training, high-performing models align closely and weak models diverge into local sub-optima in representation space; on vastly different structures from those seen during training, nearly all models collapse onto a low-information representation, indicating that today's models remain limited by training data and inductive bias and do not yet encode truly universal structure. Our findings establish representational alignment as a quantitative benchmark for foundation-level generality in scientific models. More broadly, our work can track the emergence of universal representations of matter as models scale, and for selecting and distilling models whose learned representations transfer best across modalities, domains of matter, and scientific tasks.

