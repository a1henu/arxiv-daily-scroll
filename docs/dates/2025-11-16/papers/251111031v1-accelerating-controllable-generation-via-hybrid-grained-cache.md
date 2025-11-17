---
layout: default
title: Accelerating Controllable Generation via Hybrid-grained Cache
---

# Accelerating Controllable Generation via Hybrid-grained Cache
**arXiv**：[2511.11031v1](https://arxiv.org/abs/2511.11031) · [PDF](https://arxiv.org/pdf/2511.11031.pdf)  
**作者**：Lin Liu, Huixia Ben, Shuo Wang, Jinda Lu, Junxiang Qiu, Shengeng Tang, Yanbin Hao  

**一句话要点**：提出混合粒度缓存以加速可控生成模型的计算效率

**关键词**：可控生成模型, 计算效率优化, 缓存策略, 特征重用, 跨注意力图

## 3 点简述
- 可控生成模型计算需求高，导致生成效率普遍较低
- 采用块级粗粒度缓存和提示级细粒度缓存，动态绕过冗余计算
- 在COCO-Stuff数据集上，计算成本降低63%，语义保真度损失小于1.5%

## 摘要（原文）

> Controllable generative models have been widely used to improve the realism of synthetic visual content. However, such models must handle control conditions and content generation computational requirements, resulting in generally low generation efficiency. To address this issue, we propose a Hybrid-Grained Cache (HGC) approach that reduces computational overhead by adopting cache strategies with different granularities at different computational stages. Specifically, (1) we use a coarse-grained cache (block-level) based on feature reuse to dynamically bypass redundant computations in encoder-decoder blocks between each step of model reasoning. (2) We design a fine-grained cache (prompt-level) that acts within a module, where the fine-grained cache reuses cross-attention maps within consecutive reasoning steps and extends them to the corresponding module computations of adjacent steps. These caches of different granularities can be seamlessly integrated into each computational link of the controllable generation process. We verify the effectiveness of HGC on four benchmark datasets, especially its advantages in balancing generation efficiency and visual quality. For example, on the COCO-Stuff segmentation benchmark, our HGC significantly reduces the computational cost (MACs) by 63% (from 18.22T to 6.70T), while keeping the loss of semantic fidelity (quantized performance degradation) within 1.5%.

