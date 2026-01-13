---
layout: default
title: CalPro: Prior-Aware Evidential--Conformal Prediction with Structure-Aware Guarantees for Protein Structures
---

# CalPro: Prior-Aware Evidential--Conformal Prediction with Structure-Aware Guarantees for Protein Structures
**arXiv**：[2601.07201v1](https://arxiv.org/abs/2601.07201) · [PDF](https://arxiv.org/pdf/2601.07201.pdf)  
**作者**：Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  

**一句话要点**：提出CalPro框架，结合先验感知、证据推理和保形预测，以解决蛋白质结构预测中置信度校准不足和分布偏移问题。

**关键词**：蛋白质结构预测, 不确定性量化, 保形预测, 证据推理, 分布偏移, 结构感知保证

## 3 点简述
- 核心问题：AlphaFold等深度蛋白质结构预测器的置信度估计（如pLDDT）在校准和分布偏移下表现不佳。
- 方法要点：整合几何证据头、可微保形层和领域先验，实现端到端训练和结构感知覆盖保证。
- 实验或效果：在多种模态下覆盖退化最多5%，校准误差降低30-50%，下游配体对接成功率提升25%。

## 摘要（原文）

> Deep protein structure predictors such as AlphaFold provide confidence estimates (e.g., pLDDT) that are often miscalibrated and degrade under distribution shifts across experimental modalities, temporal changes, and intrinsically disordered regions. We introduce CalPro, a prior-aware evidential-conformal framework for shift-robust uncertainty quantification. CalPro combines (i) a geometric evidential head that outputs Normal-Inverse-Gamma predictive distributions via a graph-based architecture; (ii) a differentiable conformal layer that enables end-to-end training with finite-sample coverage guarantees; and (iii) domain priors (disorder, flexibility) encoded as soft constraints. We derive structure-aware coverage guarantees under distribution shift using PAC-Bayesian bounds over ambiguity sets, and show that CalPro maintains near-nominal coverage while producing tighter intervals than standard conformal methods in regions where priors are informative. Empirically, CalPro exhibits at most 5% coverage degradation across modalities (vs. 15-25% for baselines), reduces calibration error by 30-50%, and improves downstream ligand-docking success by 25%. Beyond proteins, CalPro applies to structured regression tasks in which priors encode local reliability, validated on non-biological benchmarks.

