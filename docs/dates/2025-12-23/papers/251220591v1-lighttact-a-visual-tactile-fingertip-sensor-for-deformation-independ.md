---
layout: default
title: LightTact: A Visual-Tactile Fingertip Sensor for Deformation-Independent Contact Sensing
---

# LightTact: A Visual-Tactile Fingertip Sensor for Deformation-Independent Contact Sensing
**arXiv**：[2512.20591v1](https://arxiv.org/abs/2512.20591) · [PDF](https://arxiv.org/pdf/2512.20591.pdf)  
**作者**：Changyi Lin, Boda Huo, Mingyang Yu, Emily Ruppel, Bingqing Chen, Jonathan Francis, Ding Zhao  

**一句话要点**：提出LightTact视觉触觉指尖传感器，以光学原理实现变形无关的接触感知，解决轻接触场景难题。

**关键词**：视觉触觉传感器, 变形无关接触感知, 光学配置, 机器人操控, 像素级分割, 视觉语言模型

## 3 点简述
- 核心问题：现有触觉传感器依赖变形感知接触，难以稳健检测液体、半液体或超软材料等轻接触。
- 方法要点：采用环境光阻挡光学配置，抑制非接触区域光，仅传输真实接触产生的漫射光，实现高对比度原始图像。
- 实验或效果：在机器人手臂上集成，演示水扩散、面霜蘸取等轻接触操控，并支持视觉语言模型直接解释图像。

## 摘要（原文）

> Contact often occurs without macroscopic surface deformation, such as during interaction with liquids, semi-liquids, or ultra-soft materials. Most existing tactile sensors rely on deformation to infer contact, making such light-contact interactions difficult to perceive robustly. To address this, we present LightTact, a visual-tactile fingertip sensor that makes contact directly visible via a deformation-independent, optics-based principle. LightTact uses an ambient-blocking optical configuration that suppresses both external light and internal illumination at non-contact regions, while transmitting only the diffuse light generated at true contacts. As a result, LightTact produces high-contrast raw images in which non-contact pixels remain near-black (mean gray value < 3) and contact pixels preserve the natural appearance of the contacting surface. Built on this, LightTact achieves accurate pixel-level contact segmentation that is robust to material properties, contact force, surface appearance, and environmental lighting. We further integrate LightTact on a robotic arm and demonstrate manipulation behaviors driven by extremely light contact, including water spreading, facial-cream dipping, and thin-film interaction. Finally, we show that LightTact's spatially aligned visual-tactile images can be directly interpreted by existing vision-language models, enabling resistor value reasoning for robotic sorting.

