---
layout: default
title: Alzheimer's Disease Brain Network Mining
---

# Alzheimer's Disease Brain Network Mining
**arXiv**：[2512.17276v1](https://arxiv.org/abs/2512.17276) · [PDF](https://arxiv.org/pdf/2512.17276.pdf)  
**作者**：Alireza Moayedikia, Sara Fin  

**一句话要点**：提出MATCH-AD半监督框架，利用多视图自适应传输聚类解决阿尔茨海默病诊断中标签稀缺问题。

**关键词**：阿尔茨海默病诊断, 半监督学习, 多视图聚类, 最优传输, 神经影像分析, 标签传播

## 3 点简述
- 阿尔茨海默病诊断面临临床评估昂贵且侵入性，导致神经影像数据标签稀缺的核心挑战。
- MATCH-AD整合深度表示学习、图标签传播和最优传输理论，通过流形结构和Wasserstein距离传播诊断信息。
- 在近五千名受试者数据上评估，标签不足三分之一时实现近乎完美的诊断准确性，显著优于基线方法。

## 摘要（原文）

> Machine learning approaches for Alzheimer's disease (AD) diagnosis face a fundamental challenges. Clinical assessments are expensive and invasive, leaving ground truth labels available for only a fraction of neuroimaging datasets. We introduce Multi view Adaptive Transport Clustering for Heterogeneous Alzheimer's Disease (MATCH-AD), a semi supervised framework that integrates deep representation learning, graph-based label propagation, and optimal transport theory to address this limitation. The framework leverages manifold structure in neuroimaging data to propagate diagnostic information from limited labeled samples to larger unlabeled populations, while using Wasserstein distances to quantify disease progression between cognitive states. Evaluated on nearly five thousand subjects from the National Alzheimer's Coordinating Center, encompassing structural MRI measurements from hundreds of brain regions, cerebrospinal fluid biomarkers, and clinical variables MATCHAD achieves near-perfect diagnostic accuracy despite ground truth labels for less than one-third of subjects. The framework substantially outperforms all baseline methods, achieving kappa indicating almost perfect agreement compared to weak agreement for the best baseline, a qualitative transformation in diagnostic reliability. Performance remains clinically useful even under severe label scarcity, and we provide theoretical convergence guarantees with proven bounds on label propagation error and transport stability. These results demonstrate that principled semi-supervised learning can unlock the diagnostic potential of the vast repositories of partially annotated neuroimaging data accumulating worldwide, substantially reducing annotation burden while maintaining accuracy suitable for clinical deployment.

