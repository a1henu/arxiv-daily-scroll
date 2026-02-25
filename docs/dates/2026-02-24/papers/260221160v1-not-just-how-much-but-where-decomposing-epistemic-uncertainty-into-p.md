---
layout: default
title: Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions
---

# Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions
**arXiv**：[2602.21160v1](https://arxiv.org/abs/2602.21160) · [PDF](https://arxiv.org/pdf/2602.21160.pdf)  
**作者**：Mame Diarra Toure, David A. Stephens  

**一句话要点**：提出分解互信息为每类贡献以解决安全关键分类中不确定性不对称问题

**关键词**：贝叶斯深度学习, 不确定性分解, 安全关键分类, 互信息, 每类贡献, 选择性预测

## 3 点简述
- 核心问题：贝叶斯深度学习中互信息无法区分模型对良性或安全关键类的无知
- 方法要点：通过二阶泰勒展开将互信息分解为每类向量，校正边界抑制并实现跨类可比
- 实验或效果：在糖尿病视网膜病变等任务中，关键类贡献显著降低选择风险并提升检测性能

## 摘要（原文）

> In safety-critical classification, the cost of failure is often asymmetric, yet Bayesian deep learning summarises epistemic uncertainty with a single scalar, mutual information (MI), that cannot distinguish whether a model's ignorance involves a benign or safety-critical class. We decompose MI into a per-class vector $C_k(x)=σ_k^{2}/(2μ_k)$, with $μ_k{=}\mathbb{E}[p_k]$ and $σ_k^2{=}\mathrm{Var}[p_k]$ across posterior samples. The decomposition follows from a second-order Taylor expansion of the entropy; the $1/μ_k$ weighting corrects boundary suppression and makes $C_k$ comparable across rare and common classes. By construction $\sum_k C_k \approx \mathrm{MI}$, and a companion skewness diagnostic flags inputs where the approximation degrades. After characterising the axiomatic properties of $C_k$, we validate it on three tasks: (i) selective prediction for diabetic retinopathy, where critical-class $C_k$ reduces selective risk by 34.7\% over MI and 56.2\% over variance baselines; (ii) out-of-distribution detection on clinical and image benchmarks, where $\sum_k C_k$ achieves the highest AUROC and the per-class view exposes asymmetric shifts invisible to MI; and (iii) a controlled label-noise study in which $\sum_k C_k$ shows less sensitivity to injected aleatoric noise than MI under end-to-end Bayesian training, while both metrics degrade under transfer learning. Across all tasks, the quality of the posterior approximation shapes uncertainty at least as strongly as the choice of metric, suggesting that how uncertainty is propagated through the network matters as much as how it is measured.

