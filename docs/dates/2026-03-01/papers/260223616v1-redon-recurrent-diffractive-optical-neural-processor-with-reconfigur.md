---
layout: default
title: ReDON: Recurrent Diffractive Optical Neural Processor with Reconfigurable Self-Modulated Nonlinearity
---

# ReDON: Recurrent Diffractive Optical Neural Processor with Reconfigurable Self-Modulated Nonlinearity
**arXiv**：[2602.23616v1](https://arxiv.org/abs/2602.23616) · [PDF](https://arxiv.org/pdf/2602.23616.pdf)  
**作者**：Ziang Yin, Qi Jing, Raktim Sarma, Rena Huang, Yu Yao, Jiaqi Gu  

**一句话要点**：提出ReDON以解决衍射光学神经网络中非线性响应和可重配置性不足的问题。

**关键词**：衍射光学神经网络, 可重配置非线性, 循环自调制, 非冯·诺依曼架构, 光学计算, 图像识别

## 3 点简述
- 核心问题：传统衍射光学神经网络因静态相位掩模缺乏高效非线性响应和可重配置性，计算表达能力受限。
- 方法要点：引入可重配置的循环自调制非线性机制，通过电光自调制实现动态、输入依赖的光学传输，提升非线性表示能力。
- 实验或效果：在图像识别和分割基准测试中，相比先前方法，ReDON在模型复杂度相近且功耗增加可忽略的情况下，准确率和mIoU提升高达20%。

## 摘要（原文）

> Diffractive optical neural networks (DONNs) have demonstrated unparalleled energy efficiency and parallelism by processing information directly in the optical domain. However, their computational expressivity is constrained by static, passive diffractive phase masks that lack efficient nonlinear responses and reprogrammability. To address these limitations, we introduce the Recurrent Diffractive Optical Neural Processor (ReDON), a novel architecture featuring reconfigurable, recurrent self-modulated nonlinearity. This mechanism enables dynamic, input-dependent optical transmission through in-situ electro-optic self-modulation, providing a highly efficient and reprogrammable approach to optical computation. Inspired by the gated linear unit (GLU) used in large language models, ReDON senses a fraction of the propagating optical field and modulates its phase or intensity via a lightweight parametric function, enabling effective nonlinearity with minimal inference overhead. As a non-von Neumann architecture in which the primary weighting elements (metasurfaces) remain fixed, ReDON substantially extends the nonlinear representational capacity and task adaptability of conventional DONNs through recurrent optical hardware reuse and dynamically tunable nonlinearity. We systematically investigate various self-modulation configurations to characterize the trade-offs between hardware efficiency and computational expressivity. On image recognition and segmentation benchmarks, ReDON improves test accuracy and mean intersection-over-union (mIoU) by up to 20% compared with prior DONNs employing either optical or digital nonlinearities at comparable model complexity and negligible additional power consumption. This work establishes a new paradigm for reconfigurable nonlinear optical computing, uniting recurrence and self-modulation within non-von Neumann analog processors.

