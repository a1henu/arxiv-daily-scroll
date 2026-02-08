---
layout: default
title: Context-Aware Asymmetric Ensembling for Interpretable Retinopathy of Prematurity Screening via Active Query and Vascular Attention
---

# Context-Aware Asymmetric Ensembling for Interpretable Retinopathy of Prematurity Screening via Active Query and Vascular Attention
**arXiv**：[2602.05208v1](https://arxiv.org/abs/2602.05208) · [PDF](https://arxiv.org/pdf/2602.05208.pdf)  
**作者**：Md. Mehedi Hassan, Taufiq Hasan  

**一句话要点**：提出上下文感知非对称集成模型，通过主动查询和血管注意力实现可解释的早产儿视网膜病变筛查。

**关键词**：早产儿视网膜病变筛查, 上下文感知集成, 主动查询网络, 血管拓扑图, 可解释性, 医学图像分析

## 3 点简述
- 核心问题：早产儿视网膜病变筛查数据有限且复杂，现有模型泛化能力差。
- 方法要点：使用多尺度主动查询网络和血管拓扑图编码，模拟临床推理进行集成。
- 实验或效果：在188名婴儿数据集上，实现宏F1分数0.93和AUC 0.996的先进性能。

## 摘要（原文）

> Retinopathy of Prematurity (ROP) is among the major causes of preventable childhood blindness. Automated screening remains challenging, primarily due to limited data availability and the complex condition involving both structural staging and microvascular abnormalities. Current deep learning models depend heavily on large private datasets and passive multimodal fusion, which commonly fail to generalize on small, imbalanced public cohorts. We thus propose the Context-Aware Asymmetric Ensemble Model (CAA Ensemble) that simulates clinical reasoning through two specialized streams. First, the Multi-Scale Active Query Network (MS-AQNet) serves as a structure specialist, utilizing clinical contexts as dynamic query vectors to spatially control visual feature extraction for localization of the fibrovascular ridge. Secondly, VascuMIL encodes Vascular Topology Maps (VMAP) within a gated Multiple Instance Learning (MIL) network to precisely identify vascular tortuosity. A synergistic meta-learner ensembles these orthogonal signals to resolve diagnostic discordance across multiple objectives. Tested on a highly imbalanced cohort of 188 infants (6,004 images), the framework attained State-of-the-Art performance on two distinct clinical tasks: achieving a Macro F1-Score of 0.93 for Broad ROP staging and an AUC of 0.996 for Plus Disease detection. Crucially, the system features `Glass Box' transparency through counterfactual attention heatmaps and vascular threat maps, proving that clinical metadata dictates the model's visual search. Additionally, this study demonstrates that architectural inductive bias can serve as an effective bridge for the medical AI data gap.

