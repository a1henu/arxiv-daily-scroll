---
layout: default
title: Understanding Model Merging: A Unified Generalization Framework for Heterogeneous Experts
---

# Understanding Model Merging: A Unified Generalization Framework for Heterogeneous Experts
**arXiv**：[2601.21690v1](https://arxiv.org/abs/2601.21690) · [PDF](https://arxiv.org/pdf/2601.21690.pdf)  
**作者**：Qinglun Li, Anke Tang, Miao Zhang, Mengzhu Wang, Quanjun Yin, Li Shen  

**一句话要点**：提出基于L2稳定性理论的统一框架，以解决异构专家模型合并的泛化问题并提供调优建议。

**关键词**：模型合并, 异构专家, 泛化理论, L2稳定性, 微调超参数, 视觉分类

## 3 点简述
- 核心问题：异构微调超参数下模型合并缺乏统一理论，且开源模型超参数不透明影响合并性能预测。
- 方法要点：利用L2稳定性理论分析合并模型泛化，解释现有算法并优化理论界中的特定项。
- 实验或效果：在ResNet/ViT家族上跨多任务实验，验证超参数对合并模型泛化的影响，支持理论预测。

## 摘要（原文）

> Model merging efficiently aggregates capabilities from multiple fine-tuned models into a single one, operating purely in parameter space without original data or expensive re-computation. Despite empirical successes, a unified theory for its effectiveness under heterogeneous finetuning hyperparameters (e.g., varying learning rates, batch sizes) remains missing. Moreover, the lack of hyperparameter transparency in open-source fine-tuned models makes it difficult to predict merged-model performance, leaving practitioners without guidance on how to fine-tune merge-friendly experts. To address those two challenges, we employ $L_2$-Stability theory under heterogeneous hyperparameter environments to analyze the generalization of the merged model $\boldsymbol{x}_{avg}$. This pioneering analysis yields two key contributions: (i) \textit{A unified theoretical framework} is provided to explain existing merging algorithms, revealing how they optimize specific terms in our bound, thus offering a strong theoretical foundation for empirical observations. (ii) \textit{Actionable recommendations} are proposed for practitioners to strategically fine-tune expert models, enabling the construction of merge-friendly models within the pretraining-to-finetuning pipeline. Extensive experiments on the ResNet/Vit family across 20/8 visual classification tasks, involving thousands of finetuning models, robustly confirm the impact of different hyperparameters on the generalization of $\boldsymbol{x}_{avg}$ predicted by our theoretical results.

