---
layout: default
title: Assessing Building Heat Resilience Using UAV and Street-View Imagery with Coupled Global Context Vision Transformer
---

# Assessing Building Heat Resilience Using UAV and Street-View Imagery with Coupled Global Context Vision Transformer
**arXiv**：[2601.11357v1](https://arxiv.org/abs/2601.11357) · [PDF](https://arxiv.org/pdf/2601.11357.pdf)  
**作者**：Steffen Knoblauch, Ram Kumar Muthusamy, Hao Li, Iddy Chazua, Benedcto Adamu, Innocent Maholi, Alexander Zipf  

**一句话要点**：提出耦合全局上下文视觉变换器融合无人机与街景图像，以评估建筑热韧性。

**关键词**：建筑热韧性评估, 无人机与街景图像融合, 耦合全局上下文视觉变换器, 热红外测量, 双模态学习, 城市气候适应

## 3 点简述
- 核心问题：气候变化加剧城市热暴露，缺乏可扩展的建筑属性评估方法。
- 方法要点：使用CGCViT融合无人机和街景图像，学习热相关建筑表示。
- 实验或效果：双模态方法优于单模态达9.3%，识别植被、屋顶材质与热风险关联。

## 摘要（原文）

> Climate change is intensifying human heat exposure, particularly in densely built urban centers of the Global South. Low-cost construction materials and high thermal-mass surfaces further exacerbate this risk. Yet scalable methods for assessing such heat-relevant building attributes remain scarce. We propose a machine learning framework that fuses openly available unmanned aerial vehicle (UAV) and street-view (SV) imagery via a coupled global context vision transformer (CGCViT) to learn heat-relevant representations of urban structures. Thermal infrared (TIR) measurements from HotSat-1 are used to quantify the relationship between building attributes and heat-associated health risks. Our dual-modality cross-view learning approach outperforms the best single-modality models by up to $9.3\%$, demonstrating that UAV and SV imagery provide valuable complementary perspectives on urban structures. The presence of vegetation surrounding buildings (versus no vegetation), brighter roofing (versus darker roofing), and roofing made of concrete, clay, or wood (versus metal or tarpaulin) are all significantly associated with lower HotSat-1 TIR values. Deployed across the city of Dar es Salaam, Tanzania, the proposed framework illustrates how household-level inequalities in heat exposure - often linked to socio-economic disadvantage and reflected in building materials - can be identified and addressed using machine learning. Our results point to the critical role of localized, data-driven risk assessment in shaping climate adaptation strategies that deliver equitable outcomes.

