---
layout: default
title: Revisiting Parameter Server in LLM Post-Training
---

# Revisiting Parameter Server in LLM Post-Training
**arXiv**：[2601.19362v1](https://arxiv.org/abs/2601.19362) · [PDF](https://arxiv.org/pdf/2601.19362.pdf)  
**作者**：Xinyi Wan, Penghui Qi, Guangxing Huang, Chaoyi Ruan, Min Lin, Jialin Li  

**一句话要点**：提出On-Demand Communication以解决LLM后训练中负载不均衡导致的设备利用率低下问题

**关键词**：大语言模型后训练, 参数服务器, 负载均衡, 数据并行训练, 通信优化, 设备利用率

## 3 点简述
- LLM后训练中序列长度差异大，导致数据并行训练负载不均衡，集体通信造成同步障碍
- ODC将参数服务器融入FSDP，用点对点通信替代集体操作，减少同步次数并解耦设备负载
- 实验显示ODC提升设备利用率和训练吞吐量，在多种任务中比FSDP快达36%

## 摘要（原文）

> Modern data parallel (DP) training favors collective communication over parameter servers (PS) for its simplicity and efficiency under balanced workloads. However, the balanced workload assumption no longer holds in large language model (LLM) post-training due to the high variance in sequence lengths. Under imbalanced workloads, collective communication creates synchronization barriers, leading to under-utilization of devices with smaller workloads. This change in training dynamics calls for a revisit of the PS paradigm for its robustness to such imbalance. We propose \textbf{On-Demand Communication (ODC)}, which adapts PS into Fully Sharded Data Parallel (FSDP) by replacing collective all-gather and reduce-scatter with direct point-to-point communication. Compared to FSDP, ODC reduces the synchronization barrier from once per layer to once per minibatch and decouples the workload on each device so that faster workers are not stalled. It also enables simpler and more effective load balancing at the minibatch level. Across diverse LLM post-training tasks, ODC consistently improves device utilization and training throughput, achieving up to a 36\% speedup over standard FSDP. These results demonstrate that ODC is a superior fit for the prevalent imbalanced workloads in LLM post-training. Our implementation of ODC and integration with FSDP is open-sourced at https://github.com/sail-sg/odc.

