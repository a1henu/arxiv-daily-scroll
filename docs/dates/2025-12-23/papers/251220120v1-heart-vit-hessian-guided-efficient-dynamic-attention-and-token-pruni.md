---
layout: default
title: HEART-VIT: Hessian-Guided Efficient Dynamic Attention and Token Pruning in Vision Transformer
---

# HEART-VIT: Hessian-Guided Efficient Dynamic Attention and Token Pruning in Vision Transformer
**arXiv**：[2512.20120v1](https://arxiv.org/abs/2512.20120) · [PDF](https://arxiv.org/pdf/2512.20120.pdf)  
**作者**：Mohammad Helal Uddin, Liam Seymour, Sabur Baidya  

**一句话要点**：提出HEART-ViT框架，通过Hessian引导的动态注意力与令牌剪枝优化视觉Transformer在边缘设备的部署效率。

**关键词**：视觉Transformer优化, Hessian引导剪枝, 动态注意力机制, 令牌剪枝, 边缘计算部署, 计算效率提升

## 3 点简述
- 视觉Transformer存在二次注意力成本和冗余计算，阻碍在资源受限平台上的部署。
- HEART-ViT利用Hessian向量积估计令牌和注意力头的曲率加权敏感度，实现基于损失预算的剪枝决策。
- 在ImageNet数据集上，HEART-ViT减少FLOPs达49.4%，提升吞吐量46%，并在微调后保持或超越基线准确率。

## 摘要（原文）

> Vision Transformers (ViTs) deliver state-of-the-art accuracy but their quadratic attention cost and redundant computations severely hinder deployment on latency and resource-constrained platforms. Existing pruning approaches treat either tokens or heads in isolation, relying on heuristics or first-order signals, which often sacrifice accuracy or fail to generalize across inputs. We introduce HEART-ViT, a Hessian-guided efficient dynamic attention and token pruning framework for vision transformers, which to the best of our knowledge is the first unified, second-order, input-adaptive framework for ViT optimization. HEART-ViT estimates curvature-weighted sensitivities of both tokens and attention heads using efficient Hessian-vector products, enabling principled pruning decisions under explicit loss budgets.This dual-view sensitivity reveals an important structural insight: token pruning dominates computational savings, while head pruning provides fine-grained redundancy removal, and their combination achieves a superior trade-off. On ImageNet-100 and ImageNet-1K with ViT-B/16 and DeiT-B/16, HEART-ViT achieves up to 49.4 percent FLOPs reduction, 36 percent lower latency, and 46 percent higher throughput, while consistently matching or even surpassing baseline accuracy after fine-tuning, for example 4.7 percent recovery at 40 percent token pruning. Beyond theoretical benchmarks, we deploy HEART-ViT on different edge devices such as AGX Orin, demonstrating that our reductions in FLOPs and latency translate directly into real-world gains in inference speed and energy efficiency. HEART-ViT bridges the gap between theory and practice, delivering the first unified, curvature-driven pruning framework that is both accuracy-preserving and edge-efficient.

