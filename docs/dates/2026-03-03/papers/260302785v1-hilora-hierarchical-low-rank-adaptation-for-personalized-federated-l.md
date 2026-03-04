---
layout: default
title: HiLoRA: Hierarchical Low-Rank Adaptation for Personalized Federated Learning
---

# HiLoRA: Hierarchical Low-Rank Adaptation for Personalized Federated Learning
**arXiv**：[2603.02785v1](https://arxiv.org/abs/2603.02785) · [PDF](https://arxiv.org/pdf/2603.02785.pdf)  
**作者**：Zihao Peng, Nan Zou, Jiandian Zeng, Guo Li, Ke Chen, Boyuan Li, Tian Wang  

**一句话要点**：提出HiLoRA分层低秩适配框架，以解决联邦学习中ViT个性化调优的客户结构忽略问题。

**关键词**：联邦学习, 低秩适配, 视觉Transformer, 个性化调优, 分层结构, 子空间聚类

## 3 点简述
- 现有基于LoRA的联邦调优方法忽视真实场景中的潜在客户结构，限制共享表示学习。
- HiLoRA在根、簇、叶三级部署适配器，通过跨层正交性和级联优化分离更新子空间。
- 在CIFAR-100和DomainNet上实验显示，HiLoRA在个性化和泛化方面均取得一致提升。

## 摘要（原文）

> Vision Transformers (ViTs) have been widely adopted in vision tasks due to their strong transferability. In Federated Learning (FL), where full fine-tuning is communication heavy, Low-Rank Adaptation (LoRA) provides an efficient and communication-friendly way to adapt ViTs. However, existing LoRA-based federated tuning methods overlook latent client structures in real-world settings, limiting shared representation learning and hindering effective adaptation to unseen clients. To address this, we propose HiLoRA, a hierarchical LoRA framework that places adapters at three levels: root, cluster, and leaf, each designed to capture global, subgroup, and client-specific knowledge, respectively. Through cross-tier orthogonality and cascaded optimization, HiLoRA separates update subspaces and aligns each tier with its residual personalized objective. In particular, we develop a LoRA-Subspace Adaptive Clustering mechanism that infers latent client groups via subspace similarity analysis, thereby facilitating knowledge sharing across structurally aligned clients. Theoretically, we establish a tier-wise generalization analysis that supports HiLoRA's design. Experiments on ViT backbones with CIFAR-100 and DomainNet demonstrate consistent improvements in both personalization and generalization.

