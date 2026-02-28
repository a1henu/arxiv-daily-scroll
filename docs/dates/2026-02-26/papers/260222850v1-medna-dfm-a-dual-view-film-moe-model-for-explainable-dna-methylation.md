---
layout: default
title: MEDNA-DFM: A Dual-View FiLM-MoE Model for Explainable DNA Methylation Prediction
---

# MEDNA-DFM: A Dual-View FiLM-MoE Model for Explainable DNA Methylation Prediction
**arXiv**：[2602.22850v1](https://arxiv.org/abs/2602.22850) · [PDF](https://arxiv.org/pdf/2602.22850.pdf)  
**作者**：Yi He, Yina Cao, Jixiu Zhai, Di Wang, Junxiao Kong, Tianchi Lu  

**一句话要点**：提出MEDNA-DFM模型及信号净化算法，用于可解释的DNA甲基化预测

**关键词**：DNA甲基化预测, 可解释深度学习, 双视图模型, 信号净化算法, 基序提取, 序列-结构协同

## 3 点简述
- 核心问题：深度学习预测DNA甲基化时缺乏可解释性，阻碍生物学洞察。
- 方法要点：采用双视图FiLM-MoE架构，结合机制启发的信号净化算法提升性能与解释性。
- 实验或效果：模型在跨物种数据上验证泛化能力，提取高可靠性基序，并通过果蝇案例提出序列-结构协同假说。

## 摘要（原文）

> Accurate computational identification of DNA methylation is essential for understanding epigenetic regulation. Although deep learning excels in this binary classification task, its "black-box" nature impedes biological insight. We address this by introducing a high-performance model MEDNA-DFM, alongside mechanism-inspired signal purification algorithms. Our investigation demonstrates that MEDNA-DFM effectively captures conserved methylation patterns, achieving robust distinction across diverse species. Validation on external independent datasets confirms that the model's generalization is driven by conserved intrinsic motifs (e.g., GC content) rather than phylogenetic proximity. Furthermore, applying our developed algorithms extracted motifs with significantly higher reliability than prior studies. Finally, empirical evidence from a Drosophila 6mA case study prompted us to propose a "sequence-structure synergy" hypothesis, suggesting that the GAGG core motif and an upstream A-tract element function cooperatively. We further validated this hypothesis via in silico mutagenesis, confirming that the ablation of either or both elements significantly degrades the model's recognition capabilities. This work provides a powerful tool for methylation prediction and demonstrates how explainable deep learning can drive both methodological innovation and the generation of biological hypotheses.

