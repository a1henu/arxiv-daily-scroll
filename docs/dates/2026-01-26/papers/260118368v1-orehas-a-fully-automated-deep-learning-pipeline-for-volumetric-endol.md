---
layout: default
title: OREHAS: A fully automated deep-learning pipeline for volumetric endolymphatic hydrops quantification in MRI
---

# OREHAS: A fully automated deep-learning pipeline for volumetric endolymphatic hydrops quantification in MRI
**arXiv**：[2601.18368v1](https://arxiv.org/abs/2601.18368) · [PDF](https://arxiv.org/pdf/2601.18368.pdf)  
**作者**：Caterina Fuster-Barceló, Claudia Castrillón, Laura Rodrigo-Muñoz, Victor Manuel Vega-Suárez, Nicolás Pérez-Fernández, Gorka Bastarrika, Arrate Muñoz-Barrutia  

**一句话要点**：提出OREHAS全自动深度学习流程，用于MRI中内淋巴积水的体积量化

**关键词**：内淋巴积水量化, 深度学习分割, MRI体积分析, 自动化流程, 内耳成像

## 3 点简述
- 核心问题：内淋巴积水（EH）的量化依赖手动干预，缺乏自动化方法。
- 方法要点：集成切片分类、内耳定位和序列特定分割，实现端到端体积比计算。
- 实验或效果：在外部验证中，OREHAS接近专家标注，优于临床软件，减少操作依赖性。

## 摘要（原文）

> We present OREHAS (Optimized Recognition & Evaluation of volumetric Hydrops in the Auditory System), the first fully automatic pipeline for volumetric quantification of endolymphatic hydrops (EH) from routine 3D-SPACE-MRC and 3D-REAL-IR MRI. The system integrates three components -- slice classification, inner ear localization, and sequence-specific segmentation -- into a single workflow that computes per-ear endolymphatic-to-vestibular volume ratios (ELR) directly from whole MRI volumes, eliminating the need for manual intervention.
>   Trained with only 3 to 6 annotated slices per patient, OREHAS generalized effectively to full 3D volumes, achieving Dice scores of 0.90 for SPACE-MRC and 0.75 for REAL-IR. In an external validation cohort with complete manual annotations, OREHAS closely matched expert ground truth (VSI = 74.3%) and substantially outperformed the clinical syngo.via software (VSI = 42.5%), which tended to overestimate endolymphatic volumes. Across 19 test patients, vestibular measurements from OREHAS were consistent with syngo.via, while endolymphatic volumes were systematically smaller and more physiologically realistic.
>   These results show that reliable and reproducible EH quantification can be achieved from standard MRI using limited supervision. By combining efficient deep-learning-based segmentation with a clinically aligned volumetric workflow, OREHAS reduces operator dependence, ensures methodological consistency. Besides, the results are compatible with established imaging protocols. The approach provides a robust foundation for large-scale studies and for recalibrating clinical diagnostic thresholds based on accurate volumetric measurements of the inner ear.

