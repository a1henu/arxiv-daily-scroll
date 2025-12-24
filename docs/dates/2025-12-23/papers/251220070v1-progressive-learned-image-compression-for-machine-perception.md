---
layout: default
title: Progressive Learned Image Compression for Machine Perception
---

# Progressive Learned Image Compression for Machine Perception
**arXiv**：[2512.20070v1](https://arxiv.org/abs/2512.20070) · [PDF](https://arxiv.org/pdf/2512.20070.pdf)  
**作者**：Jungwoo Kim, Jun-Hyuk Kim, Jong-Seok Lee  

**一句话要点**：提出PICM-Net以实现面向机器感知的渐进式学习图像压缩

**关键词**：渐进式图像压缩, 机器感知, 学习图像编码, 三值平面编码, 自适应解码, 下游任务性能

## 3 点简述
- 核心问题：现有学习图像编码器缺乏面向机器感知的渐进压缩能力，无法从单一比特流解码多质量级别
- 方法要点：基于三值平面编码，分析人机感知率失真优先级差异，设计自适应解码控制器动态确定解码级别
- 实验或效果：实验表明该方法在保持下游分类任务高性能的同时，实现高效自适应渐进传输

## 摘要（原文）

> Recent advances in learned image codecs have been extended from human perception toward machine perception. However, progressive image compression with fine granular scalability (FGS)-which enables decoding a single bitstream at multiple quality levels-remains unexplored for machine-oriented codecs. In this work, we propose a novel progressive learned image compression codec for machine perception, PICM-Net, based on trit-plane coding. By analyzing the difference between human- and machine-oriented rate-distortion priorities, we systematically examine the latent prioritization strategies in terms of machine-oriented codecs. To further enhance real-world adaptability, we design an adaptive decoding controller, which dynamically determines the necessary decoding level during inference time to maintain the desired confidence of downstream machine prediction. Extensive experiments demonstrate that our approach enables efficient and adaptive progressive transmission while maintaining high performance in the downstream classification task, establishing a new paradigm for machine-aware progressive image compression.

