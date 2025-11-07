---
layout: default
title: Cambrian-S: Towards Spatial Supersensing in Video
---

# Cambrian-S: Towards Spatial Supersensing in Video
**arXiv**：[2511.04670v1](https://arxiv.org/abs/2511.04670) · [PDF](https://arxiv.org/pdf/2511.04670.pdf)  
**作者**：Shusheng Yang, Jihan Yang, Pinzhi Huang, Ellis Brown, Zihao Yang, Yue Yu, Shengbang Tong, Zihan Zheng, Yifan Xu, Muhan Wang, Daohan Lu, Rob Fergus, Yann LeCun, Li Fei-Fei, Saining Xie  

**一句话要点**：提出Cambrian-S模型与VSI-SUPER基准以推动视频空间超感知能力

**关键词**：空间超感知, 长视频理解, 自监督预测, 视觉基准, 世界建模, 事件分割

## 3 点简述
- 核心问题：当前AI系统缺乏空间超感知，无法处理长视频中的语义、事件、3D空间和预测建模
- 方法要点：引入VSI-SUPER基准和自监督预测器，利用预测误差驱动记忆与事件分割
- 实验或效果：在VSI-Bench上提升30%，但VSI-SUPER表现有限，显示仅靠数据扩展不足

## 摘要（原文）

> We argue that progress in true multimodal intelligence calls for a shift from
> reactive, task-driven systems and brute-force long context towards a broader
> paradigm of supersensing. We frame spatial supersensing as four stages beyond
> linguistic-only understanding: semantic perception (naming what is seen),
> streaming event cognition (maintaining memory across continuous experiences),
> implicit 3D spatial cognition (inferring the world behind pixels), and
> predictive world modeling (creating internal models that filter and organize
> information). Current benchmarks largely test only the early stages, offering
> narrow coverage of spatial cognition and rarely challenging models in ways that
> require true world modeling. To drive progress in spatial supersensing, we
> present VSI-SUPER, a two-part benchmark: VSR (long-horizon visual spatial
> recall) and VSC (continual visual spatial counting). These tasks require
> arbitrarily long video inputs yet are resistant to brute-force context
> expansion. We then test data scaling limits by curating VSI-590K and training
> Cambrian-S, achieving +30% absolute improvement on VSI-Bench without
> sacrificing general capabilities. Yet performance on VSI-SUPER remains limited,
> indicating that scale alone is insufficient for spatial supersensing. We
> propose predictive sensing as a path forward, presenting a proof-of-concept in
> which a self-supervised next-latent-frame predictor leverages surprise
> (prediction error) to drive memory and event segmentation. On VSI-SUPER, this
> approach substantially outperforms leading proprietary baselines, showing that
> spatial supersensing requires models that not only see but also anticipate,
> select, and organize experience.

