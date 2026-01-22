---
layout: default
title: Communication-Efficient Multi-Modal Edge Inference via Uncertainty-Aware Distributed Learning
---

# Communication-Efficient Multi-Modal Edge Inference via Uncertainty-Aware Distributed Learning
**arXiv**：[2601.14942v1](https://arxiv.org/abs/2601.14942) · [PDF](https://arxiv.org/pdf/2601.14942.pdf)  
**作者**：Hang Zhao, Hongru Li, Dongfang Xu, Shenghui Song, Khaled B. Letaief  

**一句话要点**：提出三阶段通信感知分布式学习框架，以提升多模态边缘推理的通信效率和鲁棒性。

**关键词**：多模态边缘推理, 通信效率, 分布式学习, 不确定性校准, 自监督学习, 语义通信

## 3 点简述
- 核心问题：多模态边缘推理面临通信开销大和鲁棒性不足的挑战，尤其在带宽受限的无线链路上。
- 方法要点：采用本地自监督学习、分布式微调与证据融合、不确定性引导反馈机制，分阶段优化训练和推理。
- 实验或效果：在RGB-深度室内场景分类中，以更少通信轮次实现更高准确率，对模态退化或信道变化保持鲁棒。

## 摘要（原文）

> Semantic communication is emerging as a key enabler for distributed edge intelligence due to its capability to convey task-relevant meaning. However, achieving communication-efficient training and robust inference over wireless links remains challenging. This challenge is further exacerbated for multi-modal edge inference (MMEI) by two factors: 1) prohibitive communication overhead for distributed learning over bandwidth-limited wireless links, due to the \emph{multi-modal} nature of the system; and 2) limited robustness under varying channels and noisy multi-modal inputs. In this paper, we propose a three-stage communication-aware distributed learning framework to improve training and inference efficiency while maintaining robustness over wireless channels. In Stage~I, devices perform local multi-modal self-supervised learning to obtain shared and modality-specific encoders without device--server exchange, thereby reducing the communication cost. In Stage~II, distributed fine-tuning with centralized evidential fusion calibrates per-modality uncertainty and reliably aggregates features distorted by noise or channel fading. In Stage~III, an uncertainty-guided feedback mechanism selectively requests additional features for uncertain samples, optimizing the communication--accuracy tradeoff in the distributed setting. Experiments on RGB--depth indoor scene classification show that the proposed framework attains higher accuracy with far fewer training communication rounds and remains robust to modality degradation or channel variation, outperforming existing self-supervised and fully supervised baselines.

