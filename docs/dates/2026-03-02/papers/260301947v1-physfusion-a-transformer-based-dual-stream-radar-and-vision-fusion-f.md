---
layout: default
title: physfusion: A Transformer-based Dual-Stream Radar and Vision Fusion Framework for Open Water Surface Object Detection
---

# physfusion: A Transformer-based Dual-Stream Radar and Vision Fusion Framework for Open Water Surface Object Detection
**arXiv**：[2603.01947v1](https://arxiv.org/abs/2603.01947) · [PDF](https://arxiv.org/pdf/2603.01947.pdf)  
**作者**：Yuting Wan, Liguo Sun, Jiuwu Hao, Zao Zhang, Pin LV  

**一句话要点**：提出PhysFusion，一种基于Transformer的雷达与视觉双流融合框架，用于开放水面目标检测。

**关键词**：水面目标检测, 雷达视觉融合, Transformer模型, 物理信息编码, 时序聚合, 开放水域感知

## 3 点简述
- 核心问题：水面目标检测受波浪杂波、镜面反射和远距离弱外观线索挑战，雷达点云稀疏且反射率变化大。
- 方法要点：集成物理信息雷达编码器、雷达引导交互融合模块和时序查询聚合模块，实现稳健特征学习和时空一致性。
- 实验效果：在WaterScenes和FLOW数据集上达到高mAP，参数和计算量较低，消融研究验证各组件贡献。

## 摘要（原文）

> Detecting water-surface targets for Unmanned Surface Vehicles (USVs) is challenging due to wave clutter,
>   specular reflections, and weak appearance cues in long-range observations. Although 4D millimeter-wave
>   radar complements cameras under degraded illumination, maritime radar point clouds are sparse and
>   intermittent, with reflectivity attributes exhibiting heavy-tailed variations under scattering and
>   multipath, making conventional fusion designs struggle to exploit radar cues effectively.
>   We propose PhysFusion, a physics-informed radar-image detection framework for water-surface perception.
>   The framework integrates: (1) a Physics-Informed Radar Encoder (PIR Encoder) with an RCS Mapper and
>   Quality Gate, transforming per-point radar attributes into compact scattering priors and predicting
>   point-wise reliability for robust feature learning under clutter; (2) a Radar-guided Interactive Fusion
>   Module (RIFM) performing query-level radar-image fusion between semantically enriched radar features and
>   multi-scale visual features, with the radar branch modeled by a dual-stream backbone including a
>   point-based local stream and a transformer-based global stream using Scattering-Aware Self-Attention
>   (SASA); and (3) a Temporal Query Aggregation module (TQA) aggregating frame-wise fused queries over a
>   short temporal window for temporally consistent representations.
>   Experiments on WaterScenes and FLOW demonstrate that PhysFusion achieves 59.7% mAP50:95 and 90.3% mAP50
>   on WaterScenes (T=5 radar history) using 5.6M parameters and 12.5G FLOPs, and reaches 94.8% mAP50 and
>   46.2% mAP50:95 on FLOW under radar+camera setting. Ablation studies quantify the contributions of PIR
>   Encoder, SASA-based global reasoning, and RIFM.

