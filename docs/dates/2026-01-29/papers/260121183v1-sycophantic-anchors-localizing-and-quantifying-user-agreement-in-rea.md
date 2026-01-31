---
layout: default
title: Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models
---

# Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models
**arXiv**：[2601.21183v1](https://arxiv.org/abs/2601.21183) · [PDF](https://arxiv.org/pdf/2601.21183.pdf)  
**作者**：Jacek Duszenko  

**一句话要点**：提出sycophantic anchors以定位和量化推理模型中的用户同意行为

**关键词**：推理模型, sycophancy, 定位量化, 线性探针, 激活回归, 模型对齐

## 3 点简述
- 核心问题：推理模型常错误同意用户建议，但同意起源和强度未知
- 方法要点：引入sycophantic anchors句子，通过线性探针和激活回归器定位量化
- 实验或效果：在蒸馏模型上分析超万次反事实推演，准确率达84.6%，R²为0.74

## 摘要（原文）

> Reasoning models frequently agree with incorrect user suggestions -- a behavior known as sycophancy. However, it is unclear where in the reasoning trace this agreement originates and how strong the commitment is. To localize and quantify this behavior, we introduce \emph{sycophantic anchors} -- sentences that causally lock models into user agreement. Analyzing over 10,000 counterfactual rollouts on a distilled reasoning model, we show that anchors can be reliably detected and quantified mid-inference. Linear probes distinguish sycophantic anchors with 84.6\% balanced accuracy, while activation-based regressors predict the magnitude of the commitment ($R^2 = 0.74$). We further observe asymmetry where sycophantic anchors are significantly more distinguishable than correct reasoning anchors, and find that sycophancy builds gradually during reasoning, revealing a potential window for intervention. These results offer sentence-level mechanisms for localizing model misalignment mid-inference.

