---
layout: default
title: Beyond Accuracy: A Unified Random Matrix Theory Diagnostic Framework for Crash Classification Models
---

# Beyond Accuracy: A Unified Random Matrix Theory Diagnostic Framework for Crash Classification Models
**arXiv**：[2602.19528v1](https://arxiv.org/abs/2602.19528) · [PDF](https://arxiv.org/pdf/2602.19528.pdf)  
**作者**：Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  

**一句话要点**：提出基于随机矩阵理论的谱诊断框架，以解决交通碰撞分类模型过拟合检测问题。

**关键词**：随机矩阵理论, 模型诊断, 过拟合检测, 交通碰撞分类, 谱分析, 机器学习评估

## 3 点简述
- 核心问题：传统准确率等指标无法揭示模型是否在无声过拟合。
- 方法要点：利用随机矩阵理论和重尾自正则化，分析多种模型类型的谱结构。
- 实验或效果：在爱荷华州数据集上验证，幂律指数α与专家判断强相关，并提出基于α的模型选择准则。

## 摘要（原文）

> Crash classification models in transportation safety are typically evaluated using accuracy, F1, or AUC, metrics that cannot reveal whether a model is silently overfitting. We introduce a spectral diagnostic framework grounded in Random Matrix Theory (RMT) and Heavy-Tailed Self-Regularization (HTSR) that spans the ML taxonomy: weight matrices for BERT/ALBERT/Qwen2.5, out-of-fold increment matrices for XGBoost/Random Forest, empirical Hessians for Logistic Regression, induced affinity matrices for Decision Trees, and Graph Laplacians for KNN. Evaluating nine model families on two Iowa DOT crash classification tasks (173,512 and 371,062 records respectively), we find that the power-law exponent $α$ provides a structural quality signal: well-regularized models consistently yield $α$ within $[2, 4]$ (mean $2.87 \pm 0.34$), while overfit variants show $α< 2$ or spectral collapse. We observe a strong rank correlation between $α$ and expert agreement (Spearman $ρ= 0.89$, $p < 0.001$), suggesting spectral quality captures model behaviors aligned with expert reasoning. We propose an $α$-based early stopping criterion and a spectral model selection protocol, and validate both against cross-validated F1 baselines. Sparse Lanczos approximations make the framework scalable to large datasets.

