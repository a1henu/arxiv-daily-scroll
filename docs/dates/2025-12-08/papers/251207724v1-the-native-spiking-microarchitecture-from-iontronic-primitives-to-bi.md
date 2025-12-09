---
layout: default
title: The Native Spiking Microarchitecture: From Iontronic Primitives to Bit-Exact FP8 Arithmetic
---

# The Native Spiking Microarchitecture: From Iontronic Primitives to Bit-Exact FP8 Arithmetic
**arXiv**：[2512.07724v1](https://arxiv.org/abs/2512.07724) · [PDF](https://arxiv.org/pdf/2512.07724.pdf)  
**作者**：Zhengzheng Tang  

**一句话要点**：提出原生脉冲微架构，利用离子电子学基元实现FP8位精确算术，解决后硅基材的确定性计算难题。

**关键词**：原生脉冲微架构, 离子电子学基元, FP8位精确算术, 后硅基材, 确定性计算, 神经形态硬件

## 3 点简述
- 核心问题：基于埃级通道的随机模拟材料难以支持确定性位精确AI计算，如FP8，现有神经形态方法精度不足。
- 方法要点：将噪声神经元视为逻辑基元，引入空间组合流水线和粘性额外校正机制，实现从随机离子到确定性浮点的转换。
- 实验或效果：验证所有FP8对实现100%位精确对齐，线性层延迟降至O(log N)，加速17倍，物理模拟显示对极端膜泄漏的鲁棒性。

## 摘要（原文）

> The 2025 Nobel Prize in Chemistry for Metal-Organic Frameworks (MOFs) and recent breakthroughs by Huanting Wang's team at Monash University establish angstrom-scale channels as promising post-silicon substrates with native integrate-and-fire (IF) dynamics. However, utilizing these stochastic, analog materials for deterministic, bit-exact AI workloads (e.g., FP8) remains a paradox. Existing neuromorphic methods often settle for approximation, failing Transformer precision standards. To traverse the gap "from stochastic ions to deterministic floats," we propose a Native Spiking Microarchitecture. Treating noisy neurons as logic primitives, we introduce a Spatial Combinational Pipeline and a Sticky-Extra Correction mechanism. Validation across all 16,129 FP8 pairs confirms 100% bit-exact alignment with PyTorch. Crucially, our architecture reduces Linear layer latency to O(log N), yielding a 17x speedup. Physical simulations further demonstrate robustness against extreme membrane leakage (beta approx 0.01), effectively immunizing the system against the stochastic nature of the hardware.

