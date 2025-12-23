---
layout: default
title: From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs
---

# From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs
**arXiv**：[2512.19683v1](https://arxiv.org/abs/2512.19683) · [PDF](https://arxiv.org/pdf/2512.19683.pdf)  
**作者**：Mingrui Wu, Zhaozhi Wang, Fangjinhua Wang, Jiaolong Yang, Marc Pollefeys, Tong Zhang  

**一句话要点**：提出基于多传感器户外数据集的大规模基准，以揭示MLLMs在开放世界中的空间推理缺陷。

**关键词**：多模态大语言模型, 空间推理, 户外基准, 3D信息, 视觉语言理解, 传感器融合

## 3 点简述
- 核心问题：MLLMs的空间智能不足，现有基准局限于室内或简化任务，缺乏户外验证数据。
- 方法要点：利用同步立体相机、LiDAR和IMU/GPS传感器采集行人视角视频，构建提供精确3D信息的基准。
- 实验或效果：评估显示MLLMs在开放世界性能下降，依赖语言先验而非视觉推理，基准可用于诊断和推进空间智能。

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have achieved impressive performance on semantic tasks, their spatial intelligence--crucial for robust and grounded AI systems--remains underdeveloped. Existing benchmarks fall short of diagnosing this limitation: they either focus on overly simplified qualitative reasoning or rely on domain-specific indoor data, constrained by the lack of outdoor datasets with verifiable metric ground truth. To bridge this gap, we introduce a large-scale benchmark built from pedestrian-perspective videos captured with synchronized stereo cameras, LiDAR, and IMU/GPS sensors. This dataset provides metrically precise 3D information, enabling the automatic generation of spatial reasoning questions that span a hierarchical spectrum--from qualitative relational reasoning to quantitative metric and kinematic understanding. Evaluations reveal that the performance gains observed in structured indoor benchmarks vanish in open-world settings. Further analysis using synthetic abnormal scenes and blinding tests confirms that current MLLMs depend heavily on linguistic priors instead of grounded visual reasoning. Our benchmark thus provides a principled platform for diagnosing these limitations and advancing physically grounded spatial intelligence.

