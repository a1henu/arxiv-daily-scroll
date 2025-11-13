---
layout: default
title: PIFF: A Physics-Informed Generative Flow Model for Real-Time Flood Depth Mapping
---

# PIFF: A Physics-Informed Generative Flow Model for Real-Time Flood Depth Mapping
**arXiv**：[2511.09130v1](https://arxiv.org/abs/2511.09130) · [PDF](https://arxiv.org/pdf/2511.09130.pdf)  
**作者**：ChunLiang Wu, Tsunhua Yang, Hungying Chen  

**一句话要点**：提出PIFF物理信息生成流模型，用于实时洪水深度映射

**关键词**：洪水深度映射, 物理信息生成模型, 图像到图像生成, 变换器编码器, 实时预测

## 3 点简述
- 洪水映射效率与可靠性不足，传统方法如数值模拟和航拍受限
- 基于图像生成框架，结合简化淹没模型和变换器降雨编码器
- 在台湾台南26公里区域测试，182种降雨场景下实现准确预测

## 摘要（原文）

> Flood mapping is crucial for assessing and mitigating flood impacts, yet traditional methods like numerical modeling and aerial photography face limitations in efficiency and reliability. To address these challenges, we propose PIFF, a physics-informed, flow-based generative neural network for near real-time flood depth estimation. Built on an image-to-image generative framework, it efficiently maps Digital Elevation Models (DEM) to flood depth predictions. The model is conditioned on a simplified inundation model (SPM) that embeds hydrodynamic priors into the training process. Additionally, a transformer-based rainfall encoder captures temporal dependencies in precipitation. Integrating physics-informed constraints with data-driven learning, PIFF captures the causal relationships between rainfall, topography, SPM, and flooding, replacing costly simulations with accurate, real-time flood maps. Using a 26 km study area in Tainan, Taiwan, with 182 rainfall scenarios ranging from 24 mm to 720 mm over 24 hours, our results demonstrate that PIFF offers an effective, data-driven alternative for flood prediction and response.

