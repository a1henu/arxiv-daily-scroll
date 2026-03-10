---
layout: default
title: Towards plausibility in time series counterfactual explanations
---

# Towards plausibility in time series counterfactual explanations
**arXiv**：[2603.08349v1](https://arxiv.org/abs/2603.08349) · [PDF](https://arxiv.org/pdf/2603.08349.pdf)  
**作者**：Marcin Kostrzewa, Krzysztof Galus, Maciej Zięba  

**一句话要点**：提出基于梯度优化与软DTW对齐的方法，以生成时间序列分类中高可信度的反事实解释。

**关键词**：时间序列分类, 反事实解释, 软动态时间规整, 梯度优化, 可信度评估

## 3 点简述
- 核心问题：现有方法在生成时间序列反事实解释时，难以保持真实的时间结构，导致可信度不足。
- 方法要点：通过梯度优化直接操作输入空间，结合软DTW对齐和目标类k近邻，以多损失函数平衡有效性、稀疏性、邻近性和可信度。
- 实验或效果：在有效性上表现竞争性，在目标类分布对齐上显著优于现有方法，定性分析突出现有方法在时间结构保持上的局限性。

## 摘要（原文）

> We present a new method for generating plausible counterfactual explanations for time series classification problems. The approach performs gradient-based optimization directly in the input space. To enforce plausibility, we integrate soft-DTW (dynamic time warping) alignment with $k$-nearest neighbors from the target class, which effectively encourages the generated counterfactuals to adopt a realistic temporal structure. The overall optimization objective is a multi-faceted loss function that balances key counterfactual properties. It incorporates losses for validity, sparsity, and proximity, alongside the novel soft-DTW-based plausibility component. We conduct an evaluation of our method against several strong reference approaches, measuring the key properties of the generated counterfactuals across multiple dimensions. The results demonstrate that our method achieves competitive performance in validity while significantly outperforming existing approaches in distributional alignment with the target class, indicating superior temporal realism. Furthermore, a qualitative analysis highlights the critical limitations of existing methods in preserving realistic temporal structure. This work shows that the proposed method consistently generates counterfactual explanations for time series classifiers that are not only valid but also highly plausible and consistent with temporal patterns.

