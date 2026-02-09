---
layout: default
title: A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics
---

# A Cycle-Consistent Graph Surrogate for Full-Cycle Left Ventricular Myocardial Biomechanics
**arXiv**：[2602.06884v1](https://arxiv.org/abs/2602.06884) · [PDF](https://arxiv.org/pdf/2602.06884.pdf)  
**作者**：Siyu Mu, Wei Xuan Chan, Choon Hwai Yap  

**一句话要点**：提出CardioGraphFENet以快速估计左心室全周期心肌生物力学，减少有限元分析计算负担。

**关键词**：心肌生物力学, 图神经网络, 循环一致性, 有限元分析, 左心室模拟

## 3 点简述
- 问题：基于图像的左心室力学模拟计算量大，现有图代理方法缺乏全周期预测能力。
- 方法：集成全局-局部图编码器、门控循环单元时间编码器和循环一致性双向框架。
- 效果：模型在有限元监督下实现高保真度，生成生理合理的压力-容积环，减少监督需求。

## 摘要（原文）

> Image-based patient-specific simulation of left ventricular (LV) mechanics is valuable for understanding cardiac function and supporting clinical intervention planning, but conventional finite-element analysis (FEA) is computationally intensive. Current graph-based surrogates do not have full-cycle prediction capabilities, and physics-informed neural networks often struggle to converge on complex cardiac geometries. We present CardioGraphFENet (CGFENet), a unified graph-based surrogate for rapid full-cycle estimation of LV myocardial biomechanics, supervised by a large FEA simulation dataset. The proposed model integrates (i) a global--local graph encoder to capture mesh features with weak-form-inspired global coupling, (ii) a gated recurrent unit-based temporal encoder conditioned on the target volume-time signal to model cycle-coherent dynamics, and (iii) a cycle-consistent bidirectional formulation for both loading and inverse unloading within a single framework. These strategies enable high fidelity with respect to traditional FEA ground truths and produce physiologically plausible pressure-volume loops that match FEA results when coupled with a lumped-parameter model. In particular, the cycle-consistency strategy enables a significant reduction in FEA supervision with only minimal loss in accuracy.

