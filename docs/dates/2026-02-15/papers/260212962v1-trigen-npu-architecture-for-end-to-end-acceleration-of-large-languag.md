---
layout: default
title: TriGen: NPU Architecture for End-to-End Acceleration of Large Language Models based on SW-HW Co-Design
---

# TriGen: NPU Architecture for End-to-End Acceleration of Large Language Models based on SW-HW Co-Design
**arXiv**：[2602.12962v1](https://arxiv.org/abs/2602.12962) · [PDF](https://arxiv.org/pdf/2602.12962.pdf)  
**作者**：Jonghun Lee, Junghoon Lee, Hyeonjin Kim, Seoho Jeon, Jisup Yoon, Hyunbin Park, Meejeong Park, Heonjae Ha  

**一句话要点**：提出TriGen NPU架构，通过软硬件协同设计加速资源受限设备上的大语言模型端到端执行。

**关键词**：NPU架构, 软硬件协同设计, 大语言模型加速, 低精度计算, 资源受限设备, 端到端执行

## 3 点简述
- 核心问题：大语言模型在资源受限设备上端到端执行困难，参数重用率低。
- 方法要点：采用微缩放低精度计算、快速准确查找表优化非线性操作、调度技术提升计算利用率。
- 实验或效果：在多种大语言模型上评估，平均性能提升2.73倍，内存传输减少52%，精度损失可忽略。

## 摘要（原文）

> Recent studies have extensively explored NPU architectures for accelerating AI inference in on-device environments, which are inherently resource-constrained. Meanwhile, transformer-based large language models (LLMs) have become dominant, with rapidly increasing model sizes but low degree of parameter reuse compared to conventional CNNs, making end-to-end execution on resource-limited devices extremely challenging. To address these challenges, we propose TriGen, a novel NPU architecture tailored for resource-constrained environments through software-hardware co-design. Firstly, TriGen adopts low-precision computation using microscaling (MX) to enable additional optimization opportunities while preserving accuracy, and resolves the issues that arise by employing such precision. Secondly, to jointly optimize both nonlinear and linear operations, TriGen eliminates the need for specialized hardware for essential nonlinear operations by using fast and accurate LUT, thereby maximizing performance gains and reducing hardware-cost in on-device environments, and finally, by taking practical hardware constraints into account, further employs scheduling techniques to maximize computational utilization even under limited on-chip memory capacity. We evaluate the performance of TriGen on various LLMs and show that TriGen achieves an average 2.73x performance speedup and 52% less memory transfer over the baseline NPU design with negligible accuracy loss.

