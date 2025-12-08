---
layout: default
title: Improving Local Fidelity Through Sampling and Modeling Nonlinearity
---

# Improving Local Fidelity Through Sampling and Modeling Nonlinearity
**arXiv**：[2512.05556v1](https://arxiv.org/abs/2512.05556) · [PDF](https://arxiv.org/pdf/2512.05556.pdf)  
**作者**：Sanjeev Shrestha, Rahul Dubey, Hui Liu  

**一句话要点**：提出基于MARS和N-ball采样的方法，以提升黑盒模型局部解释的保真度。

**关键词**：局部可解释性, 非线性建模, MARS, N-ball采样, 黑盒模型解释, 保真度提升

## 3 点简述
- 核心问题：LIME假设局部决策边界线性，无法捕捉非线性关系，导致解释不准确。
- 方法要点：使用MARS建模非线性局部边界，结合N-ball采样技术直接采样，提高解释的忠实性。
- 实验或效果：在三个UCI数据集上评估，相比基线平均降低37%的RMSE，显著提升局部保真度。

## 摘要（原文）

> With the increasing complexity of black-box machine learning models and their adoption in high-stakes areas, it is critical to provide explanations for their predictions. Local Interpretable Model-agnostic Explanation (LIME) is a widely used technique that explains the prediction of any classifier by learning an interpretable model locally around the predicted instance. However, it assumes that the local decision boundary is linear and fails to capture the non-linear relationships, leading to incorrect explanations. In this paper, we propose a novel method that can generate high-fidelity explanations. Multivariate adaptive regression splines (MARS) is used to model non-linear local boundaries that effectively captures the underlying behavior of the reference model, thereby enhancing the local fidelity of the explanation. Additionally, we utilize the N-ball sampling technique, which samples directly from the desired distribution instead of reweighting samples as done in LIME, further improving the faithfulness score. We evaluate our method on three UCI datasets across different classifiers and varying kernel widths. Experimental results show that our method yields more faithful explanations compared to baselines, achieving an average reduction of 37% in root mean square error, significantly improving local fidelity.

