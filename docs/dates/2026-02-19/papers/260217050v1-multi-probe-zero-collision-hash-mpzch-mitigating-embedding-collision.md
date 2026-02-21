---
layout: default
title: Multi-Probe Zero Collision Hash (MPZCH): Mitigating Embedding Collisions and Enhancing Model Freshness in Large-Scale Recommenders
---

# Multi-Probe Zero Collision Hash (MPZCH): Mitigating Embedding Collisions and Enhancing Model Freshness in Large-Scale Recommenders
**arXiv**：[2602.17050v1](https://arxiv.org/abs/2602.17050) · [PDF](https://arxiv.org/pdf/2602.17050.pdf)  
**作者**：Ziliang Zhao, Bi Xue, Emma Lin, Mengjiao Zhou, Kaustubh Vartak, Shakhzod Ali-Zade, Carson Lu, Tao Li, Bin Kuang, Rui Jian, Bin Wen, Dennis van der Staay, Yixin Bao, Eddy Li, Chao Deng, Songbin Liu, Qifan Wang, Kai Ren  

**一句话要点**：提出多探针零碰撞哈希以解决大规模推荐系统中嵌入碰撞和模型陈旧问题

**关键词**：嵌入碰撞缓解, 模型新鲜度增强, 大规模推荐系统, 线性探测哈希, TorchRec库

## 3 点简述
- 传统哈希索引在ID量增长时导致嵌入碰撞，降低模型性能和个人化质量
- 基于线性探测的多探针零碰撞哈希通过辅助张量和CUDA内核实现可配置探测和主动淘汰策略
- 在线实验显示用户嵌入零碰撞，显著提升项目嵌入新鲜度和质量，训练和推理效率与现有方法相当

## 摘要（原文）

> Embedding tables are critical components of large-scale recommendation systems, facilitating the efficient mapping of high-cardinality categorical features into dense vector representations. However, as the volume of unique IDs expands, traditional hash-based indexing methods suffer from collisions that degrade model performance and personalization quality. We present Multi-Probe Zero Collision Hash (MPZCH), a novel indexing mechanism based on linear probing that effectively mitigates embedding collisions. With reasonable table sizing, it often eliminates these collisions entirely while maintaining production-scale efficiency. MPZCH utilizes auxiliary tensors and high-performance CUDA kernels to implement configurable probing and active eviction policies. By retiring obsolete IDs and resetting reassigned slots, MPZCH prevents the stale embedding inheritance typical of hash-based methods, ensuring new features learn effectively from scratch. Despite its collision-mitigation overhead, the system maintains training QPS and inference latency comparable to existing methods. Rigorous online experiments demonstrate that MPZCH achieves zero collisions for user embeddings and significantly improves item embedding freshness and quality. The solution has been released within the open-source TorchRec library for the broader community.

