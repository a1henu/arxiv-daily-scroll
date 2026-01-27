---
layout: default
title: Cognitive Fusion of ZC Sequences and Time-Frequency Images for Out-of-Distribution Detection of Drone Signals
---

# Cognitive Fusion of ZC Sequences and Time-Frequency Images for Out-of-Distribution Detection of Drone Signals
**arXiv**：[2601.18326v1](https://arxiv.org/abs/2601.18326) · [PDF](https://arxiv.org/pdf/2601.18326.pdf)  
**作者**：Jie Li, Jing Li, Lu Lv, Zhanyu Ju, Fengkui Gong  

**一句话要点**：提出基于ZC序列与时频图像认知融合的无人机信号分布外检测算法，用于无人机远程识别任务。

**关键词**：无人机信号检测, 分布外检测, 多模态融合, 时频分析, ZC序列, 远程识别

## 3 点简述
- 核心问题：无人机信号分布外检测，需处理已知协议（如DJI）与未知/非标准协议信号。
- 方法要点：融合ZC序列特征与时频图像特征，通过多模态交互与融合增强信息互补，生成自适应注意力权重进行分类。
- 实验或效果：仿真显示算法优于现有方法，在远程识别与分布外检测指标上分别提升1.7%和7.5%，且在不同飞行条件与无人机类型下鲁棒性强。

## 摘要（原文）

> We propose a drone signal out-of-distribution detection (OODD) algorithm based on the cognitive fusion of Zadoff-Chu (ZC) sequences and time-frequency images (TFI). ZC sequences are identified by analyzing the communication protocols of DJI drones, while TFI capture the time-frequency characteristics of drone signals with unknown or non-standard communication protocols. Both modalities are used jointly to enable OODD in the drone remote identification (RID) task. Specifically, ZC sequence features and TFI features are generated from the received radio frequency signals, which are then processed through dedicated feature extraction module to enhance and align them. The resultant multi-modal features undergo multi-modal feature interaction, single-modal feature fusion, and multi-modal feature fusion to produce features that integrate and complement information across modalities. Discrimination scores are computed from the fused features along both spatial and channel dimensions to capture time-frequency characteristic differences dictated by the communication protocols, and these scores will be transformed into adaptive attention weights. The weighted features are then passed through a Softmax function to produce the signal classification results. Simulation results demonstrate that the proposed algorithm outperforms existing algorithms and achieves 1.7% and 7.5% improvements in RID and OODD metrics, respectively. The proposed algorithm also performs strong robustness under varying flight conditions and across different drone types.

