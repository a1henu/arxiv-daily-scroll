---
layout: default
title: Missingness Bias Calibration in Feature Attribution Explanations
---

# Missingness Bias Calibration in Feature Attribution Explanations
**arXiv**：[2603.04831v1](https://arxiv.org/abs/2603.04831) · [PDF](https://arxiv.org/pdf/2603.04831.pdf)  
**作者**：Shailesh Sridhar, Anton Xue, Eric Wong  

**一句话要点**：提出MCal方法以校准特征归因解释中的缺失性偏差，无需重训练模型。

**关键词**：特征归因解释, 缺失性偏差校准, 后处理方法, 医疗基准测试, 模型输出空间

## 3 点简述
- 核心问题：特征重要性评分因缺失性偏差不可靠，源于模型处理分布外输入时的系统失真。
- 方法要点：MCal作为轻量级后处理方法，通过微调冻结基础模型输出上的线性头来校正偏差。
- 实验或效果：在医疗多领域基准测试中，MCal有效减少偏差，性能优于或媲美复杂方法。

## 摘要（原文）

> Popular explanation methods often produce unreliable feature importance scores due to missingness bias, a systematic distortion that arises when models are probed with ablated, out-of-distribution inputs. Existing solutions treat this as a deep representational flaw that requires expensive retraining or architectural modifications. In this work, we challenge this assumption and show that missingness bias can be effectively treated as a superficial artifact of the model's output space. We introduce MCal, a lightweight post-hoc method that corrects this bias by fine-tuning a simple linear head on the outputs of a frozen base model. Surprisingly, we find this simple correction consistently reduces missingness bias and is competitive with, or even outperforms, prior heavyweight approaches across diverse medical benchmarks spanning vision, language, and tabular domains.

