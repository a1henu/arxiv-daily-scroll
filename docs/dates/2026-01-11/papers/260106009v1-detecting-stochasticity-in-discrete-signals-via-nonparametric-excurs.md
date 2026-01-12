---
layout: default
title: Detecting Stochasticity in Discrete Signals via Nonparametric Excursion Theorem
---

# Detecting Stochasticity in Discrete Signals via Nonparametric Excursion Theorem
**arXiv**：[2601.06009v1](https://arxiv.org/abs/2601.06009) · [PDF](https://arxiv.org/pdf/2601.06009.pdf)  
**作者**：Sunia Tanweer, Firas A. Khasawneh  

**一句话要点**：提出基于非参数游程定理的框架，从单离散时间序列区分扩散随机过程与确定性信号。

**关键词**：随机过程检测, 非参数方法, 游程定理, 二次变差, 扩散检验, 时间序列分析

## 3 点简述
- 核心问题：如何仅用单离散时间序列区分扩散随机过程与确定性信号，避免主观方法。
- 方法要点：利用连续半鞅的游程定理，关联游程数与二次变差，构建数据驱动的扩散检验。
- 实验或效果：在典型随机系统、周期混沌映射和加性白噪声系统上验证，方法非参数且模型无关。

## 摘要（原文）

> We develop a practical framework for distinguishing diffusive stochastic processes from deterministic signals using only a single discrete time series. Our approach is based on classical excursion and crossing theorems for continuous semimartingales, which correlates number $N_\varepsilon$ of excursions of magnitude at least $\varepsilon$ with the quadratic variation $[X]_T$ of the process. The scaling law holds universally for all continuous semimartingales with finite quadratic variation, including general Ito diffusions with nonlinear or state-dependent volatility, but fails sharply for deterministic systems -- thereby providing a theoretically-certfied method of distinguishing between these dynamics, as opposed to the subjective entropy or recurrence based state of the art methods. We construct a robust data-driven diffusion test. The method compares the empirical excursion counts against the theoretical expectation. The resulting ratio $K(\varepsilon)=N_{\varepsilon}^{\mathrm{emp}}/N_{\varepsilon}^{\mathrm{theory}}$ is then summarized by a log-log slope deviation measuring the $\varepsilon^{-2}$ law that provides a classification into diffusion-like or not. We demonstrate the method on canonical stochastic systems, some periodic and chaotic maps and systems with additive white noise, as well as the stochastic Duffing system. The approach is nonparametric, model-free, and relies only on the universal small-scale structure of continuous semimartingales.

