---
layout: default
title: PALUM: Part-based Attention Learning for Unified Motion Retargeting
---

# PALUM: Part-based Attention Learning for Unified Motion Retargeting
**arXiv**：[2601.07272v1](https://arxiv.org/abs/2601.07272) · [PDF](https://arxiv.org/pdf/2601.07272.pdf)  
**作者**：Siqi Liu, Maoyu Wang, Bo Dai, Cewu Lu  

**一句话要点**：提出PALUM以解决不同骨架结构间的运动重定向问题

**关键词**：运动重定向, 骨架无关表示, 注意力机制, 语义身体部位, 循环一致性, 计算机动画

## 3 点简述
- 核心问题：不同骨架拓扑结构下保持运动语义与质量的挑战
- 方法要点：基于语义身体部位划分和注意力机制学习骨架无关的运动表示
- 实验或效果：在多样骨架结构上实现优越性能，保持运动真实性和语义保真度

## 摘要（原文）

> Retargeting motion between characters with different skeleton structures is a fundamental challenge in computer animation. When source and target characters have vastly different bone arrangements, maintaining the original motion's semantics and quality becomes increasingly difficult. We present PALUM, a novel approach that learns common motion representations across diverse skeleton topologies by partitioning joints into semantic body parts and applying attention mechanisms to capture spatio-temporal relationships. Our method transfers motion to target skeletons by leveraging these skeleton-agnostic representations alongside target-specific structural information. To ensure robust learning and preserve motion fidelity, we introduce a cycle consistency mechanism that maintains semantic coherence throughout the retargeting process. Extensive experiments demonstrate superior performance in handling diverse skeletal structures while maintaining motion realism and semantic fidelity, even when generalizing to previously unseen skeleton-motion combinations. We will make our implementation publicly available to support future research.

