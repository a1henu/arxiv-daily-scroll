---
layout: default
title: UltrasODM: A Dual Stream Optical Flow Mamba Network for 3D Freehand Ultrasound Reconstruction
---

# UltrasODM: A Dual Stream Optical Flow Mamba Network for 3D Freehand Ultrasound Reconstruction
**arXiv**：[2512.07756v1](https://arxiv.org/abs/2512.07756) · [PDF](https://arxiv.org/pdf/2512.07756.pdf)  
**作者**：Mayank Anand, Ujair Alam, Surya Prakash, Priya Shukla, Gora Chand Nandi, Domenec Puig  

**一句话要点**：提出UltrasODM双流框架，通过不确定性估计和提示辅助解决自由手超声重建中的漂移和误差问题。

**关键词**：自由手超声重建, 光流估计, Mamba网络, 不确定性量化, 人机交互, 三维医学成像

## 3 点简述
- 核心问题：临床超声采集依赖操作者，快速探头运动和亮度波动导致重建误差，降低临床信任度。
- 方法要点：集成对比排序模块、光流流与Dual-Mamba时序模块，结合贝叶斯不确定性和人机交互层提供实时提示。
- 实验或效果：在临床数据集上相比UltrasOM减少漂移15.2%、距离误差12.1%，并输出逐帧不确定性和显著性图。

## 摘要（原文）

> Clinical ultrasound acquisition is highly operator-dependent, where rapid probe motion and brightness fluctuations often lead to reconstruction errors that reduce trust and clinical utility. We present UltrasODM, a dual-stream framework that assists sonographers during acquisition through calibrated per-frame uncertainty, saliency-based diagnostics, and actionable prompts. UltrasODM integrates (i) a contrastive ranking module that groups frames by motion similarity, (ii) an optical-flow stream fused with Dual-Mamba temporal modules for robust 6-DoF pose estimation, and (iii) a Human-in-the-Loop (HITL) layer combining Bayesian uncertainty, clinician-calibrated thresholds, and saliency maps highlighting regions of low confidence. When uncertainty exceeds the threshold, the system issues unobtrusive alerts suggesting corrective actions such as re-scanning highlighted regions or slowing the sweep. Evaluated on a clinical freehand ultrasound dataset, UltrasODM reduces drift by 15.2%, distance error by 12.1%, and Hausdorff distance by 10.1% relative to UltrasOM, while producing per-frame uncertainty and saliency outputs. By emphasizing transparency and clinician feedback, UltrasODM improves reconstruction reliability and supports safer, more trustworthy clinical workflows. Our code is publicly available at https://github.com/AnandMayank/UltrasODM.

