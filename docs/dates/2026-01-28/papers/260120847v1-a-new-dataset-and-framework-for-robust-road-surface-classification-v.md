---
layout: default
title: A New Dataset and Framework for Robust Road Surface Classification via Camera-IMU Fusion
---

# A New Dataset and Framework for Robust Road Surface Classification via Camera-IMU Fusion
**arXiv**：[2601.20847v1](https://arxiv.org/abs/2601.20847) · [PDF](https://arxiv.org/pdf/2601.20847.pdf)  
**作者**：Willams de Lima Costa, Thifany Ketuli Silva de Souza, Jonas Ferreira Silva, Carlos Gabriel Bezerra Pereira, Bruno Reis Vila Nova, Leonardo Silvino Brito, Rafael Raider Leoni, Juliano Silva, Valter Ferreira, Sibele Miguel Soares Neto, Samantha Uehara, Daniel Giacomo, João Marcelo Teixeira, Veronica Teichrieb, Cristiano Coelho de Araújo  

**一句话要点**：提出基于相机-IMU融合的轻量级双向交叉注意力框架与ROAD数据集，以提升道路表面分类在多变环境下的鲁棒性。

**关键词**：道路表面分类, 多模态融合, 交叉注意力, 鲁棒性数据集, 相机-IMU融合, 自适应门控

## 3 点简述
- 核心问题：现有道路表面分类方法因传感模态有限和数据集缺乏环境多样性，难以泛化到狭窄操作条件之外。
- 方法要点：通过轻量级双向交叉注意力模块融合图像和惯性测量，并使用自适应门控层调整模态贡献以应对域偏移。
- 实验或效果：在PVS基准上提升1.4个百分点，在ROAD多模态子集上提升11.6个百分点，在夜间、大雨等挑战性视觉条件下表现稳定。

## 摘要（原文）

> Road surface classification (RSC) is a key enabler for environment-aware predictive maintenance systems. However, existing RSC techniques often fail to generalize beyond narrow operational conditions due to limited sensing modalities and datasets that lack environmental diversity. This work addresses these limitations by introducing a multimodal framework that fuses images and inertial measurements using a lightweight bidirectional cross-attention module followed by an adaptive gating layer that adjusts modality contributions under domain shifts. Given the limitations of current benchmarks, especially regarding lack of variability, we introduce ROAD, a new dataset composed of three complementary subsets: (i) real-world multimodal recordings with RGB-IMU streams synchronized using a gold-standard industry datalogger, captured across diverse lighting, weather, and surface conditions; (ii) a large vision-only subset designed to assess robustness under adverse illumination and heterogeneous capture setups; and (iii) a synthetic subset generated to study out-of-distribution generalization in scenarios difficult to obtain in practice. Experiments show that our method achieves a +1.4 pp improvement over the previous state-of-the-art on the PVS benchmark and an +11.6 pp improvement on our multimodal ROAD subset, with consistently higher F1-scores on minority classes. The framework also demonstrates stable performance across challenging visual conditions, including nighttime, heavy rain, and mixed-surface transitions. These findings indicate that combining affordable camera and IMU sensors with multimodal attention mechanisms provides a scalable, robust foundation for road surface understanding, particularly relevant for regions where environmental variability and cost constraints limit the adoption of high-end sensing suites.

