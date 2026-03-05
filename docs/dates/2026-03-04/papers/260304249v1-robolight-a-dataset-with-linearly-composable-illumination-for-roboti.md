---
layout: default
title: RoboLight: A Dataset with Linearly Composable Illumination for Robotic Manipulation
---

# RoboLight: A Dataset with Linearly Composable Illumination for Robotic Manipulation
**arXiv**：[2603.04249v1](https://arxiv.org/abs/2603.04249) · [PDF](https://arxiv.org/pdf/2603.04249.pdf)  
**作者**：Shutong Jin, Jin Yang, Muhammad Zahid, Florian T. Pokorny  

**一句话要点**：提出RoboLight数据集，通过线性可组合光照支持机器人操作研究

**关键词**：机器人操作数据集, 光照变化, 高动态范围图像, 数据合成, 视觉感知, 开源数据集

## 3 点简述
- 核心问题：缺乏真实世界机器人操作中系统光照变化的数据集，影响视觉感知鲁棒性。
- 方法要点：构建RoboLight-Real真实数据集和RoboLight-Synthetic合成数据集，利用HDR图像空间插值扩展数据。
- 实验或效果：通过定性分析和真实策略部署验证数据集质量，展示三个代表性用例。

## 摘要（原文）

> In this paper, we introduce RoboLight, the first real-world robotic manipulation dataset capturing synchronized episodes under systematically varied lighting conditions. RoboLight consists of two components. (a) RoboLight-Real contains 2,800 real-world episodes collected in our custom Light Cube setup, a calibrated system equipped with eight programmable RGB LED lights. It includes structured illumination variation along three independently controlled dimensions: color, direction, and intensity. Each dimension is paired with a dedicated task featuring objects of diverse geometries and materials to induce perceptual challenges. All image data are recorded in high-dynamic-range (HDR) format to preserve radiometric accuracy. Leveraging the linearity of light transport, we introduce (b) RoboLight-Synthetic, comprising 196,000 episodes synthesized through interpolation in the HDR image space of RoboLight-Real. In principle, RoboLight-Synthetic can be arbitrarily expanded by refining the interpolation granularity. We further verify the dataset quality through qualitative analysis and real-world policy roll-outs, analyzing task difficulty, distributional diversity, and the effectiveness of synthesized data. We additionally demonstrate three representative use cases of the proposed dataset. The full dataset, along with the system software and hardware design, will be released as open-source to support continued research.

