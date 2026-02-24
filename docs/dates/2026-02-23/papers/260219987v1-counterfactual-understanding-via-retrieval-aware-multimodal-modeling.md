---
layout: default
title: Counterfactual Understanding via Retrieval-aware Multimodal Modeling for Time-to-Event Survival Prediction
---

# Counterfactual Understanding via Retrieval-aware Multimodal Modeling for Time-to-Event Survival Prediction
**arXiv**：[2602.19987v1](https://arxiv.org/abs/2602.19987) · [PDF](https://arxiv.org/pdf/2602.19987.pdf)  
**作者**：Ha-Anh Hoang Nguyen, Tri-Duc Phan Le, Duc-Hoang Pham, Huy-Son Nguyen, Cam-Van Thi Nguyen, Duc-Trong Le, Hoang-Quynh Le  

**一句话要点**：提出CURE框架，通过检索感知多模态建模解决异质性和删失数据下的个体化生存预测问题。

**关键词**：生存预测, 多模态建模, 检索感知, 反事实分析, 个体化治疗

## 3 点简述
- 核心问题：针对异质性和删失数据，优化个体化生存预测，以支持治疗决策。
- 方法要点：整合多模态信息，利用交叉注意力和专家混合架构自适应精炼信号，并检索潜在亚组。
- 实验或效果：在METABRIC和TCGA-LUAD数据集上，CURE在生存分析指标上优于基线模型。

## 摘要（原文）

> This paper tackles the problem of time-to-event counterfactual survival prediction, aiming to optimize individualized survival outcomes in the presence of heterogeneity and censored data. We propose CURE, a framework that advances counterfactual survival modeling via comprehensive multimodal embedding and latent subgroup retrieval. CURE integrates clinical, paraclinical, demographic, and multi-omics information, which are aligned and fused through cross-attention mechanisms. Complex multi-omics signals can be adaptively refined using a mixture-of-experts architecture, emphasizing the most informative omics components. Building upon this representation, CURE implicitly retrieves patient-specific latent subgroups that capture both baseline survival dynamics and treatment-dependent variations. Experimental results on METABRIC and TCGA-LUAD datasets demonstrate that proposed CURE model consistently outperforms strong baselines in survival analysis, evaluated using the Time-dependent Concordance Index ($C^{td}$) and Integrated Brier Score (IBS). These findings highlight the potential of CURE to enhance multimodal understanding and serve as a foundation for future treatment recommendation models. All code and related resources are publicly available to facilitate the reproducibility https://github.com/L2R-UET/CURE.

