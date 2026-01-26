---
layout: default
title: A Unified Calibration Framework for High-Accuracy Articulated Robot Kinematics
---

# A Unified Calibration Framework for High-Accuracy Articulated Robot Kinematics
**arXiv**：[2601.16638v1](https://arxiv.org/abs/2601.16638) · [PDF](https://arxiv.org/pdf/2601.16638.pdf)  
**作者**：Philip Tobuschat, Simon Duenser, Markus Bambach, Ivo Aschwanden  

**一句话要点**：提出统一校准框架，通过单次实验识别几何与非几何误差，提升工业机器人定位精度。

**关键词**：工业机器人校准, 静态校准, 误差建模, 高斯-牛顿优化, 定位精度

## 3 点简述
- 核心问题：工业机器人工具定位误差来源多样，现有补偿策略需独立实验和模型，效率低。
- 方法要点：统一校准框架，用虚拟关节建模几何与非几何效应，基于高斯-牛顿优化和解析梯度进行识别。
- 实验或效果：在KUKA KR30机器人上，平均位置误差降至26.8 μm，相比纯几何校准的102.3 μm显著提升。

## 摘要（原文）

> Researchers have identified various sources of tool positioning errors for articulated industrial robots and have proposed dedicated compensation strategies. However, these typically require individual, specialized experiments with separate models and identification procedures. This article presents a unified approach to the static calibration of industrial robots that identifies a robot model, including geometric and non-geometric effects (compliant bending, thermal deformation, gear transmission errors), using only a single, straightforward experiment for data collection. The model augments the kinematic chain with virtual joints for each modeled effect and realizes the identification using Gauss-Newton optimization with analytic gradients. Fisher information spectra show that the estimation is well-conditioned and the parameterization near-minimal, whereas systematic temporal cross-validation and model ablations demonstrate robustness of the model identification. The resulting model is very accurate and its identification robust, achieving a mean position error of 26.8 $μm$ on a KUKA KR30 industrial robot compared to 102.3 $μm$ for purely geometric calibration.

