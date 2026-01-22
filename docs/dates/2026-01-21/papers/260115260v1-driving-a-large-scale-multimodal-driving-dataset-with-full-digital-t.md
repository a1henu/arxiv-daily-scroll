---
layout: default
title: DrivIng: A Large-Scale Multimodal Driving Dataset with Full Digital Twin Integration
---

# DrivIng: A Large-Scale Multimodal Driving Dataset with Full Digital Twin Integration
**arXiv**：[2601.15260v1](https://arxiv.org/abs/2601.15260) · [PDF](https://arxiv.org/pdf/2601.15260.pdf)  
**作者**：Dominik Rößle, Xujun Xie, Adithya Mohan, Venkatesh Thirugnana Sambandham, Daniel Cremers, Torsten Schön  

**一句话要点**：提出DrivIng数据集，集成高保真数字孪生以支持自动驾驶感知算法的系统测试与仿真评估。

**关键词**：自动驾驶数据集, 数字孪生, 多模态感知, 3D目标检测, 仿真评估, 高精度地图

## 3 点简述
- 现有数据集缺乏高保真数字孪生，限制系统测试、边缘案例仿真和传感器修改。
- DrivIng提供约18公里多路段连续多模态数据，包括RGB相机、LiDAR和精确定位，并标注3D边界框。
- 数据集支持真实交通到仿真的1对1转移，基准测试显示其支持可重复研究和鲁棒验证。

## 摘要（原文）

> Perception is a cornerstone of autonomous driving, enabling vehicles to understand their surroundings and make safe, reliable decisions. Developing robust perception algorithms requires large-scale, high-quality datasets that cover diverse driving conditions and support thorough evaluation. Existing datasets often lack a high-fidelity digital twin, limiting systematic testing, edge-case simulation, sensor modification, and sim-to-real evaluations. To address this gap, we present DrivIng, a large-scale multimodal dataset with a complete geo-referenced digital twin of a ~18 km route spanning urban, suburban, and highway segments. Our dataset provides continuous recordings from six RGB cameras, one LiDAR, and high-precision ADMA-based localization, captured across day, dusk, and night. All sequences are annotated at 10 Hz with 3D bounding boxes and track IDs across 12 classes, yielding ~1.2 million annotated instances. Alongside the benefits of a digital twin, DrivIng enables a 1-to-1 transfer of real traffic into simulation, preserving agent interactions while enabling realistic and flexible scenario testing. To support reproducible research and robust validation, we benchmark DrivIng with state-of-the-art perception models and publicly release the dataset, digital twin, HD map, and codebase.

