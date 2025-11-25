---
layout: default
title: Facade Segmentation for Solar Photovoltaic Suitability
---

# Facade Segmentation for Solar Photovoltaic Suitability
**arXiv**：[2511.18882v1](https://arxiv.org/abs/2511.18882) · [PDF](https://arxiv.org/pdf/2511.18882.pdf)  
**作者**：Ayca Duran, Christoph Waibel, Bernd Bickel, Iro Armeni, Arno Schlueter  

**一句话要点**：提出建筑立面光伏适用性分割管道，以支持城市能源规划。

**关键词**：建筑立面分割, 光伏适用性评估, 语义分割, 城市能源规划, SegFormer微调

## 3 点简述
- 核心问题：建筑立面光伏潜力评估方法稀缺且过于简化，阻碍城市脱碳。
- 方法要点：基于SegFormer-B5微调，结合立面语义分割生成光伏布局。
- 实验或效果：在373个立面数据集上验证，显示可安装潜力远低于理论值。

## 摘要（原文）

> Building integrated photovoltaic (BIPV) facades represent a promising pathway towards urban decarbonization, especially where roof areas are insufficient and ground-mounted arrays are infeasible. Although machine learning-based approaches to support photovoltaic (PV) planning on rooftops are well researched, automated approaches for facades still remain scarce and oversimplified. This paper therefore presents a pipeline that integrates detailed information on the architectural composition of the facade to automatically identify suitable surfaces for PV application and estimate the solar energy potential. The pipeline fine-tunes SegFormer-B5 on the CMP Facades dataset and converts semantic predictions into facade-level PV suitability masks and PV panel layouts considering module sizes and clearances. Applied to a dataset of 373 facades with known dimensions from ten cities, the results show that installable BIPV potential is significantly lower than theoretical potential, thus providing valuable insights for reliable urban energy planning. With the growing availability of facade imagery, the proposed pipeline can be scaled to support BIPV planning in cities worldwide.

