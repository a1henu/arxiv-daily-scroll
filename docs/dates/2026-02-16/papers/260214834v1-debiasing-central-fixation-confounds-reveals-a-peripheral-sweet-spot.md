---
layout: default
title: Debiasing Central Fixation Confounds Reveals a Peripheral "Sweet Spot" for Human-like Scanpaths in Hard-Attention Vision
---

# Debiasing Central Fixation Confounds Reveals a Peripheral "Sweet Spot" for Human-like Scanpaths in Hard-Attention Vision
**arXiv**：[2602.14834v1](https://arxiv.org/abs/2602.14834) · [PDF](https://arxiv.org/pdf/2602.14834.pdf)  
**作者**：Pengcheng Pan, Yonekura Shogo, Yasuo Kuniyosh  

**一句话要点**：提出GCS指标以解决硬注意模型评估中的中心偏差混淆问题

**关键词**：硬注意模型, 扫描路径评估, 中心偏差, 视觉识别, Gaze-CIFAR-10, 主动感知

## 3 点简述
- 核心问题：标准扫描路径指标受数据集中心偏差影响，难以区分真实行为对齐与中心趋势
- 方法要点：提出GCS（注视一致性分数），结合中心去偏和运动相似性，评估扫描路径
- 实验或效果：在Gaze-CIFAR-10上揭示外围感知的“甜点”区域，优化硬注意模型设计

## 摘要（原文）

> Human eye movements in visual recognition reflect a balance between foveal sampling and peripheral context. Task-driven hard-attention models for vision are often evaluated by how well their scanpaths match human gaze. However, common scanpath metrics can be strongly confounded by dataset-specific center bias, especially on object-centric datasets. Using Gaze-CIFAR-10, we show that a trivial center-fixation baseline achieves surprisingly strong scanpath scores, approaching many learned policies. This makes standard metrics optimistic and blurs the distinction between genuine behavioral alignment and mere central tendency. We then analyze a hard-attention classifier under constrained vision by sweeping foveal patch size and peripheral context, revealing a peripheral sweet spot: only a narrow range of sensory constraints yields scanpaths that are simultaneously (i) above the center baseline after debiasing and (ii) temporally human-like in movement statistics. To address center bias, we propose GCS (Gaze Consistency Score), a center-debiased composite metric augmented with movement similarity. GCS uncovers a robust sweet spot at medium patch size with both foveal and peripheral vision, that is not obvious from raw scanpath metrics or accuracy alone, and also highlights a "shortcut regime" when the field-of-view becomes too large. We discuss implications for evaluating active perception on object-centric datasets and for designing gaze benchmarks that better separate behavioral alignment from center bias.

