---
layout: default
title: Missingness Bias Calibration in Feature Attribution Explanations
---

# Missingness Bias Calibration in Feature Attribution Explanations
**arXiv**：[2603.04831v1](https://arxiv.org/abs/2603.04831) · [PDF](https://arxiv.org/pdf/2603.04831.pdf)  
**作者**：Shailesh Sridhar, Anton Xue, Eric Wong  

**一句话要点**：提出MCal方法，通过微调线性头校准特征归因解释中的缺失性偏差。

**关键词**：特征归因解释, 缺失性偏差校准, 后处理方法, 医疗基准, 模型输出空间

## 3 点简述
- 核心问题：特征归因方法因缺失性偏差产生不可靠重要性分数。
- 方法要点：MCal作为轻量级后处理方法，在冻结基础模型输出上微调线性头。
- 实验或效果：在医疗多领域基准上，MCal有效减少偏差，性能优于或媲美重型方法。

## 摘要（原文）

> Popular explanation methods often produce unreliable feature importance scores due to missingness bias, a systematic distortion that arises when models are probed with ablated, out-of-distribution inputs. Existing solutions treat this as a deep representational flaw that requires expensive retraining or architectural modifications. In this work, we challenge this assumption and show that missingness bias can be effectively treated as a superficial artifact of the model's output space. We introduce MCal, a lightweight post-hoc method that corrects this bias by fine-tuning a simple linear head on the outputs of a frozen base model. Surprisingly, we find this simple correction consistently reduces missingness bias and is competitive with, or even outperforms, prior heavyweight approaches across diverse medical benchmarks spanning vision, language, and tabular domains.

