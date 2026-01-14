---
layout: default
title: Intra-tree Column Subsampling Hinders XGBoost Learning of Ratio-like Interactions
---

# Intra-tree Column Subsampling Hinders XGBoost Learning of Ratio-like Interactions
**arXiv**：[2601.08121v1](https://arxiv.org/abs/2601.08121) · [PDF](https://arxiv.org/pdf/2601.08121.pdf)  
**作者**：Mykola Pinchuk  

**一句话要点**：研究XGBoost中树内列子采样对比率类交互学习的影响，建议避免或添加比率特征

**关键词**：XGBoost, 列子采样, 比率交互, 梯度提升树, 特征工程, 合成数据

## 3 点简述
- 核心问题：XGBoost树内列子采样是否阻碍比率类交互的学习，影响模型性能
- 方法要点：使用合成数据模拟比率结构，通过调整子采样参数和添加工程化比率特征进行实验
- 实验或效果：子采样降低测试PR-AUC，添加比率特征可缓解，相对降幅最高达54%

## 摘要（原文）

> Many applied problems contain signal that becomes clear only after combining multiple raw measurements. Ratios and rates are common examples. In gradient boosted trees, this combination is not an explicit operation: the model must synthesize it through coordinated splits on the component features. We study whether intra-tree column subsampling in XGBoost makes that synthesis harder. We use two synthetic data generating processes with cancellation-style structure. In both, two primitive features share a strong nuisance factor, while the target depends on a smaller differential factor. A log ratio cancels the nuisance and isolates the signal. We vary colsample_bylevel and colsample_bynode over s in {0.4, 0.6, 0.8, 0.9}, emphasizing mild subsampling (s >= 0.8). A control feature set includes the engineered ratio, removing the need for synthesis. Across both processes, intra-tree column subsampling reduces test PR-AUC in the primitives-only setting. In the main process the relative decrease reaches 54 percent when both parameters are set to 0.4. The effect largely disappears when the engineered ratio is present. A path-based co-usage metric drops in the same cells where performance deteriorates. Practically, if ratio-like structure is plausible, either avoid intra-tree subsampling or include the intended ratio features.

