---
layout: default
title: From Real-World Traffic Data to Relevant Critical Scenarios
---

# From Real-World Traffic Data to Relevant Critical Scenarios
**arXiv**：[2512.07482v1](https://arxiv.org/abs/2512.07482) · [PDF](https://arxiv.org/pdf/2512.07482.pdf)  
**作者**：Florian Lüttner, Nicole Neis, Daniel Stadler, Robin Moss, Mirjam Fehling-Kaschek, Matthias Pfriem, Alexander Stolz, Jens Ziehn  

**一句话要点**：提出基于真实高速公路数据的车道变换场景分析与合成方法，以识别和生成安全相关场景。

**关键词**：自动驾驶验证, 车道变换场景, 真实交通数据, 关键性度量, 合成场景生成, 高速公路安全

## 3 点简述
- 核心问题：自动驾驶系统验证需覆盖广泛相关场景，但自由度多且未知不安全场景增加，导致识别挑战。
- 方法要点：从真实高速公路交通数据采集处理轨迹，应用关键性度量评估车道变换场景，并基于记录生成合成场景。
- 实验或效果：在AVEAS项目中实现处理链，支持安全相关场景识别、数据驱动方法开发及合成关键场景生成。

## 摘要（原文）

> The reliable operation of autonomous vehicles, automated driving functions, and advanced driver assistance systems across a wide range of relevant scenarios is critical for their development and deployment. Identifying a near-complete set of relevant driving scenarios for such functionalities is challenging due to numerous degrees of freedom involved, each affecting the outcomes of the driving scenario differently. Moreover, with increasing technical complexity of new functionalities, the number of potentially relevant, particularly "unknown unsafe" scenarios is increasing. To enhance validation efficiency, it is essential to identify relevant scenarios in advance, starting with simpler domains like highways before moving to more complex environments such as urban traffic. To address this, this paper focuses on analyzing lane change scenarios in highway traffic, which involve multiple degrees of freedom and present numerous safetyrelevant scenarios. We describe the process of data acquisition and processing of real-world data from public highway traffic, followed by the application of criticality measures on trajectory data to evaluate scenarios, as conducted within the AVEAS project (www.aveas.org). By linking the calculated measures to specific lane change driving scenarios and the conditions under which the data was collected, we facilitate the identification of safetyrelevant driving scenarios for various applications. Further, to tackle the extensive range of "unknown unsafe" scenarios, we propose a way to generate relevant scenarios by creating synthetic scenarios based on recorded ones. Consequently, we demonstrate and evaluate a processing chain that enables the identification of safety-relevant scenarios, the development of data-driven methods for extracting these scenarios, and the generation of synthetic critical scenarios via sampling on highways.

