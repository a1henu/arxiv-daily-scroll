---
layout: default
title: Halt the Hallucination: Decoupling Signal and Semantic OOD Detection Based on Cascaded Early Rejection
---

# Halt the Hallucination: Decoupling Signal and Semantic OOD Detection Based on Cascaded Early Rejection
**arXiv**：[2602.06330v1](https://arxiv.org/abs/2602.06330) · [PDF](https://arxiv.org/pdf/2602.06330.pdf)  
**作者**：Ningkang Peng, Chuanjie Cheng, Jingyang Mao, Xiaoqian Peng, Feng Xing, Bo Zhang, Chao Tan, Zhichao Zheng, Peiheng Li, Yanhui Gu  

**一句话要点**：提出级联早期拒绝框架以解决分布外检测中的计算浪费和语义幻觉问题

**关键词**：分布外检测, 级联早期拒绝, 语义幻觉, 异常检测, 计算效率

## 3 点简述
- 核心问题：现有方法对低层统计噪声进行全尺度推理，导致资源浪费和语义幻觉。
- 方法要点：通过结构能量筛和语义感知超球能量检测器，实现从粗到细的层次化异常过滤。
- 实验或效果：在CIFAR-100基准上，FPR95从33.58%降至22.84%，AUROC达93.97%，计算开销减少32%。

## 摘要（原文）

> Efficient and robust Out-of-Distribution (OOD) detection is paramount for safety-critical applications.However, existing methods still execute full-scale inference on low-level statistical noise. This computational mismatch not only incurs resource waste but also induces semantic hallucination, where deep networks forcefully interpret physical anomalies as high-confidence semantic features.To address this, we propose the Cascaded Early Rejection (CER) framework, which realizes hierarchical filtering for anomaly detection via a coarse-to-fine logic.CER comprises two core modules: 1)Structural Energy Sieve (SES), which establishes a non-parametric barrier at the network entry using the Laplacian operator to efficiently intercept physical signal anomalies; and 2) the Semantically-aware Hyperspherical Energy (SHE) detector, which decouples feature magnitude from direction in intermediate layers to identify fine-grained semantic deviations. Experimental results demonstrate that CER not only reduces computational overhead by 32% but also achieves a significant performance leap on the CIFAR-100 benchmark:the average FPR95 drastically decreases from 33.58% to 22.84%, and AUROC improves to 93.97%. Crucially, in real-world scenarios simulating sensor failures, CER exhibits performance far exceeding state-of-the-art methods. As a universal plugin, CER can be seamlessly integrated into various SOTA models to provide performance gains.

