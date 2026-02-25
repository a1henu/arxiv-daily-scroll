---
layout: default
title: Multimodal MRI Report Findings Supervised Brain Lesion Segmentation with Substructures
---

# Multimodal MRI Report Findings Supervised Brain Lesion Segmentation with Substructures
**arXiv**：[2602.20994v1](https://arxiv.org/abs/2602.20994) · [PDF](https://arxiv.org/pdf/2602.20994.pdf)  
**作者**：Yubin Ge, Yongsong Huang, Xiaofeng Liu  

**一句话要点**：提出MS-RSuper方法以解决多模态MRI报告监督下脑病灶分割中报告不完整和层次化信息利用不足的问题

**关键词**：脑病灶分割, 报告监督学习, 多模态MRI, 不确定性建模, 解剖先验

## 3 点简述
- 核心问题：脑肿瘤MRI报告常仅描述最大病灶，提供定性或不确定线索，导致传统报告监督方法过约束或产生幻觉
- 方法要点：解析全局定量和模态定性发现，引入统一、单边、不确定性感知的损失函数，对齐模态线索并利用解剖先验
- 实验或效果：在1238个报告标注的BraTS-MET/MEN扫描上，MS-RSuper显著优于稀疏监督基线和朴素报告监督方法

## 摘要（原文）

> Report-supervised (RSuper) learning seeks to alleviate the need for dense tumor voxel labels with constraints derived from radiology reports (e.g., volumes, counts, sizes, locations). In MRI studies of brain tumors, however, we often involve multi-parametric scans and substructures. Here, fine-grained modality/parameter-wise reports are usually provided along with global findings and are correlated with different substructures. Moreover, the reports often describe only the largest lesion and provide qualitative or uncertain cues (``mild,'' ``possible''). Classical RSuper losses (e.g., sum volume consistency) can over-constrain or hallucinate unreported findings under such incompleteness, and are unable to utilize these hierarchical findings or exploit the priors of varied lesion types in a merged dataset. We explicitly parse the global quantitative and modality-wise qualitative findings and introduce a unified, one-sided, uncertainty-aware formulation (MS-RSuper) that: (i) aligns modality-specific qualitative cues (e.g., T1c enhancement, FLAIR edema) with their corresponding substructures using existence and absence losses; (ii) enforces one-sided lower-bounds for partial quantitative cues (e.g., largest lesion size, minimal multiplicity); and (iii) adds extra- vs. intra-axial anatomical priors to respect cohort differences. Certainty tokens scale penalties; missing cues are down-weighted. On 1238 report-labeled BraTS-MET/MEN scans, our MS-RSuper largely outperforms both a sparsely-supervised baseline and a naive RSuper method.

