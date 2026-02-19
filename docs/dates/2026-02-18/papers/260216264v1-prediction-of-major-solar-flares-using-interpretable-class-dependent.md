---
layout: default
title: Prediction of Major Solar Flares Using Interpretable Class-dependent Reward Framework with Active Region Magnetograms and Domain Knowledge
---

# Prediction of Major Solar Flares Using Interpretable Class-dependent Reward Framework with Active Region Magnetograms and Domain Knowledge
**arXiv**：[2602.16264v1](https://arxiv.org/abs/2602.16264) · [PDF](https://arxiv.org/pdf/2602.16264.pdf)  
**作者**：Zixian Wu, Xuebao Li, Yanfang Zheng, Rui Wang, Shunhuang Zhang, Jinfang Wei, Yongshang Lv, Liang Dong, Zamri Zainal Abidin, Noraisyah Mohamed Shah, Hongwei Ye, Pengchao Yan, Xuefeng Li, Xiaojia Ji, Xusheng Huang, Xiaotian Wang, Honglei Jin  

**一句话要点**：提出基于类别依赖奖励框架的监督分类方法，用于预测24小时内≥MM级太阳耀斑。

**关键词**：太阳耀斑预测, 类别依赖奖励, 深度学习模型, 磁图分析, 模型可解释性, 监督分类

## 3 点简述
- 核心问题：预测太阳耀斑，结合磁图与领域知识特征，提升准确性和可解释性。
- 方法要点：开发类别依赖奖励框架，集成CNN、CNN-BiLSTM和Transformer模型，优化分类性能。
- 实验或效果：CDR-Transformer在知识特征上表现最佳，优于NASA/CCMC，并通过SHAP分析增强模型可解释性。

## 摘要（原文）

> In this work, we develop, for the first time, a supervised classification framework with class-dependent rewards (CDR) to predict $\geq$MM flares within 24 hr. We construct multiple datasets, covering knowledge-informed features and line-of sight (LOS) magnetograms. We also apply three deep learning models (CNN, CNN-BiLSTM, and Transformer) and three CDR counterparts (CDR-CNN, CDR-CNN-BiLSTM, and CDR-Transformer). First, we analyze the importance of LOS magnetic field parameters with the Transformer, then compare its performance using LOS-only, vector-only, and combined magnetic field parameters. Second, we compare flare prediction performance based on CDR models versus deep learning counterparts. Third, we perform sensitivity analysis on reward engineering for CDR models. Fourth, we use the SHAP method for model interpretability. Finally, we conduct performance comparison between our models and NASA/CCMC. The main findings are: (1)Among LOS feature combinations, R_VALUE and AREA_ACR consistently yield the best results. (2)Transformer achieves better performance with combined LOS and vector magnetic field data than with either alone. (3)Models using knowledge-informed features outperform those using magnetograms. (4)While CNN and CNN-BiLSTM outperform their CDR counterparts on magnetograms, CDR-Transformer is slightly superior to its deep learning counterpart when using knowledge-informed features. Among all models, CDR-Transformer achieves the best performance. (5)The predictive performance of the CDR models is not overly sensitive to the reward choices.(6)Through SHAP analysis, the CDR model tends to regard TOTUSJH as more important, while the Transformer tends to prioritize R_VALUE more.(7)Under identical prediction time and active region (AR) number, the CDR-Transformer shows superior predictive capabilities compared to NASA/CCMC.

