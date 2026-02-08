---
layout: default
title: Phi-Former: A Pairwise Hierarchical Approach for Compound-Protein Interactions Prediction
---

# Phi-Former: A Pairwise Hierarchical Approach for Compound-Protein Interactions Prediction
**arXiv**：[2602.05479v1](https://arxiv.org/abs/2602.05479) · [PDF](https://arxiv.org/pdf/2602.05479.pdf)  
**作者**：Zhe Wang, Zijing Liu, Chencheng Xu, Yuan Yao  

**一句话要点**：提出Phi-Former，一种基于基序的层次化表示学习方法，用于预测化合物-蛋白质相互作用。

**关键词**：化合物-蛋白质相互作用预测, 层次化表示学习, 基序建模, 成对预训练, 可解释性, 药物发现

## 3 点简述
- 核心问题：现有原子级CPI模型未充分反映化学现实，基序作为生物识别和结合的关键单元被忽视。
- 方法要点：采用层次化表示和成对预训练框架，系统建模原子-原子、基序-基序和原子-基序的相互作用。
- 实验或效果：在CPI任务上表现优异，提供可解释的模型解释，支持药物设计和精准医疗应用。

## 摘要（原文）

> Drug discovery remains time-consuming, labor-intensive, and expensive, often requiring years and substantial investment per drug candidate. Predicting compound-protein interactions (CPIs) is a critical component in this process, enabling the identification of molecular interactions between drug candidates and target proteins. Recent deep learning methods have successfully modeled CPIs at the atomic level, achieving improved efficiency and accuracy over traditional energy-based approaches. However, these models do not always align with chemical realities, as molecular fragments (motifs or functional groups) typically serve as the primary units of biological recognition and binding. In this paper, we propose Phi-former, a pairwise hierarchical interaction representation learning method that addresses this gap by incorporating the biological role of motifs in CPIs. Phi-former represents compounds and proteins hierarchically and employs a pairwise pre-training framework to model interactions systematically across atom-atom, motif-motif, and atom-motif levels, reflecting how biological systems recognize molecular partners. We design intra-level and inter-level learning pipelines that make different interaction levels mutually beneficial. Experimental results demonstrate that Phi-former achieves superior performance on CPI-related tasks. A case study shows that our method accurately identifies specific atoms or motifs activated in CPIs, providing interpretable model explanations. These insights may guide rational drug design and support precision medicine applications.

