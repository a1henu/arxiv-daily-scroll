---
layout: default
title: Expert Switching for Robust AAV Landing: A Dual-Detector Framework in Simulation
---

# Expert Switching for Robust AAV Landing: A Dual-Detector Framework in Simulation
**arXiv**：[2512.14054v1](https://arxiv.org/abs/2512.14054) · [PDF](https://arxiv.org/pdf/2512.14054.pdf)  
**作者**：Humaira Tasnim, Ashik E Rasul, Bruce Jo, Hyung-Jin Yoon  

**一句话要点**：提出基于双检测器的尺度自适应框架，以提升自主飞行器在降落过程中的停机坪检测鲁棒性。

**关键词**：自主飞行器降落, 尺度自适应检测, 双检测器框架, 几何门控机制, 闭环仿真评估

## 3 点简述
- 核心问题：单检测器在自主飞行器降落时难以应对停机坪尺度剧烈变化，导致检测性能下降。
- 方法要点：训练两个YOLOv8专家分别处理远距离和近距离停机坪检测，通过几何门控机制自适应选择专家。
- 实验或效果：在集成CARLA和NASA GUAM的闭环环境中验证，相比单检测器基线，显著提升了对齐稳定性、降落精度和整体鲁棒性。

## 摘要（原文）

> Reliable helipad detection is essential for Autonomous Aerial Vehicle (AAV) landing, especially under GPS-denied or visually degraded conditions. While modern detectors such as YOLOv8 offer strong baseline performance, single-model pipelines struggle to remain robust across the extreme scale transitions that occur during descent, where helipads appear small at high altitude and large near touchdown. To address this limitation, we propose a scale-adaptive dual-expert perception framework that decomposes the detection task into far-range and close-range regimes. Two YOLOv8 experts are trained on scale-specialized versions of the HelipadCat dataset, enabling one model to excel at detecting small, low-resolution helipads and the other to provide high-precision localization when the target dominates the field of view. During inference, both experts operate in parallel, and a geometric gating mechanism selects the expert whose prediction is most consistent with the AAV's viewpoint. This adaptive routing prevents the degradation commonly observed in single-detector systems when operating across wide altitude ranges. The dual-expert perception module is evaluated in a closed-loop landing environment that integrates CARLA's photorealistic rendering with NASA's GUAM flight-dynamics engine. Results show substantial improvements in alignment stability, landing accuracy, and overall robustness compared to single-detector baselines. By introducing a scale-aware expert routing strategy tailored to the landing problem, this work advances resilient vision-based perception for autonomous descent and provides a foundation for future multi-expert AAV frameworks.

