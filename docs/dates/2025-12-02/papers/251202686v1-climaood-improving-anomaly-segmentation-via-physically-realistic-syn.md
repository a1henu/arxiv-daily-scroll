---
layout: default
title: ClimaOoD: Improving Anomaly Segmentation via Physically Realistic Synthetic Data
---

# ClimaOoD: Improving Anomaly Segmentation via Physically Realistic Synthetic Data
**arXiv**：[2512.02686v1](https://arxiv.org/abs/2512.02686) · [PDF](https://arxiv.org/pdf/2512.02686.pdf)  
**作者**：Yuxing Liu, Yong Liu  

**一句话要点**：提出ClimaOoD基准，通过物理真实合成数据提升自动驾驶异常分割性能

**关键词**：异常分割, 合成数据生成, 自动驾驶, 物理真实, 多天气场景, 开放世界检测

## 3 点简述
- 异常分割面临数据稀缺和多样性不足问题，限制模型在开放世界中的泛化能力
- ClimaDrive框架结合结构引导多天气生成和提示驱动异常修复，合成语义连贯且物理真实的驾驶数据
- 实验显示，使用ClimaOoD训练能显著提升AUROC、AP等指标，增强模型鲁棒性

## 摘要（原文）

> Anomaly segmentation seeks to detect and localize unknown or out-of-distribution (OoD) objects that fall outside predefined semantic classes a capability essential for safe autonomous driving. However, the scarcity and limited diversity of anomaly data severely constrain model generalization in open-world environments. Existing approaches mitigate this issue through synthetic data generation, either by copy-pasting external objects into driving scenes or by leveraging text-to-image diffusion models to inpaint anomalous regions. While these methods improve anomaly diversity, they often lack contextual coherence and physical realism, resulting in domain gaps between synthetic and real data. In this paper, we present ClimaDrive, a semantics-guided image-to-image framework for synthesizing semantically coherent, weather-diverse, and physically plausible OoD driving data. ClimaDrive unifies structure-guided multi-weather generation with prompt-driven anomaly inpainting, enabling the creation of visually realistic training data. Based on this framework, we construct ClimaOoD, a large-scale benchmark spanning six representative driving scenarios under both clear and adverse weather conditions. Extensive experiments on four state-of-the-art methods show that training with ClimaOoD leads to robust improvements in anomaly segmentation. Across all methods, AUROC, AP, and FPR95 show notable gains, with FPR95 dropping from 3.97 to 3.52 for RbA on Fishyscapes LAF. These results demonstrate that ClimaOoD enhances model robustness, offering valuable training data for better generalization in open-world anomaly detection.

