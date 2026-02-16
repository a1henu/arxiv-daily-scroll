---
layout: default
title: Quantization-Aware Collaborative Inference for Large Embodied AI Models
---

# Quantization-Aware Collaborative Inference for Large Embodied AI Models
**arXiv**：[2602.13052v1](https://arxiv.org/abs/2602.13052) · [PDF](https://arxiv.org/pdf/2602.13052.pdf)  
**作者**：Zhonghao Lyu, Ming Xiao, Mikael Skoglund, Merouane Debbah, H. Vincent Poor  

**一句话要点**：提出量化感知协同推理方法，以解决资源受限具身AI系统中大型模型部署的挑战。

**关键词**：量化感知协同推理, 大型AI模型部署, 具身AI系统, 率失真分析, 边缘计算优化

## 3 点简述
- 核心问题：大型AI模型在资源受限具身代理中部署时面临参数规模大和计算需求高的挑战。
- 方法要点：开发量化诱导推理失真的可处理近似，推导量化率-失真函数上下界，并联合设计量化比特宽度和计算频率。
- 实验或效果：通过仿真和真实测试验证失真近似、率失真界及联合设计的有效性，平衡推理质量、延迟和能耗。

## 摘要（原文）

> Large artificial intelligence models (LAIMs) are increasingly regarded as a core intelligence engine for embodied AI applications. However, the massive parameter scale and computational demands of LAIMs pose significant challenges for resource-limited embodied agents. To address this issue, we investigate quantization-aware collaborative inference (co-inference) for embodied AI systems. First, we develop a tractable approximation for quantization-induced inference distortion. Based on this approximation, we derive lower and upper bounds on the quantization rate-inference distortion function, characterizing its dependence on LAIM statistics, including the quantization bit-width. Next, we formulate a joint quantization bit-width and computation frequency design problem under delay and energy constraints, aiming to minimize the distortion upper bound while ensuring tightness through the corresponding lower bound. Extensive evaluations validate the proposed distortion approximation, the derived rate-distortion bounds, and the effectiveness of the proposed joint design. Particularly, simulations and real-world testbed experiments demonstrate the effectiveness of the proposed joint design in balancing inference quality, latency, and energy consumption in edge embodied AI systems.

