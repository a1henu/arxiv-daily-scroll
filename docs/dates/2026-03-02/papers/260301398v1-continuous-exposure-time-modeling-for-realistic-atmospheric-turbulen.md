---
layout: default
title: Continuous Exposure-Time Modeling for Realistic Atmospheric Turbulence Synthesis
---

# Continuous Exposure-Time Modeling for Realistic Atmospheric Turbulence Synthesis
**arXiv**：[2603.01398v1](https://arxiv.org/abs/2603.01398) · [PDF](https://arxiv.org/pdf/2603.01398.pdf)  
**作者**：Junwei Zeng, Dong Liang, Sheng-Jun Huang, Kun Zhan, Songcan Chen  

**一句话要点**：提出连续曝光时间建模方法以合成更真实的大气湍流效应

**关键词**：大气湍流合成, 连续曝光时间建模, 调制传递函数, 点扩散函数, 合成数据集, 图像恢复

## 3 点简述
- 现有方法简化曝光时间与模糊关系，导致合成数据不真实
- 提出ET-MTF，将模糊建模为曝光时间的连续函数
- 构建ET-Turb数据集，实验显示训练模型在真实数据上泛化更优

## 摘要（原文）

> Atmospheric turbulence significantly degrades long-range imaging by introducing geometric warping and exposure-time-dependent blur, which adversely affects both visual quality and the performance of high-level vision tasks. Existing methods for synthesizing turbulence effects often oversimplify the relationship between blur and exposure-time, typically assuming fixed or binary exposure settings. This leads to unrealistic synthetic data and limited generalization capability of trained models. To address this gap, we revisit the modulation transfer function (MTF) formulation and propose a novel Exposure-Time-dependent MTF (ET-MTF) that models blur as a continuous function of exposure-time. For blur synthesis, we derive a tilt-invariant point spread function (PSF) from the ET-MTF, which, when integrated with a spatially varying blur-width field, provides a comprehensive and physically accurate characterization of turbulence-induced blur. Building on this synthesis pipeline, we construct ET-Turb, a large-scale synthetic turbulence dataset that explicitly incorporates continuous exposure-time modeling across diverse optical and atmospheric conditions. The dataset comprises 5,083 videos (2,005,835 frames), partitioned into 3,988 training and 1,095 test videos. Extensive experiments demonstrate that models trained on ET-Turb produce more realistic restorations and achieve superior generalization on real-world turbulence data compared to those trained on other datasets. The dataset is publicly available at: github.com/Jun-Wei-Zeng/ET-Turb.

