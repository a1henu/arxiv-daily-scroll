---
layout: default
title: Reliable and Resilient Collective Communication Library for LLM Training and Serving
---

# Reliable and Resilient Collective Communication Library for LLM Training and Serving
**arXiv**：[2512.25059v1](https://arxiv.org/abs/2512.25059) · [PDF](https://arxiv.org/pdf/2512.25059.pdf)  
**作者**：Wei Wang, Nengneng Yu, Sixian Xiong, Zaoxing Liu  

**一句话要点**：提出R²CCL容错通信库以解决大规模LLM训练与推理中的网络故障问题

**关键词**：容错通信库, LLM训练, 网络故障恢复, 多NIC硬件, 集体通信, GPU集群

## 3 点简述
- 核心问题：大规模GPU集群中网络故障导致GPU时间浪费10-15%，传统超时机制常终止作业
- 方法要点：利用多NIC硬件实现无损低开销故障转移，包括快速连接迁移、带宽感知负载重分配和弹性集体算法
- 实验或效果：在8-GPU H100服务器和模拟数百GPU场景中，R²CCL对NIC故障高度鲁棒，训练开销<1%，推理开销<3%，优于基线

## 摘要（原文）

> Modern ML training and inference now span tens to tens of thousands of GPUs, where network faults can waste 10--15\% of GPU hours due to slow recovery. Common network errors and link fluctuations trigger timeouts that often terminate entire jobs, forcing expensive checkpoint rollback during training and request reprocessing during inference. We present R$^2$CCL, a fault-tolerant communication library that provides lossless, low-overhead failover by exploiting multi-NIC hardware. R$^2$CCL performs rapid connection migration, bandwidth-aware load redistribution, and resilient collective algorithms to maintain progress under failures. We evaluate R$^2$CCL on two 8-GPU H100 InfiniBand servers and via large-scale ML simulators modeling hundreds of GPUs with diverse failure patterns. Experiments show that R$^2$CCL is highly robust to NIC failures, incurring less than 1\% training and less than 3\% inference overheads. R$^2$CCL outperforms baselines AdapCC and DejaVu by 12.18$\times$ and 47$\times$, respectively.

