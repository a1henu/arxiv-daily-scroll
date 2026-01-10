---
layout: default
title: HATIR: Heat-Aware Diffusion for Turbulent Infrared Video Super-Resolution
---

# HATIR: Heat-Aware Diffusion for Turbulent Infrared Video Super-Resolution
**arXiv**：[2601.04682v1](https://arxiv.org/abs/2601.04682) · [PDF](https://arxiv.org/pdf/2601.04682.pdf)  
**作者**：Yang Zou, Xingyue Zhu, Kaiqi Han, Jun Ma, Xingyuan Li, Zhiying Jiang, Jinyuan Liu  

**一句话要点**：提出HATIR方法，通过热感知扩散联合建模湍流退化与细节损失，解决红外视频超分辨率问题。

**关键词**：红外视频超分辨率, 湍流缓解, 扩散模型, 热感知先验, 相量引导流估计, 湍流感知解码

## 3 点简述
- 核心问题：红外视频受大气湍流和压缩退化影响，现有方法忽略模态差异或无法恢复湍流失真。
- 方法要点：注入热感知变形先验，使用相量引导流估计器和湍流感知解码器，联合逆建模退化过程。
- 实验或效果：构建FLIR-IVSR数据集，包含640个场景的LR-HR序列，促进红外视频超分辨率研究。

## 摘要（原文）

> Infrared video has been of great interest in visual tasks under challenging environments, but often suffers from severe atmospheric turbulence and compression degradation. Existing video super-resolution (VSR) methods either neglect the inherent modality gap between infrared and visible images or fail to restore turbulence-induced distortions. Directly cascading turbulence mitigation (TM) algorithms with VSR methods leads to error propagation and accumulation due to the decoupled modeling of degradation between turbulence and resolution. We introduce HATIR, a Heat-Aware Diffusion for Turbulent InfraRed Video Super-Resolution, which injects heat-aware deformation priors into the diffusion sampling path to jointly model the inverse process of turbulent degradation and structural detail loss. Specifically, HATIR constructs a Phasor-Guided Flow Estimator, rooted in the physical principle that thermally active regions exhibit consistent phasor responses over time, enabling reliable turbulence-aware flow to guide the reverse diffusion process. To ensure the fidelity of structural recovery under nonuniform distortions, a Turbulence-Aware Decoder is proposed to selectively suppress unstable temporal cues and enhance edge-aware feature aggregation via turbulence gating and structure-aware attention. We built FLIR-IVSR, the first dataset for turbulent infrared VSR, comprising paired LR-HR sequences from a FLIR T1050sc camera (1024 X 768) spanning 640 diverse scenes with varying camera and object motion conditions. This encourages future research in infrared VSR. Project page: https://github.com/JZ0606/HATIR

