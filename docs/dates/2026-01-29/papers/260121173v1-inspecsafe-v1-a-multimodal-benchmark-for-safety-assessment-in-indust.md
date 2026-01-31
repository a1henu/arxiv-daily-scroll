---
layout: default
title: InspecSafe-V1: A Multimodal Benchmark for Safety Assessment in Industrial Inspection Scenarios
---

# InspecSafe-V1: A Multimodal Benchmark for Safety Assessment in Industrial Inspection Scenarios
**arXiv**：[2601.21173v1](https://arxiv.org/abs/2601.21173) · [PDF](https://arxiv.org/pdf/2601.21173.pdf)  
**作者**：Zeyi Liu, Shuang Liu, Jihai Min, Zhaoheng Zhang, Jun Cen, Pengyu Han, Songqiao Hu, Zihan Meng, Xiao He, Donghua Zhou  

**一句话要点**：提出InspecSafe-V1多模态基准数据集以解决工业巡检场景中AI系统安全评估的瓶颈问题

**关键词**：工业巡检安全评估, 多模态基准数据集, 像素级分割标注, 跨模态融合, 真实环境数据收集, 同步感知模态

## 3 点简述
- 核心问题：现有数据集因模拟数据、单模态感知或缺乏细粒度标注，限制了工业基础模型的鲁棒场景理解和多模态安全推理。
- 方法要点：从真实巡检机器人操作中收集数据，覆盖五种工业场景，提供像素级分割标注、语义场景描述和安全等级标签。
- 实验或效果：包含七种同步感知模态，支持多模态异常识别、跨模态融合和综合安全评估，基于2,239个有效巡检站点构建。

## 摘要（原文）

> With the rapid development of industrial intelligence and unmanned inspection, reliable perception and safety assessment for AI systems in complex and dynamic industrial sites has become a key bottleneck for deploying predictive maintenance and autonomous inspection. Most public datasets remain limited by simulated data sources, single-modality sensing, or the absence of fine-grained object-level annotations, which prevents robust scene understanding and multimodal safety reasoning for industrial foundation models. To address these limitations, InspecSafe-V1 is released as the first multimodal benchmark dataset for industrial inspection safety assessment that is collected from routine operations of real inspection robots in real-world environments. InspecSafe-V1 covers five representative industrial scenarios, including tunnels, power facilities, sintering equipment, oil and gas petrochemical plants, and coal conveyor trestles. The dataset is constructed from 41 wheeled and rail-mounted inspection robots operating at 2,239 valid inspection sites, yielding 5,013 inspection instances. For each instance, pixel-level segmentation annotations are provided for key objects in visible-spectrum images. In addition, a semantic scene description and a corresponding safety level label are provided according to practical inspection tasks. Seven synchronized sensing modalities are further included, including infrared video, audio, depth point clouds, radar point clouds, gas measurements, temperature, and humidity, to support multimodal anomaly recognition, cross-modal fusion, and comprehensive safety assessment in industrial environments.

