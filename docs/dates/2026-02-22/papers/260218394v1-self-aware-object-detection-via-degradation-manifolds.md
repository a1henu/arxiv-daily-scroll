---
layout: default
title: Self-Aware Object Detection via Degradation Manifolds
---

# Self-Aware Object Detection via Degradation Manifolds
**arXiv**：[2602.18394v1](https://arxiv.org/abs/2602.18394) · [PDF](https://arxiv.org/pdf/2602.18394.pdf)  
**作者**：Stefan Becker, Simon Weiss, Wolfgang Hübner, Michael Arens  

**一句话要点**：提出基于退化流形的自感知目标检测框架，以评估输入是否在检测器名义操作范围内。

**关键词**：自感知目标检测, 退化流形, 对比学习, 特征空间结构化, 零样本迁移, 分布偏移

## 3 点简述
- 核心问题：目标检测器在模糊、噪声等退化条件下可能无声失败，需自感知能力评估输入状态。
- 方法要点：通过多层对比学习训练轻量嵌入头，结构化特征空间以捕获退化类型和严重程度，无需退化标签。
- 实验或效果：在合成退化基准、跨数据集零样本迁移和自然天气分布偏移中展示强分离性和泛化能力。

## 摘要（原文）

> Object detectors achieve strong performance under nominal imaging conditions but can fail silently when exposed to blur, noise, compression, adverse weather, or resolution changes. In safety-critical settings, it is therefore insufficient to produce predictions without assessing whether the input remains within the detector's nominal operating regime. We refer to this capability as self-aware object detection.
>   We introduce a degradation-aware self-awareness framework based on degradation manifolds, which explicitly structure a detector's feature space according to image degradation rather than semantic content. Our method augments a standard detection backbone with a lightweight embedding head trained via multi-layer contrastive learning. Images sharing the same degradation composition are pulled together, while differing degradation configurations are pushed apart, yielding a geometrically organized representation that captures degradation type and severity without requiring degradation labels or explicit density modeling.
>   To anchor the learned geometry, we estimate a pristine prototype from clean training embeddings, defining a nominal operating point in representation space. Self-awareness emerges as geometric deviation from this reference, providing an intrinsic, image-level signal of degradation-induced shift that is independent of detection confidence.
>   Extensive experiments on synthetic corruption benchmarks, cross-dataset zero-shot transfer, and natural weather-induced distribution shifts demonstrate strong pristine-degraded separability, consistent behavior across multiple detector architectures, and robust generalization under semantic shift. These results suggest that degradation-aware representation geometry provides a practical and detector-agnostic foundation.

