---
layout: default
title: Fair-Eye Net: A Fair, Trustworthy, Multimodal Integrated Glaucoma Full Chain AI System
---

# Fair-Eye Net: A Fair, Trustworthy, Multimodal Integrated Glaucoma Full Chain AI System
**arXiv**：[2601.18464v1](https://arxiv.org/abs/2601.18464) · [PDF](https://arxiv.org/pdf/2601.18464.pdf)  
**作者**：Wenbin Wei, Suyuan Yao, Cheng Huang, Xiangyu Gao  

**一句话要点**：提出Fair-Eye Net公平多模态AI系统，以解决青光眼筛查与随访中的主观性和公平性问题。

**关键词**：多模态融合, 公平性约束, 青光眼AI, 不确定性感知, 临床可靠性, 异构数据集成

## 3 点简述
- 核心问题：青光眼筛查依赖单测试或松散检查，导致主观性、碎片化护理和公平性不足。
- 方法要点：集成眼底照片、OCT、视野和人口因素，采用双流异构融合和不确定性感知门控策略。
- 实验或效果：AUC达0.912，减少种族假阴性差异73.4%，实现早期风险预警（92%敏感度，88%特异度）。

## 摘要（原文）

> Glaucoma is a top cause of irreversible blindness globally, making early detection and longitudinal follow-up pivotal to preventing permanent vision loss. Current screening and progression assessment, however, rely on single tests or loosely linked examinations, introducing subjectivity and fragmented care. Limited access to high-quality imaging tools and specialist expertise further compromises consistency and equity in real-world use. To address these gaps, we developed Fair-Eye Net, a fair, reliable multimodal AI system closing the clinical loop from glaucoma screening to follow-up and risk alerting. It integrates fundus photos, OCT structural metrics, VF functional indices, and demographic factors via a dual-stream heterogeneous fusion architecture, with an uncertainty-aware hierarchical gating strategy for selective prediction and safe referral. A fairness constraint reduces missed diagnoses in disadvantaged subgroups. Experimental results show it achieved an AUC of 0.912 (96.7% specificity), cut racial false-negativity disparity by 73.4% (12.31% to 3.28%), maintained stable cross-domain performance, and enabled 3-12 months of early risk alerts (92% sensitivity, 88% specificity). Unlike post hoc fairness adjustments, Fair-Eye Net optimizes fairness as a primary goal with clinical reliability via multitask learning, offering a reproducible path for clinical translation and large-scale deployment to advance global eye health equity.

