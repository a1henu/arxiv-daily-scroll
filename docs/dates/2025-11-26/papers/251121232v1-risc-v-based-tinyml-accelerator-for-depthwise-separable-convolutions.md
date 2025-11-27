---
layout: default
title: RISC-V Based TinyML Accelerator for Depthwise Separable Convolutions in Edge AI
---

# RISC-V Based TinyML Accelerator for Depthwise Separable Convolutions in Edge AI
**arXiv**：[2511.21232v1](https://arxiv.org/abs/2511.21232) · [PDF](https://arxiv.org/pdf/2511.21232.pdf)  
**作者**：Muhammed Yildirim, Ozcan Ozturk  

**一句话要点**：提出RISC-V融合像素数据流加速器以解决边缘AI中深度可分离卷积的内存墙问题

**关键词**：边缘AI加速器, 深度可分离卷积, RISC-V处理器, 数据流优化, 内存墙缓解, TinyML硬件

## 3 点简述
- 核心问题：深度可分离卷积逐层执行导致中间特征图传输能耗高、延迟大
- 方法要点：采用融合像素数据流，无中间缓冲，通过流水线完成所有阶段计算
- 实验或效果：FPGA实现59.3倍加速，ASIC合成显示小面积低功耗

## 摘要（原文）

> The increasing demand for on-device intelligence in Edge AI and TinyML applications requires the efficient execution of modern Convolutional Neural Networks (CNNs). While lightweight architectures like MobileNetV2 employ Depthwise Separable Convolutions (DSC) to reduce computational complexity, their multi-stage design introduces a critical performance bottleneck inherent to layer-by-layer execution: the high energy and latency cost of transferring intermediate feature maps to either large on-chip buffers or off-chip DRAM. To address this memory wall, this paper introduces a novel hardware accelerator architecture that utilizes a fused pixel-wise dataflow. Implemented as a Custom Function Unit (CFU) for a RISC-V processor, our architecture eliminates the need for intermediate buffers entirely, reducing the data movement up to 87\% compared to conventional layer-by-layer execution. It computes a single output pixel to completion across all DSC stages-expansion, depthwise convolution, and projection-by streaming data through a tightly-coupled pipeline without writing to memory. Evaluated on a Xilinx Artix-7 FPGA, our design achieves a speedup of up to 59.3x over the baseline software execution on the RISC-V core. Furthermore, ASIC synthesis projects a compact 0.284 mm$^2$ footprint with 910 mW power at 2 GHz in 28 nm, and a 1.20 mm$^2$ footprint with 233 mW power at 300 MHz in 40 nm. This work confirms the feasibility of a zero-buffer dataflow within a TinyML resource envelope, offering a novel and effective strategy for overcoming the memory wall in edge AI accelerators.

