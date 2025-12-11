---
layout: default
title: A Distributed Framework for Privacy-Enhanced Vision Transformers on the Edge
---

# A Distributed Framework for Privacy-Enhanced Vision Transformers on the Edge
**arXiv**：[2512.09309v1](https://arxiv.org/abs/2512.09309) · [PDF](https://arxiv.org/pdf/2512.09309.pdf)  
**作者**：Zihao Ding, Mufeng Zhu, Zhongze Tang, Sheng Wei, Yao Liu  

**一句话要点**：提出分布式隐私增强视觉Transformer边缘框架，以解决资源受限设备视觉任务中的隐私泄露问题。

**关键词**：隐私保护, 边缘计算, 视觉Transformer, 分布式框架, 数据分片

## 3 点简述
- 核心问题：视觉智能工具计算需求高，云端卸载易导致传输和服务器端隐私漏洞。
- 方法要点：使用可信边缘设备作为协调器，将视觉数据分片分发至多个独立云服务器，防止单服务器完整重建。
- 实验或效果：以Segment Anything Model为例，保持近基线分割性能，显著降低内容重建和用户数据暴露风险。

## 摘要（原文）

> Nowadays, visual intelligence tools have become ubiquitous, offering all kinds of convenience and possibilities. However, these tools have high computational requirements that exceed the capabilities of resource-constrained mobile and wearable devices. While offloading visual data to the cloud is a common solution, it introduces significant privacy vulnerabilities during transmission and server-side computation. To address this, we propose a novel distributed, hierarchical offloading framework for Vision Transformers (ViTs) that addresses these privacy challenges by design. Our approach uses a local trusted edge device, such as a mobile phone or an Nvidia Jetson, as the edge orchestrator. This orchestrator partitions the user's visual data into smaller portions and distributes them across multiple independent cloud servers. By design, no single external server possesses the complete image, preventing comprehensive data reconstruction. The final data merging and aggregation computation occurs exclusively on the user's trusted edge device. We apply our framework to the Segment Anything Model (SAM) as a practical case study, which demonstrates that our method substantially enhances content privacy over traditional cloud-based approaches. Evaluations show our framework maintains near-baseline segmentation performance while substantially reducing the risk of content reconstruction and user data exposure. Our framework provides a scalable, privacy-preserving solution for vision tasks in the edge-cloud continuum.

