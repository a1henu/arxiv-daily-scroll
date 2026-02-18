---
layout: default
title: Continuous-Time Piecewise-Linear Recurrent Neural Networks
---

# Continuous-Time Piecewise-Linear Recurrent Neural Networks
**arXiv**：[2602.15649v1](https://arxiv.org/abs/2602.15649) · [PDF](https://arxiv.org/pdf/2602.15649.pdf)  
**作者**：Alena Brändle, Lukas Eisenmann, Florian Götz, Daniel Durstewitz  

**一句话要点**：提出连续时间分段线性循环神经网络以解决动态系统重建中的连续时间建模问题

**关键词**：动态系统重建, 连续时间建模, 分段线性循环神经网络, 可分析性, 数值积分绕过

## 3 点简述
- 动态系统重建需从时间序列恢复底层系统，现有离散时间模型与连续物理过程不符
- 开发连续时间分段线性循环神经网络理论，利用分段线性结构绕过数值积分高效训练
- 在基准测试中比较连续时间模型与离散时间模型及神经ODE，展示性能与可分析性优势

## 摘要（原文）

> In dynamical systems reconstruction (DSR) we aim to recover the dynamical system (DS) underlying observed time series. Specifically, we aim to learn a generative surrogate model which approximates the underlying, data-generating DS, and recreates its long-term properties (`climate statistics'). In scientific and medical areas, in particular, these models need to be mechanistically tractable -- through their mathematical analysis we would like to obtain insight into the recovered system's workings. Piecewise-linear (PL), ReLU-based RNNs (PLRNNs) have a strong track-record in this regard, representing SOTA DSR models while allowing mathematical insight by virtue of their PL design. However, all current PLRNN variants are discrete-time maps. This is in disaccord with the assumed continuous-time nature of most physical and biological processes, and makes it hard to accommodate data arriving at irregular temporal intervals. Neural ODEs are one solution, but they do not reach the DSR performance of PLRNNs and often lack their tractability. Here we develop theory for continuous-time PLRNNs (cPLRNNs): We present a novel algorithm for training and simulating such models, bypassing numerical integration by efficiently exploiting their PL structure. We further demonstrate how important topological objects like equilibria or limit cycles can be determined semi-analytically in trained models. We compare cPLRNNs to both their discrete-time cousins as well as Neural ODEs on DSR benchmarks, including systems with discontinuities which come with hard thresholds.

