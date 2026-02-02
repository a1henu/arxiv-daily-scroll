---
layout: default
title: Segment Any Events with Language
---

# Segment Any Events with Language
**arXiv**：[2601.23159v1](https://arxiv.org/abs/2601.23159) · [PDF](https://arxiv.org/pdf/2601.23159.pdf)  
**作者**：Seungjun Lee, Gim Hee Lee  

**一句话要点**：提出SEAL框架以解决开放词汇事件实例分割问题，支持多粒度分割与分类。

**关键词**：事件传感器, 开放词汇实例分割, 多粒度分割, 视觉提示, 参数高效架构

## 3 点简述
- 核心问题：事件传感器场景理解研究稀缺，缺乏开放词汇实例分割方法。
- 方法要点：SEAL为统一框架，结合视觉提示实现事件分割与开放词汇掩码分类。
- 实验或效果：在四个基准测试中性能与推理速度显著优于基线，参数高效。

## 摘要（原文）

> Scene understanding with free-form language has been widely explored within diverse modalities such as images, point clouds, and LiDAR. However, related studies on event sensors are scarce or narrowly centered on semantic-level understanding. We introduce SEAL, the first Semantic-aware Segment Any Events framework that addresses Open-Vocabulary Event Instance Segmentation (OV-EIS). Given the visual prompt, our model presents a unified framework to support both event segmentation and open-vocabulary mask classification at multiple levels of granularity, including instance-level and part-level. To enable thorough evaluation on OV-EIS, we curate four benchmarks that cover label granularity from coarse to fine class configurations and semantic granularity from instance-level to part-level understanding. Extensive experiments show that our SEAL largely outperforms proposed baselines in terms of performance and inference speed with a parameter-efficient architecture. In the Appendix, we further present a simple variant of our SEAL achieving generic spatiotemporal OV-EIS that does not require any visual prompts from users in the inference. Check out our project page in https://0nandon.github.io/SEAL

