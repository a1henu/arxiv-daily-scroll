---
layout: default
title: Geometry- and Relation-Aware Diffusion for EEG Super-Resolution
---

# Geometry- and Relation-Aware Diffusion for EEG Super-Resolution
**arXiv**：[2602.02238v1](https://arxiv.org/abs/2602.02238) · [PDF](https://arxiv.org/pdf/2602.02238.pdf)  
**作者**：Laura Yao, Gengwei Zhang, Moajjem Chowdhury, Yunmei Liu, Tianlong Chen  

**一句话要点**：提出TopoDiff以解决EEG空间超分辨率中缺乏生理空间结构感知的问题

**关键词**：脑电图超分辨率, 扩散模型, 拓扑感知, 通道关系图, 空间生成, 下游任务

## 3 点简述
- 核心问题：现有EEG空间超分辨率方法缺乏对生理空间结构的感知，限制空间生成性能
- 方法要点：结合拓扑感知图像嵌入和动态通道关系图，提供全局几何上下文和时变电极关系
- 实验或效果：在多个EEG数据集上实现生成保真度提升和下游任务性能改进

## 摘要（原文）

> Recent electroencephalography (EEG) spatial super-resolution (SR) methods, while showing improved quality by either directly predicting missing signals from visible channels or adapting latent diffusion-based generative modeling to temporal data, often lack awareness of physiological spatial structure, thereby constraining spatial generation performance. To address this issue, we introduce TopoDiff, a geometry- and relation-aware diffusion model for EEG spatial super-resolution. Inspired by how human experts interpret spatial EEG patterns, TopoDiff incorporates topology-aware image embeddings derived from EEG topographic representations to provide global geometric context for spatial generation, together with a dynamic channel-relation graph that encodes inter-electrode relationships and evolves with temporal dynamics. This design yields a spatially grounded EEG spatial super-resolution framework with consistent performance improvements. Across multiple EEG datasets spanning diverse applications, including SEED/SEED-IV for emotion recognition, PhysioNet motor imagery (MI/MM), and TUSZ for seizure detection, our method achieves substantial gains in generation fidelity and leads to notable improvements in downstream EEG task performance.

